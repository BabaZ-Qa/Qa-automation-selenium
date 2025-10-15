import pytest
from Tests_Pages.GiftCardHomepage import GiftCardHome


@pytest.mark.usefixtures("test_setup")
class TestUstTaraf:
    def test_ust_taraflarin_gorunduyunu_dogrula(self):
        urunler = ["BOOKS", "COMPUTERS", "ELECTRONICS",
                   "APPAREL & SHOES", "DIGITAL DOWNLOADS", "JEWELRY", "GIFT CARDS"]
        anasehife = GiftCardHome(self.driver)
        mesaj = anasehife.ust_taraf_sekmeler()
        assert urunler == mesaj
