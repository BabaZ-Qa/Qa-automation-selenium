import pytest
from Tests_Pages.Homepage import Homepage


@pytest.mark.usefixtures("test_setup")
class TestHomeTry:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage = Homepage(self.driver)

    @pytest.mark.alma
    def test_books_kisminda_derhal_add_cart_bas(self):
        urun_page = self.homepage.ust_taraftaki_books_kismina_tikla()
        urun_page.urune_tiklamadan_add_to_cart_et()

        message = urun_page.magaza_sehifesindeki_add_cart_sonraki_mesaji_dogrula()
        assert message == "The product has been added to your shopping cart"
