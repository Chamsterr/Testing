from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class CoinMarketCapPage:
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.driver

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

        coin_elements = self.driver.find_elements(
            By.CSS_SELECTOR, 'p.coin-name')

        for coin in coin_elements:
            if env_vars["coin_name"] in coin.text:
                break
        else:
            raise Exception("Не пошло")


    def _take_screenshot(self, save_as: str):
        self.driver.save_screenshot(save_as)