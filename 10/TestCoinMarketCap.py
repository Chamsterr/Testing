import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import sys
from CoinMarketCapPage import CoinMarketCapPage
from CurrencyPage import CurrencyPage
from Browser import Browser

class TestCoinMarketCap(unittest.TestCase):

    def test_search(self):
        self.browser = Browser()
        self.currencyPage = CoinMarketCapPage(self.browser)

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
                found_coin = True
                break

        self.assertTrue(found_coin, "Не пошло")

    def test_get_stats(self):
        self.browser = Browser()
        self.currencyPage = CurrencyPage(self.browser)
        stats = self.currencyPage.find_stats()
        self.assertTrue(len(stats), 3)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
