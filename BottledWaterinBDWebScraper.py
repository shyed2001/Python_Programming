''' import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://bbs.gov.bd/bottled-water-bangladesh"


# Send a GET request to the website and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the relevant information from the HTML page
bottled_water_items = soup.find_all("div", class_="bottled-water-item")
for item in bottled_water_items:
    name = item.find("div", class_="name").text
    price = item.find("div", class_="price").text
    availability = item.find("div", class_="availability").text
    # print_bottled_water_info(url)
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
 '''
 
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.dwasa.org.bd"

# Send a GET request to the website and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Search for the specified phrase in the HTML content
if "Bangladesh" in soup.text:
    print("The phrase was found on the website!")
else:
    print("The phrase was not found on the website.")