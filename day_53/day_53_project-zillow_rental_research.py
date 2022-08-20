# I kept the course requirements. Bs4 is not the best tool to scrape in this particular case.


from time import sleep
import requests as r
from bs4 import BeautifulSoup
import os
import dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Environment variables
dotenv.load_dotenv(
    Path("path to dotenv")
)
zillow_url = os.environ["ZILLOW_URL"]
g_form_url = os.environ["G_FORM_URL"]

headers = {
    "headers"
}

# Zillow data
zillow_session = r.Session()
zillow_soup = BeautifulSoup(
    zillow_session.get(zillow_url, headers=headers).text, "html.parser"
)
zillow_properties = zillow_soup.find_all(
    name="div", class_="property-card-data"
)

zillow_data = []
for _ in zillow_properties:
    zillow_data.append({
        # "link": (_.a)["href"],
        "link": _ if "https" in (_.a)["href"] else f'https://www.zillow.com{(_.a)["href"]}',
        "address": (_.a.address).getText().split(" | ")[-1],
        "price": _.find(
            "span", {"data-test": "property-card-price"}).getText().split("+")[0]
    })

print(zillow_data)


if zillow_data:
    # Google forms
    service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get(g_form_url)

    for item in zillow_data:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div'))).click()
        address = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address.send_keys(
            item["address"],
            Keys.TAB,
            item["price"],
            Keys.TAB,
            item["link"],
            Keys.TAB,
            Keys.ENTER)
        sleep(2)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//a[text()="Send another response"]'))).click()
        sleep(2)

    driver.quit()
else:
    print("No data")
