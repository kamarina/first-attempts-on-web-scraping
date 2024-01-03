from bs4 import BeautifulSoup
import requests

# Define the URL to scrape
url_to_scrape = "https://quotes.toscrape.com/"

# Use a descriptive variable name for the response object
response = requests.get(url_to_scrape)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a BeautifulSoup object for parsing HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes using a descriptive variable name
    quotes = soup.findAll("span", attrs={"class": "text"})

    # Find all authors using a descriptive variable name
    authors = soup.findAll("small", attrs={"class": "author"})

    # Iterate through each quote-author pair using zip
    for quote, author in zip(quotes, authors):
        # Print the formatted quote and author
        print(f"{quote.text} - {author.text}")
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve the page. Status code: {response.status_code}")