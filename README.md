# first-attempts-on-web-scraping
Learning web-scraping to implement in the portfolio project I am working on.

# Program 1: Web Scraping Quotes
This program demonstrates basic web scraping using the BeautifulSoup library and requests module. It scrapes quotes from the website "https://quotes.toscrape.com/" and prints them along with the respective authors.

## How to Run
1. Ensure you have the necessary libraries installed:
```python
pip install beautifulsoup4 requests
```
2. Run the script:
```python
python quotes_scraping.py
```
## Program Structure
* 'url_to_scrape': The URL of the website to scrape.
* Sends a request to the website and checks if the request was successful (status code 200).
* If successful, it creates a BeautifulSoup object to parse HTML content.
* Finds quotes and authors using descriptive variable names.
* Iterates through each quote-author pair using 'zip' and prints the formatted output.
# Program 2: eBay Dog Toys Scraper
This program scrapes dog toy listings from eBay, extracting item titles, prices, and postage costs. It utilizes regular expressions to extract numeric values and prints the information in a formatted way.
## How to Run
1. Ensure you have the necessary libraries installed:
```python
pip install beautifulsoup4 requests
```
2. Run the script:
```python
python ebay_scraper.py
```
## Program Structure
* 'url_first:' The eBay URL for dog toy listings.
* Sends a request with a user-agent header to simulate a web browser.
* If the request is successful (status code 200), it creates a BeautifulSoup object.
* Finds and extracts relevant information (items, prices, postage) from the HTML.
* Iterates over items and prints the formatted output for each item.

Both programs showcase basic web scraping techniques, demonstrating how to extract information from websites with different structures.
