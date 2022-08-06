import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import dotenv
from pathlib import Path

# Environment Variables
dotenv_path = Path(
    "path to dotenv")
dotenv.load_dotenv(dotenv_path=dotenv_path)
tw_url = os.environ["TW_URL"]
tw_email = os.environ["TW_EMAIL"]
tw_user = os.environ["TW_USER"]
tw_password = os.environ["TW_PASSWORD"]
st_url = os.environ["ST_URL"]


# Set service and options for Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)


class TwitterBot:
    """Create bot"""

    def __init__(self, service=service, options=chrome_options):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.down = 0
        self.up = 0

    def get_internet_speed(self, url=st_url, wait=60):
        """Check internet speed"""
        self.driver.get(url=url)
        go = self.driver.find_element(By.XPATH, '//*[text()="Go"]')
        self.driver.execute_script("arguments[0].click();", go)

        time.sleep(wait)

        self.down = float(self.driver.find_element(
            By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(
            By.CLASS_NAME, "upload-speed").text)

    def post_tweet(self):
        """Post message on Twitter"""
        tweet = f"Internet speed check today: {self.down}-Download/{self.up}-Upload"
        self.driver.get(tw_url)
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//span[text()="Sign in"]'))).click()
        email = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//input[@autocomplete="username"]')))
        email.send_keys(tw_email, Keys.ENTER)
        user = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//input[@data-testid="ocfEnterTextTextInput"]')))
        user.send_keys(tw_user, Keys.ENTER)
        password = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//input[@autocomplete="current-password"]')))
        password.send_keys(tw_password, Keys.ENTER)
        post = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@data-text="true"]')))
        post.send_keys(tweet)
        self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//span[text()="Tweet"]'))).click()
        self.driver.quit()


bot = TwitterBot()
bot.get_internet_speed()
bot.post_tweet()


# print(self.driver.find_element(
#     By.CSS_SELECTOR, 'div.gauge-wrapper').value_of_css_property("visibility"))
