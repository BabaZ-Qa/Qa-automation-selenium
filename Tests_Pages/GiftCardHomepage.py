from selenium.webdriver.common.by import By
from Tests_Pages.GiftCardPrice import GiftCardPrice

from Tests_Pages.PageBase import PageBase


class GiftCardHome(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GIFT_CARD_URUN_CLICK = (By.XPATH, "//h2/a[text()='$25 Virtual Gift Card']")

    def gift_urunune_tikla(self):
        gift_urun_link = self.wait_element_visibility(
            GiftCardHome.GIFT_CARD_URUN_CLICK)
        gift_urun_link.click()
        gift_price = GiftCardPrice(self.driver)
        return gift_price

    def ust_taraf_sekmeler(self):
        isimler = [isim.text for isim in self.driver.find_elements(
            By.XPATH, "//ul[@class='top-menu']/li/a")]
        return isimler
