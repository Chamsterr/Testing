from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_by_url(self, url: str):
        self.driver.get(url)
        time.sleep(5000)

if __name__ == "__main__":
    browser = Browser()
    browser.open_by_url('https://coinmarketcap.com/')