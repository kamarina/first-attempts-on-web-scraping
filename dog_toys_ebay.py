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

def scrape_ebay_dog_toys(min_budget, max_budget):
    # Define the URL to scrape
    url_first = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=dog+toys&_sacat=0"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    r = requests.get(url_first, headers=headers)

    if r.status_code == 200:
        # Create a BeautifulSoup object for parsing HTML content
        soup = BeautifulSoup(r.text, "html.parser")

        # Find and extract relevant information from the HTML
        items = soup.findAll("div", attrs={"class": "s-item__title"})
        prices = soup.findAll("span", attrs={"class": "s-item__price"})
        postage_cost = soup.findAll("span", attrs={"class": "s-item__shipping s-item__logisticsCost"})

        # Prepare a list to store the selected items within the budget
        selected_items = []

        # Iterate over the items and filter based on the budget
        for index, (item, price, postage) in enumerate(zip(items, prices, postage_cost), start=1):
            price_value = extract_numeric_part(price.text.strip())
            postage_value = extract_numeric_part(postage.text.strip())
            total_per_item = price_value + postage_value

            # Check if the total price is within the user's budget range
            if min_budget <= total_per_item <= max_budget:
                selected_items.append({
                    "item_name": item.text.strip(),
                    "postage": postage.text.strip(),
                    "price": price.text.strip(),
                    "total_per_item": total_per_item
                })

        return selected_items

# Get user input for budget range
min_budget = float(input("Enter the minimum budget: £"))
max_budget = float(input("Enter the maximum budget: £"))

# Call the function to scrape and filter dog toys within the budget
result = scrape_ebay_dog_toys(min_budget, max_budget)

# Print the results
if result:
    print("\nDog Toys within the budget:")
    for index, item in enumerate(result, start=1):
        print(f"\n<Item {index}>: {item['item_name']}\nPostage: {item['postage']},\nPrice: {item['price']} ("
              f"Total with postage: £{item['total_per_item']:.2f})")
else:
    print("\nNo dog toys found within the specified budget range.")
