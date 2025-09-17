from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    LAPTOPUN_SEBET_TEXTI = (By.XPATH, "//td/a[text()='14.1-inch Laptop']")

    def urunun_sebetde_oldugunu_dogrulama(self):
        mesaaj = self.driver.find_element(*CartPage.LAPTOPUN_SEBET_TEXTI).text
        return mesaaj
