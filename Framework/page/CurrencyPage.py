from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.DriverSingletone import DriverSingleton
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time

def hover_and_sleep(driver, button):
    webdriver.ActionChains(driver).move_to_element(button).perform()
    time.sleep(3)

def click_element(driver, xpath):
    element_to_click = driver.find_element(By.XPATH, xpath)
    element_to_click.click()


class CurrencyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_stats(self):
        self.driver.get("https://coinmarketcap.com/currencies/bitcoin/")
        price = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span')))
        market_cup = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[1]/div[1]/dd')))
        volue = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd')))

        return price, market_cup, volue

    def toggle_favorite_coin(self):
        self.driver.get("https://coinmarketcap.com/currencies/bitcoin/")
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="section-coin-overview"]/div[1]/button[1]')))
        button.click()

    def get_favorite_coin_state(self):
        self.driver.get("https://coinmarketcap.com/currencies/bitcoin/")
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[1]/button[1]')))
        favorite_coin_stage = button.find_element(By.TAG_NAME, 'use')
        return favorite_coin_stage.get_attribute('href')
    
    def download_chart(self):
        self.driver.get("https://coinmarketcap.com/currencies/bitcoin/")
        time.sleep(1)
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,  '//*[@id="react-tabs-46"]/div/div[2]')))
        
        t1 = threading.Thread(target=hover_and_sleep, args=(self.driver, button))
        time.sleep(3)
        t2 = threading.Thread(target=click_element, args=(self.driver, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[4]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/ul/li[8]/div[2]/div/div[1]/div/div/button[2]/div'))

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    driverSingletone = DriverSingleton()
    currencyPage = CurrencyPage(driverSingletone.driver)
    # currencyPage.find_stats()
    currencyPage.download_chart()
    # currencyPage.toggle_favorite_coin()
    # print(currencyPage.get_favorite_coin_state())