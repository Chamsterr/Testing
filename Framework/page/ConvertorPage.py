from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  driver.DriverSingletone import DriverSingleton
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from selenium.webdriver.common.keys import Keys

class ConvertorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def use_convertor(self, quality):
        # /html/body/div[1]/div[2]/div/div[2]/div/div/div/section[1]/div/div[1]/div[1]/input
        self.driver.get("https://coinmarketcap.com/converter/")
        quality_input = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div/section[1]/div/div[1]/div[1]/input"
        )
        quality_input.send_keys(Keys.CONTROL + "a")
        quality_input.send_keys(quality)
        time.sleep(2)
    
    def get_result(self):
        # /html/body/div[1]/div[2]/div/div[2]/div/div/div/section[1]/div/div[3]/div[3]/em
        result = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/section[1]/div/div[3]/div[3]/em')))
        return  int(result.text.replace(',', '').replace('.', ''))

if __name__ == "__main__":
    convertorPage = ConvertorPage(DriverSingleton.getInstance())
    convertorPage.use_convertor(-1231)
    print(convertorPage.get_result())
    time.sleep(2)