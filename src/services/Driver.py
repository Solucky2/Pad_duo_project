import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import os


class Driver:


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(self.sleep_time)
        self.end_session()

    def __init__(self, url, num_of_iterations, sleep_time):
        load_dotenv()
        self.options = Options()
        self.service = Service()
        self.options.add_argument('--no-headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.url = url
        self.num_of_iterations = num_of_iterations
        self.sleep_time = sleep_time
        self.username = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

    def open(self):
        self.driver.get(self.url)

    def end_session(self):
        self.driver.quit()

    def handle_pop_up(self, pop_up_locator):
        WebDriverWait(self.driver, self.sleep_time).until(
            ec.presence_of_element_located((By.ID, pop_up_locator))).click()

    def navigate_to_login(self, login_locator, login_by_email_locator):
        WebDriverWait(self.driver, self.sleep_time).until(
            ec.presence_of_element_located((By.ID, login_locator))
        ).click()
        WebDriverWait(self.driver, self.sleep_time).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, login_by_email_locator))
        ).click()

    def login(self, username_locator, password_locator):
        WebDriverWait(self.driver, self.sleep_time).until(
            ec.presence_of_element_located((By.ID, username_locator))).send_keys(self.username)
        WebDriverWait(self.driver, self.sleep_time).until(
            ec.presence_of_element_located((By.ID, password_locator))).send_keys(self.password, Keys.ENTER)

    def get_page_source(self):
        for num in range(1, self.num_of_iterations+1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.page_source
