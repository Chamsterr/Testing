from selenium import webdriver
from selenium.webdriver.common.by import By
from  driver.DriverSingletone import DriverSingleton
import time
import os

class CoinMarketCapPage:
    def __init__(self, driver):
        self.driver = driver

    def use_search(self, coin_name):
        self.driver.get("https://coinmarketcap.com/")
        env_vars = os.environ
        div_with_input = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]")
        div_with_input.click()
        time.sleep(1)

        search = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/div/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div[1]/input")
        search.send_keys(coin_name)

        time.sleep(5)

        try:
            result = self.driver.find_element(
                By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[1]")
        except:
            raise Exception("Не пошло")
        return True

if __name__ == "__main__":
    coinMarketCapPage = CoinMarketCapPage(DriverSingleton.getInstance())
    print(coinMarketCapPage.use_search("234567890"))