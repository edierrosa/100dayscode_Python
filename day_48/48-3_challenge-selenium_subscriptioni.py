from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# Set service and webdriver for chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Subscribe to test page
test_page = "https://secure-retreat-92358.herokuapp.com/"

driver.get(test_page)
first = driver.find_element(By.NAME, "fName")
first.send_keys("Dummy")
last = driver.find_element(By.NAME, "lName")
last.send_keys("Quixote")
email = driver.find_element(By.NAME, "email")
email.send_keys("dummy@dummy.com")
sign_in = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
sign_in.click()

driver.quit()
