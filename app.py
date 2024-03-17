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
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://delhimetrorail.info/kashmere-gate-delhi-metro-station-to-laxmi-nagar-delhi-metro-station"

# Send a GET request to the URL
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# Extracting table 1 and table 3 data
tables = soup.find_all('table')
table1_data = tables[1].find_all('td')
table3_data = tables[3].find_all('td')

# Function to process and format text
def process_text(text):
    # Remove "Phone 8800793107" and replace 'DMRC Rs.' with 'Rs.'
    text = text.replace("DMRC Rs.", "Rs.")
    text = text.split("Phone 8800793107")[0]
    # Insert spaces between letters and digits
    text = ''.join([' ' + char if char.isdigit() and text[index - 1].isalpha() else char for index, char in enumerate(text)]).strip()
    return text.strip()

# Extracting text from table cells and processing
table1_text = [process_text(td.text.strip()) for td in table1_data]
#table3_text = [process_text(td.text.strip()) for td in table3_data]

# Indices of values you want to print
indices_to_print = [0, 2, 4, 6, 8]

# Print values at the specified indices for table 1
for index in indices_to_print:
    print(table1_text[index])

# # Print values at the specified indices for table 3
# print("\nTable 3:")
# for index in indices_to_print:
#     print(table3_text[index])

############################## table for routes ###########################################
div_canvas = soup.find(id="divCanvas")

# Print the content of the element
if div_canvas:
    print(div_canvas.text.strip())
else:
    print("Element with id='divCanvas' not found.")




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
