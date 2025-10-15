from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Tests_Pages.PageBase import PageBase


class GiftCardPrice(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GIFTCARD_URUN_ADI = (
        By.XPATH, "//h1[contains(text(),'$25 Virtual Gift Card')]")
    GIFTCARD_URUN_QIYMETI = (By.XPATH, "//span[contains(text(),'25.00')]")

    BOOKS_URUNUN_QUANTITY_AYARLAMA = (
        By.CSS_SELECTOR, "input[id^='addtocart']")

    FICTION_BOOKS_URUNUNUN_ADD_CART_BUTTON = (
        By.CSS_SELECTOR, "input[id^='add-to-cart']")

    URUNUN_SEBETDE_OLDUGUNU_DOGRULA = (By.XPATH, "(//div//p)[1]")

    def gift_urun_ad_dogrula(self):
        ad = self.driver.find_element(*GiftCardPrice.GIFTCARD_URUN_ADI).text
        return ad

    def gift_urununun_qiymetini_dogrula(self):
        qiymet = self.driver.find_element(
            *GiftCardPrice.GIFTCARD_URUN_QIYMETI).text
        return qiymet

    def books_urunun_sayisini_artirmayi_dogrula(self):
        self.driver.find_element(
            *GiftCardPrice.BOOKS_URUNUN_QUANTITY_AYARLAMA).clear()
        self.driver.find_element(
            *GiftCardPrice.BOOKS_URUNUN_QUANTITY_AYARLAMA).send_keys("2")

    def books_urununu_add_to_cart_et(self):
        self.driver.find_element(
            *GiftCardPrice.FICTION_BOOKS_URUNUNUN_ADD_CART_BUTTON).click()
        self.wait_element_presence(
            GiftCardPrice.URUNUN_SEBETDE_OLDUGUNU_DOGRULA)

    def books_urunun_sebetde_oldugunu_dogrula(self):
        mesaj = self.driver.find_element(
            *GiftCardPrice.URUNUN_SEBETDE_OLDUGUNU_DOGRULA).text
        return mesaj
