from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


URL = "https://www.ebay.com/globaldeals/tech"
driver.get(URL)


WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'dne-itemtile')]"))
)


scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


products = driver.find_elements(By.XPATH, "//div[contains(@class,'dne-itemtile')]")

data = []
for product in products:
    try:
        title = product.find_element(By.XPATH, ".//span[contains(@class,'ebayui-ellipsis')]").text.strip()
    except:
        title = "N/A"

    try:
        price = product.find_element(By.XPATH, ".//span[contains(@class,'first')]").text.strip()
    except:
        price = "N/A"

    try:
        original_price = product.find_element(By.XPATH, ".//span[contains(@class,'itemtile-price-strikethrough')]").text.strip()
    except:
        original_price = "N/A"

    try:
        shipping = product.find_element(By.XPATH, ".//span[contains(@class,'dne-itemtile-delivery')]").text.strip()
    except:
        shipping = "N/A"

    try:
        item_url = product.find_element(By.XPATH, ".//a").get_attribute("href")
    except:
        item_url = "N/A"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.append({
        "timestamp": timestamp,
        "title": title,
        "price": price,
        "original_price": original_price,
        "shipping": shipping,
        "item_url": item_url
    })
print("Products found:", len(products))
for product in products[:5]:  # check first 5 only
    try:
        title = product.find_element(By.XPATH, ".//h3").text
        print("✅ Title:", title[:60])
    except:
        print("❌ Title missing")

    try:
        price = product.find_element(By.XPATH, ".//*[contains(@class,'first')]").text
        print("✅ Price:", price)
    except:
        print("❌ Price missing")


df = pd.DataFrame(data)
file_name = "ebay_tech_deals.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode='a', index=False, header=False)
else:
    df.to_csv(file_name, index=False)

print(f"[Scraped {len(df)} products successfully!]")
print(f"Data saved to {file_name}")

driver.quit()
