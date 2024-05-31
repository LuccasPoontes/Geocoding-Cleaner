import requests
from unidecode import unidecode

# Coordinates to be converted
latitude = -23.3608000
longitude = -46.9233200

# OpenStreetMap Nominatim URL for reverse geocoding
url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}'

# Set the headers including User-Agent
headers = {
    'User-Agent': 'MyGeocodingApp/1.0 (your_email@example.com)'
}

# Make the request and get the response
response = requests.get(url, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    try:
        data = response.json()
        
        # Extract details
        address = data.get('address', {})
        road = address.get('road', 'N/A')
        house_number = address.get('house_number', 'N/A')
        neighbourhood = address.get('neighbourhood', 'N/A')
        city = address.get('city', 'N/A')
        state = address.get('state', 'N/A')
        postcode = address.get('postcode', 'N/A')

        # Clean up the strings to remove special character issues
        road = unidecode(road)
        house_number = unidecode(house_number)
        neighbourhood = unidecode(neighbourhood)
        city = unidecode(city)
        state = unidecode(state)
        postcode = unidecode(postcode)

        # Print the detailed address
        print(f"Address: {road}, {house_number}, {neighbourhood}, {city}, {state}, {postcode}")
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON.")
else:
    print(f"Request failed with status code {response.status_code}.")
    # Print the response content for debugging
    print("Response content:", response.text)
