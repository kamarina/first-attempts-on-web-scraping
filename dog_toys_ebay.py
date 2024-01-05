import requests
from bs4 import BeautifulSoup
import re


def extract_numeric_part(text):
    """
    Extracts the numeric part from the given text using regular expression.
    Parameters:
        text (str): The input text containing numeric and non-numeric parts.
    Returns:
        float: The numeric part extracted from the text, or 0.0 if no numeric part is found.
    """
    # Extract numeric part from the given text using regular expression
    match = re.search(r'[\d.]+', text)
    if match:
        return float(match.group())
    else:
        return 0.0  # Return 0.0 if no numeric part is found


# Define the URL to scrape
url_first = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=dog+toys&_sacat=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

r = requests.get(url_first, headers=headers)
print(r)

if r.status_code == 200:
    # Create a BeautifulSoup object for parsing HTML content
    soup = BeautifulSoup(r.text, "html.parser")

    # Find and extract relevant information from the HTML
    items = soup.findAll("div", attrs={"class": "s-item__title"})
    prices = soup.findAll("span", attrs={"class": "s-item__price"})
    postage_cost = soup.findAll("span", attrs={"class": "s-item__shipping s-item__logisticsCost"})

    # Iterate over the items and print the extracted information
    for index, (item, price, postage) in enumerate(zip(items, prices, postage_cost), start=1):
        price_value = extract_numeric_part(price.text.strip())
        postage_value = extract_numeric_part(postage.text.strip())

        total_per_item = price_value + postage_value

        # Print the formatted output for each item
        print(
            f"\n <Item {index}>: {item.text.strip()} \n Postage: {postage.text.strip()},\n Price: {price.text.strip()} (Total per item: £{total_per_item:.2f})")
