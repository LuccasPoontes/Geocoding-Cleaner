from flask import Flask, request, jsonify, send_from_directory
import requests
from unidecode import unidecode

app = Flask(__name__, static_folder="static")

@app.route('/')
def serve_index():
    # Serve o arquivo index.html da pasta "static"
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/reverse-geocode', methods=['POST'])
def reverse_geocode():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if not latitude or not longitude:
        return jsonify({"error": "Latitude and longitude are required"}), 400
    
    url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}'
    headers = {
        'User-Agent': 'MyGeocodingApp/1.0 (your_email@example.com)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            address = data.get('address', {})
            result = {
                "road": unidecode(address.get('road', 'N/A')),
                "house_number": unidecode(address.get('house_number', 'N/A')),
                "neighbourhood": unidecode(address.get('neighbourhood', 'N/A')),
                "city": unidecode(address.get('city', 'N/A')),
                "state": unidecode(address.get('state', 'N/A')),
                "postcode": unidecode(address.get('postcode', 'N/A'))
            }
            return jsonify(result), 200
        except requests.exceptions.JSONDecodeError:
            return jsonify({"error": "Invalid response from geocoding service"}), 500
    else:
        return jsonify({"error": f"Geocoding service failed with status code {response.status_code}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
