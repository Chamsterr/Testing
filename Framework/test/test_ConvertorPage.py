import pytest
import json
import os
from pydantic import BaseModel
from page.ConvertorPage import ConvertorPage
from driver.DriverSingletone import DriverSingleton
from model.Coin import Coin

class TestConvertorPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverSingleton.getInstance()
        self.page = ConvertorPage(self.driver)
        yield

    @pytest.mark.parametrize("coin, should_raise", [(Coin(**coin), should_raise) for coin, should_raise in json.load(open(os.getenv('CONVERTOR')))])
    def test_convertor(self, coin, should_raise):
        try:
            self.page.use_convertor(coin.quantity)
            if coin.quantity >= 0:
                assert self.page.get_result() >= 0, "Не пошло"
            else:
                raise Exception("Не пошло")
        except Exception as e:
            if should_raise:
                assert str(e) == "Не пошло"