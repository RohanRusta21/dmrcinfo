# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # URL to scrape
# url = "https://delhimetrorail.info/kashmere-gate-delhi-metro-station-to-rajiv-chowk-delhi-metro-station"

# # Send a GET request to the URL
# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# #print(soup)
# ############# need table 1 and table 3
# a = soup.find_all('table')[1]
# #print(a)

# table_data = a.find_all('td')
# #print(table_data)


# td = [title.text.strip() for title in table_data]
# #print(td)

# # Indices of values you want to print
# indices_to_print = [0, 2, 4, 6, 8]

# # Print values at the specified indices
# for index in indices_to_print:
#     print(td[index])


































































































############################## correct code ##################################################


# import requests
# from bs4 import BeautifulSoup
# import json

# # Load station names from JSON file
# with open("stations.json") as f:
#     station_data = json.load(f)
#     stations = station_data["stations"]

# # Display available stations
# print("Available stations:")
# for i, station in enumerate(stations, 1):
#     print(f"{i}. {station}")

# # Prompt user to select source and destination stations by name
# source_station_input = input("Enter the name of the source station: ")
# destination_station_input = input("Enter the name of the destination station: ")

# # Convert inputs to lowercase
# source_station_input = source_station_input.lower()
# destination_station_input = destination_station_input.lower()

# # Initialize variables to store station names and cities
# source_station = None
# destination_station = None
# source_city = None
# destination_city = None

# # Function to extract station and city names
# def extract_station_and_city(station_input):
#     parts = station_input.split(", ")
#     if len(parts) == 2:
#         return parts[0], parts[1]
#     return None, None

# # Extract source station name and city
# source_station, source_city = extract_station_and_city(source_station_input)

# # Extract destination station name and city
# destination_station, destination_city = extract_station_and_city(destination_station_input)

# # Validate station and city names
# if source_station and destination_station and source_city and destination_city:
#     # Format URL with station values
#     url = f"https://yometro.com/from-{source_station.lower()}-metro-station-{source_city.lower()}-to-{destination_station.lower()}-metro-station-{destination_city.lower()}"
#     print(url)

#     # Send GET request to URL
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'html.parser')

#     # Find element with id "tabpanel1"
#     tabpanel1 = soup.find(id="tabpanel1")

#     if tabpanel1:
#         # Extract and display route options
#         route_options = tabpanel1.find('table', class_='table').find_all('tr')
#         print("\nRoute Options:")
#         for option in route_options:
#             print(option.text.strip())

#         # Extract and display information
#         print(f"\n{source_station.capitalize()} to {destination_station.capitalize()} Information:")
#         info_tables = tabpanel1.find_all('table', class_='table')
#         if len(info_tables) >= 2:
#             info_table = info_tables[1]  # Second table contains the information
#             info_rows = info_table.find_all('tr')
#             for row in info_rows:
#                 cells = row.find_all('td')
#                 if len(cells) == 2:  # Ensure it's a data row
#                     for cell in cells:
#                         print(cell.text.strip())
#     else:
#         print("Error: Element with id 'tabpanel1' not found.")
# else:
#     print("Invalid station name or city name.")



import requests
from bs4 import BeautifulSoup
import json

# Load station names from JSON file
with open("stations.json") as f:
    station_data = json.load(f)
    stations = station_data["stations"]

# Display available stations
# print("Available stations:")
for i, station in enumerate(stations, 1):
    print(f"{i}. {station}")

# Prompt user to select source and destination stations by name
source_station_input = input("Enter the name of the source station: ")
destination_station_input = input("Enter the name of the destination station: ")

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
    print(url)
    # Send GET request to URL
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find element with id "tabpanel1"
    tabpanel1 = soup.find(id="tabpanel1")

    if tabpanel1:
        # Extract and display route options
        route_options = tabpanel1.find('table', class_='table').find_all('tr')
        print("\nRoute Options:")
        for option in route_options:
            print(option.text.strip())

        # Extract and display information
        print(f"\n{source_station_input.capitalize()} to {destination_station_input.capitalize()} Information:")
        info_tables = tabpanel1.find_all('table', class_='table')
        if len(info_tables) >= 2:
            info_table = info_tables[1]  # Second table contains the information
            info_rows = info_table.find_all('tr')
            for row in info_rows:
                cells = row.find_all('td')
                if len(cells) == 2:  # Ensure it's a data row
                    for cell in cells:
                        print(cell.text.strip())
    else:
        print("Error: Element with id 'tabpanel1' not found.")
else:
    print("Invalid station name or city name.")




















































































# import requests
# from bs4 import BeautifulSoup

# # Get user inputs for source and destination stations
# sr = input("Enter the source station: ")
# dest = input("Enter the destination station: ")

# # Format the URL with user inputs
# url = f"https://yometro.com/from-{sr}-metro-station-delhi-to-{dest}-metro-station-delhi"

# # Send a GET request to the URL
# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# # Find the element with id "tabpanel1"
# tabpanel1 = soup.find(id="tabpanel1")

# # Check if tabpanel1 is not None before proceeding
# if tabpanel1:
#     # Extract and display the route options
#     route_options_table = tabpanel1.find('table', class_='table')
#     if route_options_table:
#         route_options = route_options_table.find_all('tr')
#         for option in route_options:
#             print(option.text.strip())

#     # Extract and display Kashmere Gate to Rajiv Chowk information
#     print("\nKashmere Gate to Rajiv Chowk information:")
#     info_tables = tabpanel1.find_all('table', class_='table')
#     if len(info_tables) >= 2:
#         info_table = info_tables[1]  # Second table contains the information
#         info_rows = info_table.find_all('tr')
#         for row in info_rows:
#             cells = row.find_all('td')
#             if len(cells) == 2:  # Ensure it's a data row
#                 for cell in cells:
#                     print(cell.text.strip())
# else:
#     print("Error: Element with id 'tabpanel1' not found.")






########################################## correct code ########################################################################




# # Extracting table 1 and table 3 data
# tables = soup.find_all('table')
# table1_data = tables[1].find_all('td')
# table3_data = tables[3].find_all('td')

# # Function to process and format text
# def process_text(text):
#     # Remove "Phone 8800793107" and replace 'DMRC Rs.' with 'Rs.'
#     text = text.replace("DMRC Rs.", "Rs.")
#     text = text.split("Phone 8800793107")[0]
#     # Insert spaces between letters and digits
#     text = ''.join([' ' + char if char.isdigit() and text[index - 1].isalpha() else char for index, char in enumerate(text)]).strip()
#     return text.strip()

# # Extracting text from table cells and processing
# table1_text = [process_text(td.text.strip()) for td in table1_data]
# #table3_text = [process_text(td.text.strip()) for td in table3_data]

# # Indices of values you want to print
# indices_to_print = [0, 2, 4, 6, 8]

# # Print values at the specified indices for table 1
# for index in indices_to_print:
#     print(table1_text[index])

# # Print values at the specified indices for table 3
# print("\nTable 3:")
# for index in indices_to_print:
#     print(table3_text[index])

############################## table for routes ###########################################
# div_canvas = soup.find(id="divCanvas")

# # Print the content of the element
# if div_canvas:
#     print(div_canvas.text.strip())
# else:
#     print("Element with id='divCanvas' not found.")




#td = [title.text.strip() for title in table_data]
# #print(td)

# # Indices of values you want to print
#indices_to_print = [0, 2, 4, 6, 8]

# # Print values at the specified indices
# for index in indices_to_print:
#     print(td[index])
































# table_data = a.find_all('td')[3]
# print(table_data)
# table_data = a.find_all('td')[5]
# print(table_data)
# table_data = a.find_all('td')[7]
# print(table_data)
# table_data = a.find_all('td')[9]
# print(table_data)

#b = soup.find_all('table')[3]
#print(b)

#<table class="table"><tbody><tr><td title="Monday To Saturday">Fare</td><td><div> DMRC Rs. 20</div></td></tr><tr><td>Time</td><td>0:09</td></tr><tr><td>First</td><td>5:07</td></tr><tr><td>Last</td><td>0:00</td></tr><tr><td>Phone </td><td><a href="tel:8800793107">8800793107</a></td></tr></tbody></table>




# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find the table containing the data
#     table = soup.find('table', class_='table')
    

#     if table:
#         # Extract data from the table
#         data = {}
        
#         for row in table.find_all('tr'):
#             label_cell = row.find('td', class_='label')
#             value_cell = row.find('td', class_='value')
#             if label_cell and value_cell:
#                 key = label_cell.text.strip()
#                 value = value_cell.text.strip()
#                 data[key] = value
                

#         # Print the extracted data
#         for key, value in data.items():
#             print(key + ":", value)
#     else:
#         print("Table with class 'table' not found on the webpage.")
        
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)
