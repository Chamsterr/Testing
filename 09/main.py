from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_by_url(self, url: str):
        self.driver.get(url)
        self._wait_until_browser_is_closed()

    def _wait_until_browser_is_closed(self):
        try:
            while True:
                time.sleep(1)
                self.driver.title
        except WebDriverException:
            print("Browser has been closed by user")

if __name__ == "__main__":
    browser = Browser()
    browser.open_by_url('https://coinmarketcap.com/')