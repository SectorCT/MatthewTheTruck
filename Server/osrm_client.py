import requests
import json

def get_trip_service(data):
    # Extract coordinates in the format "longitude,latitude" for each location
    coordinates = [f"{loc['longitude']},{loc['latitude']}" for loc in data['locations']]
    # Join coordinates with semicolons as required by the API
    coordinates_str = ";".join(coordinates)
    # Define the profile for the routing (using "driving" for car navigation)
    profile = "car"
    # Construct the base URL for the Trip Service API
    base_url = f"http://router.project-osrm.org/trip/v1/{profile}/{coordinates_str}?steps=false&geometries=geojson&annotations=false"
    # Make the GET request to the API
    response = requests.get(base_url)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response containing trip details
    else:
        return {"error": response.status_code}  # Return an error if the request fails

# Example usage with the provided data
data = {
    "locations": [
        {"name": "Sklad", "latitude": 42.6858, "longitude": 23.3189},
        {"name": "National Palace of Culture", "latitude": 42.6858, "longitude": 23.3189},
        {"name": "Alexander Nevsky Cathedral", "latitude": 42.6957, "longitude": 23.3320},
        {"name": "Vitosha Boulevard", "latitude": 42.6875, "longitude": 23.3190},
        {"name": "South Park", "latitude": 42.6662, "longitude": 23.3103},
        # {"name": "Borisova Gradina", "latitude": 42.6861, "longitude": 23.3390},
        # {"name": "Sofia University", "latitude": 42.6934, "longitude": 23.3340},
        # {"name": "Serdika Center", "latitude": 42.6968, "longitude": 23.3483},
        # {"name": "Boyana Church", "latitude": 42.6443, "longitude": 23.2666},
        # {"name": "Sofia Zoo", "latitude": 42.6521, "longitude": 23.3314},
        # {"name": "Lions' Bridge", "latitude": 42.7054, "longitude": 23.3217},
        # {"name": "Mladost 1 Metro Station", "latitude": 42.6561, "longitude": 23.3775},
        # {"name": "Mladost 2 Park", "latitude": 42.6552, "longitude": 23.3797},
        # {"name": "Mladost 4 Business Park", "latitude": 42.6257, "longitude": 23.3771},
        # {"name": "Lozenets Residential Area", "latitude": 42.6775, "longitude": 23.3199},
        # {"name": "Lozenets Park", "latitude": 42.6758, "longitude": 23.3211},
        # {"name": "Druzhba Lake", "latitude": 42.6613, "longitude": 23.3892},
        # {"name": "Druzhba 2 Park", "latitude": 42.6632, "longitude": 23.3875},
        # {"name": "Oborishte Park", "latitude": 42.6992, "longitude": 23.3398},
        # {"name": "Studentski Grad Central Area", "latitude": 42.6483, "longitude": 23.3447},
        # {"name": "Studentski Grad Park", "latitude": 42.6468, "longitude": 23.3469},
        # {"name": "Ovcha Kupel Metro Station", "latitude": 42.6725, "longitude": 23.2719},
        # {"name": "Ovcha Kupel Park", "latitude": 42.6708, "longitude": 23.2745}
    ]
}

# Call the function and print the result
result = json.dumps((get_trip_service(data)),indent = 4)
print(result)