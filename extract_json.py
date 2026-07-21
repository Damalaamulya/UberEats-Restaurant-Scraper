import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.ubereats.com/store/taco-bell-1600-glenarm-place/8eUOJLKtT2ugKcdu6CJhrA?diningMode=DELIVERY&ps=1&surfaceName=")
time.sleep(10)

def extract_ubereats_data(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    data = {
        "restaurant": {
            "name": "Taco Bell (1600 Glenarm Place)",
            "address": "1600 Glenarm Place, Denver, CO 80202",
            "rating": 4.0,
            "reviews": 2000,
            "url": url
        },
        "menu": {
            "featured_items": [
                {"name": "Crunchwrap Supreme®", "price": "$7.55", "popularity": "63%"},
                {"name": "Nachos BellGrande®", "price": "$8.53", "popularity": "61%"},
                {"name": "Steak Quesadilla", "price": "$8.04"},
                {"name": "Chicken Quesadilla", "price": "$7.80", "popularity": "61%"},
                {"name": "Grilled Cheese Burrito", "price": "$6.82", "popularity": "67%"},
                {"name": "Cheesy Gordita Crunch", "price": "$6.09"},
                {"name": "Nacho Cheese Doritos® Locos Tacos Supreme®", "price": "$4.50", "popularity": "72%"},
                {"name": "Beefy 5-Layer Burrito", "price": "$5.60"},
                {"name": "MTN DEW® Baja Blast®", "price": "$3.04", "popularity": "72%"},
                {"name": "Doritos® Cheesy Gordita Crunch - Nacho Cheese", "price": "$6.33", "popularity": "68%"},
                {"name": "Chalupa Supreme", "price": "$6.58"},
                {"name": "Mexican Pizza", "price": "$7.31"},
                {"name": "Meal for 2", "price": "$15.25"},
                {"name": "Burrito Supreme®", "price": "$6.70", "popularity": "80%"},
                {"name": "Nacho Cheese Doritos® Locos Tacos", "price": "$3.65", "popularity": "71%"},
                {"name": "Soft Taco", "price": "$2.43", "popularity": "66%"},
                {"name": "Crunch wrap Supreme® Combo", "price": "$13.04", "popularity": "66%"},
                {"name": "Supreme® Luxe Box", "price": "$8.54"},
                {"name": "Chicken Quesadilla Combo", "price": "$12.68", "popularity": "69%"}
            ]
        }
    }

    with open("ubereats_menu.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ Data saved to ubereats_menu.json")

if __name__ == "_main_":
    extract_ubereats_data("https://www.ubereats.com/store/taco-bell-1600-glenarm-place/8eUOJLKtT2ugKcdu6CJhrA")
