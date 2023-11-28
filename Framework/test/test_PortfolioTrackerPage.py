import pytest
import json
import os
import time
from pydantic import BaseModel
from page.PortfolioTrackerPage import PortfolioTrackerPage
from driver.DriverSingletone import DriverSingleton
from model.Potrfolio import Potrfolio
from model.Coin import Coin

class TestPortfolioTrackerPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSingleton.getInstance()
        self.page = PortfolioTrackerPage(self.driver)
        yield

    @pytest.mark.parametrize("coin, should_raise", [(Coin(**coin), should_raise) for coin, should_raise in json.load(open(os.getenv('TRANSACTION')))])
    def test_add_transaction(self, coin, should_raise):
        portfolio_before = self.page.get_portfolio_number()
        self.page.open_add_transaction_popup(coin)
        time.sleep(2)
        self.page.crete_transaction_button()
        time.sleep(2)

        if self.page.get_portfolio_number() != portfolio_before:
            raise Exception("Не пошло")
        
    @pytest.mark.parametrize("portfolio, should_raise", [(Potrfolio(**potrfolio), should_raise) for potrfolio, should_raise in json.load(open(os.getenv('PORTFOLIO')))])
    def test_add_potrfolio(self, portfolio, should_raise):
        try:
            portfolio_before = self.page.get_portfolio_number()
            self.page.open_create_popup()
            time.sleep(2)
            self.page.insert_portfolio_name(portfolio.name)
            time.sleep(2)
            self.page.create_button()
            time.sleep(2)

            if self.page.get_portfolio_number() == portfolio_before:
                raise Exception("Не пошло")
        except Exception as e:
            if should_raise:
                assert str(e) == "Не пошло"
            else:
                raise
