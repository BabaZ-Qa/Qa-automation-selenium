import pytest
from Tests_Pages.Homepage import Homepage
from Tests_Pages.Laptop_cart_page import LaptopCartpage
from Tests_Pages.GiftCardPrice import GiftCardPrice


@pytest.mark.usefixtures("test_setup")
class TestBooksAddCart:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage = Homepage(self.driver)

    def test_books_add_cart(self):
        books_urununu_secme = self.homepage.books_linkine_tikla()

        books_cart_page = books_urununu_secme.fiction_books_urunune_tikla()

        books_cart_page.books_urunun_sayisini_artirmayi_dogrula()
        books_cart_page.books_urununu_add_to_cart_et()

        message = books_cart_page.books_urunun_sebetde_oldugunu_dogrula()
        assert message == "The latest fiction book"
