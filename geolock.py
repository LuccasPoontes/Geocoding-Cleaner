from geopy.geocoders import ArcGIS
from unidecode import unidecode

# Initialize the geolocator
geolocator = ArcGIS()

# Coordinates to be converted
latitude = -21.9845750
longitude = -47.9103380

# Perform the reverse geocoding
location = geolocator.reverse((latitude, longitude))

# Extract the address and postal code
address = location.address
postal_code = location.raw.get('Postal')

# Clean up the address string to remove special character issues
clean_address = unidecode(address)

# Print the full address and ZIP code
print(f"Address: {clean_address}")
print(f"Full ZIP Code: {postal_code}")
