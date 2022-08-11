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
insta_url = os.environ["INSTA_URL"]
insta_email = os.environ["INSTA_EMAIL"]
insta_password = os.environ["INSTA_PASSWORD"]


# Set service and options for Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)


class InstaBot:
    """Create bot"""

    def __init__(self, service=service, options=chrome_options):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.followers = []
        self.following = []

    def login(self):
        """Log in to Instagram """
        self.driver.get(insta_url)
        email = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//input[@aria-label="Phone number, username or email address"]')))
        email.send_keys(insta_email, Keys.TAB, insta_password, Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//button[text()="Not now"]'))).click()
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//button[text()="Not Now"]'))).click()

    def find_followers(self, account):
        """Get all followers of a given account"""
        self.driver.get(f"{insta_url}{account}/")
        followers = self.wait.until(EC.presence_of_element_located((
            By.XPATH, f'//a[@href="/{account}/followers/"]/div/span[@class="_ac2a"]')))
        number_of_followers = int(
            (followers.get_attribute("title")).replace(",", ""))
        print(f"followers: {number_of_followers}")
        followers.click()

        while len(self.followers) < number_of_followers:
            time.sleep(3)
            try:
                div = self.wait.until(EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div')))
                followers_accounts = div.find_elements(By.TAG_NAME, "a")
                for _ in followers_accounts:
                    if _.get_attribute('href') not in self.followers:
                        self.followers.append(_.get_attribute('href'))
                    scroll = self.wait.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR, "div._aano")))
                    self.driver.execute_script(
                        "arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            except:
                break

    def find_following(self, account):
        """Get all followings of a given account"""
        self.driver.get(f"{insta_url}{account}/")
        following = self.wait.until(EC.presence_of_element_located((
            By.XPATH, f'//a[@href="/{account}/following/"]/div/span[@class="_ac2a"]')))
        number_of_followings = int((
            following.text).replace(",", ""))
        print(f"following: {number_of_followings}")
        following.click()

        while len(self.following) < number_of_followings:
            time.sleep(3)
            try:
                div = self.wait.until(EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/div')))
                following_accounts = div.find_elements(By.TAG_NAME, "a")
                for _ in following_accounts:
                    if _.get_attribute('href') not in self.following:
                        self.following.append(_.get_attribute('href'))
                    scroll = self.wait.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR, "div._aano")))
                    self.driver.execute_script(
                        "arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            except:
                break

    def not_follow_back(self):
        """Get the accounts that do not follow back"""
        not_following_you = [
            item for item in self.following if item not in self.followers]
        print(not_following_you)


bot = InstaBot()
bot.login()
bot.find_followers("some account")
bot.find_following("some account")
bot.not_follow_back()
bot.driver.quit()
