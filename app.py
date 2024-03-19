from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

# Load station names from JSON file
with open("stations.json") as f:
    station_data = json.load(f)
    stations = station_data["stations"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        source_station_input = request.form["source_station"]
        destination_station_input = request.form["destination_station"]

        # Process input and fetch data
        result = process_input(source_station_input, destination_station_input)
        return render_template("result.html", result=result)

    return render_template("index.html", stations=stations)

def process_input(source_station_input, destination_station_input):
    # Convert inputs to lowercase
    source_station_input = source_station_input.lower()
    destination_station_input = destination_station_input.lower()

    # Initialize variables to store station names and cities
    source_station = None
    destination_station = None
    source_city = None
    destination_city = None

    # Function to extract station and city names
    def extract_station_and_city(station_input):
        parts = station_input.split(", ")
        if len(parts) == 2:
            station_name = parts[0].replace(" ", "-")
            city_name = parts[1].replace(" ", "-")
            return station_name, city_name
        return None, None

    # Extract source station name and city
    source_station, source_city = extract_station_and_city(source_station_input)

    # Extract destination station name and city
    destination_station, destination_city = extract_station_and_city(destination_station_input)

    # Validate station and city names
    if source_station and destination_station and source_city and destination_city:
        # Format URL with station values
        url = f"https://yometro.com/from-{source_station}-metro-station-{source_city}-to-{destination_station}-metro-station-{destination_city}"
        
        try:
            # Send GET request to URL
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Find element with id "tabpanel1"
            tabpanel1 = soup.find(id="tabpanel1")

            if tabpanel1:
                result = {
                    "source_station": source_station_input.capitalize(),
                    "destination_station": destination_station_input.capitalize(),
                    "route_options": [],
                    "information": []
                }

                # Extract route options
                route_options = tabpanel1.find('table', class_='table').find_all('tr')
                for option in route_options:
                    result["route_options"].append(option.text.strip())

                # Extract information
                info_tables = tabpanel1.find_all('table', class_='table')
                if len(info_tables) >= 2:
                    info_table = info_tables[1]  # Second table contains the information
                    info_rows = info_table.find_all('tr')
                    for row in info_rows:
                        cells = row.find_all('td')
                        if len(cells) == 2:  # Ensure it's a data row
                            info = {
                                "label": cells[0].text.strip(),
                                "value": cells[1].text.strip()
                            }
                            result["information"].append(info)

                return result
            else:
                return {"error": "Not found."}
        except requests.RequestException as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid station name or city name."}

if __name__ == "__main__":
    app.run(debug=True)
