import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://edition.cnn.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup and the default HTML parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the newsHeadlines
    newsHeadlines = soup.find_all('div', class_='container__headline')
    # Open a file for writing (change 'newsHeadlines.txt' to your desired filename)
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for newsHeadline in newsHeadlines:
            file.write(newsHeadline.get_text() + '\n')

    print("Scraped data has been written to 'newsHeadlines.txt'")

else:
    print(f"Failed to fetch the web page. Status Code: {response.status_code}")
