from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver.DriverSingletone import DriverSingleton
from selenium.webdriver.common.keys import Keys
import time


class PortfolioTrackerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_create_popup(self):
        self.driver.get("https://coinmarketcap.com/portfolio-tracker/")
        open_portfolio_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,  '/html/body/div[1]/div[2]/div/div[2]/div/div/aside/div/div/div/div/div/div[3]/div[3]/div')))
        open_portfolio_button.click()

        add_transactions_manually_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  '/html/body/div[8]/div/div[2]/div[2]/div[2]/div/div[1]')))
        add_transactions_manually_button.click()

    def create_button(self):
        create_portfolio_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  '/html/body/div[9]/div/div[2]/button')))
        create_portfolio_button.click()

    def insert_portfolio_name(self, portfolio_name):
        portfolio_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  '/html/body/div[9]/div/div[2]/input')))
        portfolio_name_input.send_keys(portfolio_name)

    def get_insert_portfolio_name(self):
        portfolio_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  '/html/body/div[9]/div/div[2]/input')))
        return portfolio_name_input.get_attribute("value")

    def get_portfolio_number(self):
        self.driver.get("https://coinmarketcap.com/portfolio-tracker/")
        my_portfolios_span = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,  '/html/body/div[1]/div[2]/div/div[2]/div/div/aside/div/div/div/div/div/div[3]/div[1]/span')))
        return my_portfolios_span.text
    
    def open_add_transaction_popup(self, coin):
        self.driver.get("https://coinmarketcap.com/portfolio-tracker/")

        # /html/body/div[1]/div[2]/div/div[2]/div/div/aside/div/div/div/div/div/div[3]/div[2]/div[1]

        first_portfolio = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/aside/div/div/div/div/div/div[3]/div[2]/div[1]')))
        first_portfolio.click()

        add_transaction_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,  '/html/body/div[1]/div[2]/div/div[2]/div/div/section/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[9]/div/button')))
        add_transaction_button.click()
        
        quantity_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,  '/html/body/div[9]/div/div[2]/div/div[1]/div/div[2]/div[1]/input')))
        
        quantity_input.send_keys(coin.quantity)

        price_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,  '/html/body/div[9]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/input')))
        price_input.send_keys(Keys.CONTROL + "a")
        price_input.send_keys(coin.price)

    def crete_transaction_button(self):
        # /html/body/div[9]/div/div[2]/div/div[1]/div/div[5]/button
        crete_transaction_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  '/html/body/div[9]/div/div[2]/div/div[1]/div/div[5]/button')))
        crete_transaction_button.click()

if __name__ == "__main__":
    portfolioTrackerPage = PortfolioTrackerPage(DriverSingleton.getInstance())

    portfolioTrackerPage.open_add_transaction_popup()
    time.sleep(50)

    # portfolioTrackerPage.open_create_popup()
    # time.sleep(5)
    # portfolioTrackerPage.create_button()
    # print(portfolioTrackerPage.get_portfolio_number())
    # time.sleep(5)
    # portfolioTrackerPage.open_create_popup()
    # portfolioTrackerPage.insert_portfolio_name(
    #     "123456789123456789123456789")
    # print(portfolioTrackerPage.get_insert_portfolio_name())
    # portfolioTrackerPage.create_button()
    # time.sleep(5)
    # print(portfolioTrackerPage.get_portfolio_number())