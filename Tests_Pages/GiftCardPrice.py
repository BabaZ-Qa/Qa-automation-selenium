from selenium.webdriver.common.by import By


class GiftCardPrice:
    def __init__(self, driver):
        self.driver = driver

    GIFTCARD_URUN_ADI = (
        By.XPATH, "//h1[contains(text(),'$25 Virtual Gift Card')]")
    GIFTCARD_URUN_QIYMETI = (By.XPATH, "//span[contains(text(),'25.00')]")

    def gift_urun_ad_dogrula(self):
        ad = self.driver.find_element(*GiftCardPrice.GIFTCARD_URUN_ADI).text
        return ad

    def gift_urununun_qiymetini_dogrula(self):
        qiymet = self.driver.find_element(
            *GiftCardPrice.GIFTCARD_URUN_QIYMETI).text
        return qiymet
