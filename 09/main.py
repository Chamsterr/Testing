from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
import os

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_by_url(self, url: str):
        self.driver.get(url)

    def use_search(self):
        env_vars = os.environ
        div_with_input = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]")
        div_with_input.click()
        time.sleep(1)

        search = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/div/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div[1]/input")
        search.send_keys(env_vars["coin_name"])

        time.sleep(3)
        self._take_screenshot('screenshots/screenshot.png')

        coin_elements = self.driver.find_elements(
            By.CSS_SELECTOR, 'p.coin-name')

        for coin in coin_elements:
            if env_vars["coin_name"] in coin.text:
                break
        else:
            raise Exception("Не пошло")

    def _take_screenshot(self, save_as: str):
        self.driver.save_screenshot(save_as)

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
    time.sleep(1)
    browser.use_search()
