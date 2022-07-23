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
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)
linkedin_user = os.environ["LINKEDIN_USER"]
linkedin_password = os.environ["LINKEDIN_PASSWORD"]
linkedin_mobile_number = os.environ["LINKEDIN_MOBILE_NUMBER"]


# Set service and webdriver for chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)


# Linkedin url and headers
linkedin_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=100961908&keywords=python%20developer&location=Malta"


# Get LinkedIn url
driver.get(linkedin_url)


# Go to LinkedIn sign in page and sign in
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))).click()

signin_linkedin = wait.until(
    EC.presence_of_element_located((By.ID, "username")))
signin_linkedin.send_keys(
    linkedin_user, Keys.TAB,
    linkedin_password, Keys.ENTER)


# Create a list of job objects
job_list = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container--clickable")))


def follow_company(job):
    """Follow company"""
    role = job.find_element(
        By.CLASS_NAME, "job-card-list__title").text
    company = job.find_element(
        By.CLASS_NAME, "job-card-container__company-name").text
    try:
        job.click()
        follow = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "button.follow")))
        # driver.execute_script("arguments[0].scrollIntoView();", follow)
        if follow:
            follow.click()
            print(f'Role: {role}\nCompany: {company}\nFollowed')
    except Exception:
        print(f"Not able to follow {company}")


for job in job_list:
    follow_company(job)

driver.quit()
