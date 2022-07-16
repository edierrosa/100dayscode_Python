from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re

# Set service and webdriver for chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Get cookie game page
cookie_game_url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_game_url)


# Select elements
cookie = driver.find_element(By.ID, "cookie")
cps = driver.find_element(By.ID, "cps")


def get_available_items():
    """Available items to buy"""
    return [item for item in driver.find_elements(By.CSS_SELECTOR, "#store div") if item.get_attribute("class") != "grayed"]


def buy_expensive_item(items):
    """Buy expensive item"""
    items[-1].click()


# Triggers
time_to_buy = time.time() + 5
timeout = time.time() + 300


# Play
while True:
    cookie.click()
    # Every 5 seconds
    if time.time() > time_to_buy:
        buy_expensive_item(get_available_items())
        time_to_buy = time.time() + 5
    # Break the loop
    if time.time() > timeout:
        print(cps.text)
        break


driver.quit()
