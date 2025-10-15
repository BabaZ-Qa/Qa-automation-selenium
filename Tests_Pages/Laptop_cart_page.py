from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Tests_Pages.PageBase import PageBase
from Tests_Pages.Cartpage import CartPage
from Tests_Pages.GiftCardPrice import GiftCardPrice


class LaptopCartpage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LAPTOP_ADD_TO_CART_BUTTON = ((
        By.CSS_SELECTOR, "input[id^='add-to-cart']"))
    SHOPPING_CART_CLICK = ((By.XPATH, "//a[text()='shopping cart']"))

    FICTION_BOOKS_URUN_LINKI = (By.XPATH, "//h2/a[text()='Fiction']")

    MAGAZA_SEHIFESINDE_ADD_TO_CART_SONRAKI_MESAJ = (By.XPATH, "(//div//p)[1]")

    MAGAZA_SEHIFESINDEKI_ADD_TO_CART_BUTTON = (
        By.XPATH, "(//div/input[contains(@class,'button-2')])[2]")

    def laptop_add_to_cart_bas(self):
        self.driver.find_element(
            *LaptopCartpage.LAPTOP_ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (LaptopCartpage.SHOPPING_CART_CLICK)))

    def sebet_linkine_bas_mehsulu_bax(self):
        self.driver.find_element(*LaptopCartpage.SHOPPING_CART_CLICK).click()
        cartpage = CartPage(self.driver)
        return cartpage

    def fiction_books_urunune_tikla(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (LaptopCartpage.FICTION_BOOKS_URUN_LINKI)))
        self.driver.find_element(
            *LaptopCartpage.FICTION_BOOKS_URUN_LINKI).click()
        books_cart_page = GiftCardPrice(self.driver)
        return books_cart_page

    def urune_tiklamadan_add_to_cart_et(self):
        self.driver.find_element(
            *LaptopCartpage.MAGAZA_SEHIFESINDEKI_ADD_TO_CART_BUTTON).click()
        self.wait_element_visible(
            LaptopCartpage.MAGAZA_SEHIFESINDE_ADD_TO_CART_SONRAKI_MESAJ)

    def magaza_sehifesindeki_add_cart_sonraki_mesaji_dogrula(self):
        mesaj = self.driver.find_element(
            *LaptopCartpage.MAGAZA_SEHIFESINDE_ADD_TO_CART_SONRAKI_MESAJ).text
        return mesaj
