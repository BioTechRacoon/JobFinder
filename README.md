# JobFinder
This script allows you to scrape addresses within a specified perimeter based on a keyword search on Google Maps. It can be useful when you're looking for job opportunities. The script uses the Google Places API to retrieve nearby places based on a given address, radius, and keyword.

# Google Maps Address Scraper

This Python script enables you to scrape addresses within a specific perimeter based on a keyword search using the Google Maps API. It can be particularly helpful when you want to gather a list of potential job locations. The script utilizes the `requests` library for making HTTP requests and the `geopy` library for calculating distances.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your system
- API key for the Google Maps API. You can obtain one by following the instructions on the [Google Maps Platform documentation](https://developers.google.com/maps/gmp-get-started)

## Installation

1. Clone this repository to your local machine or download the script directly.

2. Install the required Python dependencies by running the following command:

pip install -r requirements.txt

## Usage

1. Open the script `google_maps_scraper.py` in a text editor.

2. Replace `'YOUR API KEY'` on line 6 with your actual Google Maps API key.

3. Modify the following variables according to your requirements:

- `address`: Specify the address around which you want to search for places.
- `radius`: Specify the radius (in meters) for the search area.
- `keyword`: Specify the keyword you want to search for.

4. Save the changes to the script.

5. Run the script by executing the following command:

python google_maps_scraper.py


6. The script will scrape the addresses and distances of the places matching the specified keyword within the given radius from the provided address.

7. Once the script finishes, it will create a CSV file named `google_maps_results.csv` containing the scraped data.

## Notes

- The script geocodes the specified address to retrieve its latitude and longitude coordinates. It then uses these coordinates for the nearby search.
- The results are sorted based on the distance from the specified address, from nearest to farthest.
- The script overwrites the existing `google_maps_results.csv` file if it already exists.
- You can open the CSV file with a spreadsheet program or use it as input for further analysis or processing.

**Note:** Ensure you comply with the terms of service and usage limits of the Google Maps API when using this script.

## License

This project is licensed under the [MIT License](LICENSE).
