import pytest
from Tests_Pages import PageBase
from Tests_Pages.GiftCardHomepage import GiftCardHome
from Tests_Pages.GiftCardPrice import GiftCardPrice
import softest


@pytest.mark.usefixtures("test_setup")
class Testvisible(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.gift_card = GiftCardHome(self.driver)

    @pytest.mark.smut
    def test_mehsulun_adi_qiymetini_dogrulama(self):
        gift_price = self.gift_card.gift_urunune_tikla()
        giftin_adi = gift_price.gift_urun_ad_dogrula()
        giftin_qiymeti = gift_price.gift_urununun_qiymetini_dogrula()
        print("Urunun adi:"+giftin_adi)
        print("Urunun qiymeti:"+giftin_qiymeti)
        assert giftin_adi == '$25 Virtual Gift Card'
        assert giftin_qiymeti == '25.00'
