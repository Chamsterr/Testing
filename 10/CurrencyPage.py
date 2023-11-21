from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import sys
from Browser import Browser

class CurrencyPage:
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.driver


    def find_stats(self):
        self.browser.go_to("https://coinmarketcap.com/currencies/bitcoin/")
        price = self.driver.find_element(By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')
        market_cup = self.driver.find_element(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[1]/div[1]/dd')
        volue = self.driver.find_element(By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd')

        return price, market_cup, volue


if __name__ == "__main__":
    browser = Browser()
    currencyPage = CurrencyPage(browser)
    currencyPage.find_stats()