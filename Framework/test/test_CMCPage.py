import pytest
import json
import os
from pydantic import BaseModel
from page.CoinMarketCapPage import CoinMarketCapPage
from driver.DriverSingletone import DriverSingleton
from model.Coin import Coin

class TestCMCPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSingleton.getInstance()
        self.page = CoinMarketCapPage(self.driver)
        yield

    @pytest.mark.parametrize("coin, should_raise", [(Coin(**coin), should_raise) for coin, should_raise in json.load(open(os.getenv('SEARCH')))])
    def test_search(self, coin, should_raise):
        try:
            found = self.page.use_search(coin.name)
            assert found, "Не пошло"
        except Exception as e:
            if should_raise:
                assert str(e) == "Не пошло"
            else:
                raise