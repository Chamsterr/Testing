from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def go_to(self, url: str):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()