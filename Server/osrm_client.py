import requests
import json

packages = {
    "locations": [       
        {"name": "Sklad", "latitude": 42.6858, "longitude": 23.3189},
        {"name": "Sofia Zoo", "latitude": 42.6521, "longitude": 23.3314},
        {"name": "Alexander Nevsky Cathedral", "latitude": 42.6957, "longitude": 23.3320},
        {"name": "Vitosha Boulevard", "latitude": 42.6875, "longitude": 23.3190},
        {"name": "South Park", "latitude": 42.6662, "longitude": 23.3103}
    ]
}

def osrm_trip_result(data):

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

    def extract_leg_routes(osrm_response):
        if "trips" not in osrm_response or not osrm_response["trips"]:
            return None

        trip = osrm_response["trips"][0]
        coords = trip["geometry"]["coordinates"]

        def find_coord_index(target, coords, tol=1e-6):
            for i, c in enumerate(coords):
                if abs(c[0] - target[0]) < tol and abs(c[1] - target[1]) < tol:
                    return i
            return None

        #podrejda paketi
        wp_indices = []
        for wp in osrm_response["waypoints"]:
            idx = find_coord_index(wp["location"], coords)
            if idx is not None:
                wp_indices.append((idx, wp))
        
        wp_indices.sort(key=lambda x: x[0])

        legs = trip["legs"]
        # legs = {"steps": [], "summary": "", "weight": 396.2, "duration": 393.6, "distance": 3219.8
        #         },
        # if len(legs) == len(wp_indices):
        #     legs = legs[:-1]
        #     # wp_indices = wp_indices[:-1]

        output = []

        for i ,_ in enumerate(wp_indices):
            if i == 0:
                #start point
                output.append({
                        "waypoint_index": 0,
                        "route": [coords[0]],
                        "location": coords[0],
                        "duration": 0
                    })
                continue

            start_idx = wp_indices[i-1][0]
            end_idx = wp_indices[i][0]

            segment = coords[start_idx:end_idx + 1] 
            leg_info = legs[i-1]
            wp = wp_indices[i][1]
            output.append({
                "waypoint_index": wp.get("waypoint_index"),
                "route": segment,
                "location": wp.get("location", []),
                "duration": leg_info.get("duration", 0)
            })

        return output

    osrm_response = get_trip_service(data)
    filtered_routes = extract_leg_routes(osrm_response)
    return(json.dumps(filtered_routes, indent=4))

print(osrm_trip_result(packages))
