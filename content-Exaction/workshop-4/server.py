import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website you want to scrape
url = 'http://quotes.toscrape.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup and the default HTML parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the quotes and authors
    quotes = []
    quote_elements = soup.find_all('span', class_='text')
    author_elements = soup.find_all('small', class_='author')
    for quote, author in zip(quote_elements, author_elements):
        quotes.append((quote.get_text(), author.get_text()))

    # Save the scraped data to a CSV file
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Quote', 'Author'])
        csvwriter.writerows(quotes)

    print("Scraped data has been saved to 'quotes.csv'")

else:
    print(f"Failed to fetch the web page. Status Code: {response.status_code}")
