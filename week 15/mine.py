# Import libraries
###EXPLINATION AT BOTTOM###
from bs4 import BeautifulSoup
import requests
import csv
 
# Set the URL to scrape
url = "https://weather.com/weather/tenday/l/USNY0996:1:US"
 
# Send a GET request to the URL and store the response
response = requests.get(url)
 
# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
 
# Find the forecast container element
temps = soup.find_all(class_="DailyContent--temp--1s3a7")
days = soup.find_all(class_="DetailsSummary--daypartName--kbngc")
print(f'{days[0].text}, {temps[0].text}')
print(f'{days[1].text}, {temps[2].text}')
print(f'{days[2].text}, {temps[4].text}')
print(f'{days[3].text}, {temps[6].text}')
print(f'{days[4].text}, {temps[8].text}')
print(f'{days[5].text}, {temps[10].text}')
print(f'{days[6].text}, {temps[12].text}')
print(f'{days[7].text}, {temps[14].text}')
print(f'{days[8].text}, {temps[16].text}')
print(f'{days[9].text}, {temps[18].text}')

# Create an empty list to store the forecast data
forecast_data = []
 
# # Loop through each row in the forecast table
# for row in today.find_all("tr"):
#   # Create an empty dictionary to store the forecast data for each day
#   day_data = {}
 
#   # Loop through each cell in the row
#   for cell in row.find_all("td"):
#     # Get the forecast date and store it in the dictionary
#     if cell.get("headers")[0] == "date":
#       day_data["date"] = cell.text
 
#     # Get the forecast description and store it in the dictionary
#     if cell.get("headers")[0] == "description":
#       day_data["description"] = cell.text
 
#     # Get the forecast high and low temperatures and store them in the dictionary
#     if cell.get("headers")[0] == "hi-lo":
#       temperatures = cell.text.split("/")
#       day_data["high"] = temperatures[0]
#       day_data["low"] = temperatures[1]
 
  # Add the day's forecast data to the list
 
# Open a new file to write the forecast data to
with open("forecast.csv", "w") as csv_file:
  # Create a CSV writer
  writer = csv.DictWriter(csv_file, fieldnames=[f'''{days[0].text, temps[0].text[:2],}\n,{days[1].text, temps[2].text[:2],}\n,{days[2].text, temps[4].text[:2],}\n,{days[3].text, temps[6].text[:2],}\n,{days[4].text, temps[8].text[:2],}\n,{days[5].text, temps[10].text[:2],}\n,{days[6].text, temps[12].text[:2],}\n,{days[7].text, temps[14].text[:2],}\n,{days[8].text, temps[16].text[:2],}\n,{days[9].text, temps[18].text[:2]}'''])
 
  # Write the column headers
  writer.writeheader()
 
  # Write the forecast data to the file
  for day in forecast_data:
    writer.writerow(day)

### I know I was supposed to consistantly update my github but I decided not to since I was testing things.
### Most of the code that the ai gave us was wrong, it gave tables and classes that dont exist, I think.
### I just remade a basic weather scraper with 10 days; gives out the day, and the tempature.
### The output doesn't look pretty in the csv file since I made it quick, but it gets the job done.
### The only code I used from the ai was url, parser, etc. And I used some of the code at the bottom to use the csv file.
### Other than that I think it would be eaiser to just make it from scratch in the beginning, rather than trying to fix broken code.
