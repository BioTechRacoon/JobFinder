python
import csv
import requests
from geopy.distance import geodesic

API_KEY = 'YOUR API KEY'
URL = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={API_KEY}'

address = 'YOUR ADRESS'  # Specify your address
radius = 3000  # Specify the radius in meters for your search zone
keyword = 'KEY WORD'  # Specify the keyword for search

# Geocode the address to get the latitude and longitude coordinates
geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?key={API_KEY}&address={address}'
geocode_response = requests.get(geocode_url)
geocode_data = geocode_response.json()

# Extract latitude and longitude from the geocode response
location = geocode_data['results'][0]['geometry']['location']
lat = location['lat']
lng = location['lng']

# Set the parameters for the nearby search
params = {
    'location': f'{lat},{lng}',
    'radius': radius,
    'keyword': keyword
}

# Send the request to the Google Maps API
response = requests.get(URL, params=params)
data = response.json()
results = data['results']

# Calculate the distance between your address and each result
for result in results:
    result_location = result['geometry']['location']
    result_lat = result_location['lat']
    result_lng = result_location['lng']
    result_distance = geodesic((lat, lng), (result_lat, result_lng)).meters
    result['distance'] = result_distance

# Sort the results by distance from the nearest to the farthest
results = sorted(results, key=lambda x: x['distance'])

# Create and open the CSV file in write mode
with open('google_maps_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Address', 'Distance'])  # Write header row

    # Process the sorted results and write each row to the CSV file
    for result in results:
        name = result['name']
        address = result['vicinity']
        distance = result['distance']
        writer.writerow([name, address, distance])

print("CSV file created successfully.")
