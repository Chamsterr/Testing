import pytest
import json
import os
from pydantic import BaseModel
from page.CurrencyPage import CurrencyPage
from driver.DriverSingletone import DriverSingleton
from model.Coin import Coin

class TestCurrencyPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSingleton.getInstance()
        self.page = CurrencyPage(self.driver)
        yield

    def test_download_chart(self):
        self.page.download_chart()
        
    def test_toggle_favorite_coin(self):
        before = self.page.get_favorite_coin_state()
        self.page.toggle_favorite_coin()
        if before == self.page.get_favorite_coin_state():
            raise Exception("Не пошло")

    def test_find_stats(self):
        assert self.page.find_stats(), "Не пошло"
