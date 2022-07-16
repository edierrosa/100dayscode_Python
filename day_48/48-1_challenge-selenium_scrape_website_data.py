
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# You can hard code driver location
# chrome_driver_path = "/Users/Agilulfo/Coding/chromedriver_win32/chromedriver.exe"
# service = ChromeService(executable_path=chrome_driver_path)

# product_url = "https://www.amazon.com/Bedtime-Originals-Twinkle-Elephant-Plush/dp/B0771V1JZX/?_encoding=UTF8&pd_rd_w=x0jk1&content-id=amzn1.sym.0a0fec03-b408-45eb-8e57-18d0d31850f9&pf_rd_p=0a0fec03-b408-45eb-8e57-18d0d31850f9&pf_rd_r=D7988WQD4NYSPTCE69AM&pd_rd_wg=68kFF&pd_rd_r=bfe74ffc-d49b-4561-b2dc-623662076fa4&ref_=pd_gw_unk"

# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get(product_url)
# product_name = driver.find_element(by=By.ID, value="productTitle")
# print(product_name.text)

# driver.quit()


python_url = "https://www.python.org/"

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(python_url)

events_ul = driver.find_elements(
    by=By.CSS_SELECTOR, value=".event-widget ul li")

events = {idx: {
    "time": item.find_element(by=By.TAG_NAME, value="time").text,
    "name": item.find_element(by=By.TAG_NAME, value="a").text
} for idx, item in enumerate(events_ul)}


print(events)

driver.quit()
