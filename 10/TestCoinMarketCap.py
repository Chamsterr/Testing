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
        self.browser.go_to("https://coinmarketcap.com/")
        self.coinMarketCapPage = CoinMarketCapPage(self.browser)
        found = self.coinMarketCapPage.use_search()

        self.assertTrue(found, "Не пошло")
        self.browser.quit()

    def test_get_stats(self):
        self.browser = Browser()
        self.currencyPage = CurrencyPage(self.browser)
        stats = self.currencyPage.find_stats()
        self.assertTrue(len(stats), 3)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
