from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Set service and webdriver for chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Get wikipedia article counter
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wikipedia_url)

# wiki_article_counter = driver.find_element(
#     by=By.CSS_SELECTOR, value="#articlecount a")

# wiki_article_counter.click()

free = driver.find_element(by=By.LINK_TEXT, value="free")
free.click()

driver.quit()
