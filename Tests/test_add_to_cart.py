import pytest
from Tests_Pages.Homepage import Homepage


@pytest.mark.usefixtures("test_setup")
class TestCartButton:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage = Homepage(self.driver)

    def test_adds_products_to_cart(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        laptop_page = self.homepage.laptop_urunune_tikla()
        laptop_page.laptop_add_to_cart_bas()
        urun_ismi = cartpage = laptop_page.sebet_linkine_bas_mehsulu_bax()
        mesaj = cartpage.urunun_sebetde_oldugunu_dogrulama()
        assert mesaj == "14.1-inch Laptop"
