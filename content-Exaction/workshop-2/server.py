import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'http://quotes.toscrape.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup and the default HTML parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the quotes
    quotes = soup.find_all('span', class_='text')

    # Open a file for writing (change 'quotes.txt' to your desired filename)
    with open('quotes.txt', 'w', encoding='utf-8') as file:
        for quote in quotes:
            file.write(quote.get_text() + '\n')

    print("Scraped data has been written to 'quotes.txt'")

else:
    print(f"Failed to fetch the web page. Status Code: {response.status_code}")
