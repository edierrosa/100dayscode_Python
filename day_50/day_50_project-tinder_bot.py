import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
import dotenv
from pathlib import Path


# Environment Variables
dotenv_path = Path(
    "path to dotenv")
dotenv.load_dotenv(dotenv_path=dotenv_path)
fb_user = os.environ["FB_USER"]
fb_password = os.environ["FB_PASSWORD"]


# Set service and webdriver for chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)


# Tinder url
tinder_url = "https://tinder.com/"
driver.get(tinder_url)
main_window = driver.current_window_handle
# driver.maximize_window()

# Login with Facebook
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[text()="Log in"]'))).click()
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//span[text()="Login with Facebook"]'))).click()

driver.switch_to.window(driver.window_handles[1])


# Facebook credentials
credentials = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'input#email')))
credentials.send_keys(fb_user, Keys.TAB, fb_password, Keys.ENTER)

driver.switch_to.window(main_window)


# Allow browser location
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//span[text()="Allow"]'))).click()
# Not interested
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//span[text()="Not interested"]'))).click()
# Accept cookies
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//span[text()="I accept"]'))).click()


# Like as much as you can
n = 0
while True:
    n += 1
    time.sleep(2)
    try:
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.Bgc\(\$c-like-green\)\:a"))).click()
        print(f"Like {n}")
    except ElementClickInterceptedException:
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@title="Back to Tinder"]'))).click()
            print("It's a match")
        except TimeoutException:
            try:
                time.sleep(2)
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//span[text()="Not interested"]'))).click()
                print("Not interested. Stop offering stuff! I want a match!")
            except:
                wait.until(EC.presence_of_element_located((
                    By.XPATH, '//span[text()="No Thanks"]'))).click()
                print("No more likes today")
                break
        except NoSuchElementException:
            time.sleep(2)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
