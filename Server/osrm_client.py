import requests
import json

def get_trip_service(data):
    coordinates = [f"{loc['longitude']},{loc['latitude']}" for loc in data['locations']]
    coordinates_str = ";".join(coordinates)
    profile = "car"
    base_url = f"http://router.project-osrm.org/trip/v1/{profile}/{coordinates_str}?steps=false&geometries=geojson&annotations=false"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}

data = {
    "locations": [
        {"name": "Sklad", "latitude": 42.6858, "longitude": 23.3189},
        {"name": "Sofia Zoo", "latitude": 42.6521, "longitude": 23.3314},
        {"name": "Alexander Nevsky Cathedral", "latitude": 42.6957, "longitude": 23.3320},
        {"name": "Vitosha Boulevard", "latitude": 42.6875, "longitude": 23.3190},
        {"name": "South Park", "latitude": 42.6662, "longitude": 23.3103}
    ]
}

result = json.dumps((get_trip_service(data)),indent = 4)
# print(result)

def extract_leg_routes(osrm_response):
    if "trips" not in osrm_response or not osrm_response["trips"]:
        return None

    trip = osrm_response["trips"][0]
    coords = trip["geometry"]["coordinates"]

    # Helper to find the index in 'coords' where a waypoint's location occurs.
    def find_coord_index(target, coords, tol=1e-6):
        for i, c in enumerate(coords):
            if abs(c[0] - target[0]) < tol and abs(c[1] - target[1]) < tol:
                return i
        return None

    # Gather each waypoint with its index in the geometry
    wp_indices = []
    for wp in osrm_response["waypoints"]:
        idx = find_coord_index(wp["location"], coords)
        if idx is not None:
            wp_indices.append((idx, wp))
    
    # Sort waypoints by their occurrence in the full route
    wp_indices.sort(key=lambda x: x[0])

    # Remove return-to-start if detected
    legs = trip["legs"]
    if len(legs) == len(wp_indices):
        legs = legs[:-1]
        wp_indices = wp_indices[:-1]

    output = []
    for i in range(len(legs)):  # Fix: Prevent out-of-bounds error
        if i + 1 >= len(wp_indices):  
            break  # Prevent accessing beyond the last waypoint
        
        start_idx = wp_indices[i][0]
        end_idx = wp_indices[i+1][0]

        segment = coords[start_idx:end_idx + 1]  # Extract the sub-route
        leg_info = legs[i]
        wp = wp_indices[i+1][1]  # Destination waypoint
        
        output.append({
            "waypoint_index": wp.get("waypoint_index"),
            "trips_index": wp.get("trips_index"),
            "route": segment,
            "hint": wp.get("hint", ""),
            "distance": wp.get("distance", 0),
            "name": wp.get("name", ""),
            "location": wp.get("location", []),
            "leg_duration": leg_info.get("duration", 0)
        })

    return output

# Example usage:
osrm_response = get_trip_service(data)
filtered_routes = extract_leg_routes(osrm_response)
print(json.dumps(filtered_routes, indent=4))
