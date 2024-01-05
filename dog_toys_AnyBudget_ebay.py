import requests
from bs4 import BeautifulSoup
import re

def extract_numeric_part(text):
    match = re.search(r'[\d.]+', text)
    if match:
        return float(match.group())
    else:
        return 0.0

def get_budget_input(prompt):
    while True:
        try:
            budget = float(input(prompt))
            if budget < 0:
                raise ValueError("Budget must be a non-negative number.")
            return budget
        except ValueError:
            print("Invalid input. Please enter a valid non-negative number.")

def scrape_ebay_dog_toys(min_budget, max_budget):
    url_first = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=dog+toys&_sacat=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }
    r = requests.get(url_first, headers=headers)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.findAll("div", attrs={"class": "s-item__title"})
        prices = soup.findAll("span", attrs={"class": "s-item__price"})
        postage_cost = soup.findAll("span", attrs={"class": "s-item__shipping s-item__logisticsCost"})
        selected_items = []

        for index, (item, price, postage) in enumerate(zip(items, prices, postage_cost), start=1):
            price_value = extract_numeric_part(price.text.strip())
            postage_value = extract_numeric_part(postage.text.strip())
            total_per_item = price_value + postage_value

            if min_budget <= total_per_item <= max_budget:
                selected_items.append({
                    "item_name": item.text.strip(),
                    "postage": postage.text.strip(),
                    "price": price.text.strip(),
                    "total_per_item": total_per_item
                })

        return selected_items

# Get user input for budget range with validation
min_budget = get_budget_input("Enter the minimum budget: £")
max_budget = get_budget_input("Enter the maximum budget: £")

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
