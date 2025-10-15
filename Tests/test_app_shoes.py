import pytest
from ddt import ddt, data, unpack
import unittest
from Tests_Pages.Homepage import Homepage


@pytest.mark.usefixtures("test_setup")
@ddt
class TestAppShoes(unittest.TestCase):
    urunler = ["50's Rockabilly Polka Dot Top JR Plus Size", "Blue and green Sneaker", "Blue Jeans", "Casual Golf Belt", "Custom T-Shirt",
               "Denim Short with Rhinestones", "Genuine Leather Handbag with Cell Phone Holder & Many Pockets", "Green and blue Sneaker"]

    @data((urunler))
    @unpack
    def test_app_shoes(self, beklenen_mesaj):
        anasehife = Homepage(self.driver)
        anasehife.apparel_shoes_tikla()
        mesaj = anasehife.apparel_shoes_urunlerini_dogrula()
        assert mesaj == beklenen_mesaj
