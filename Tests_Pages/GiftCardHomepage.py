from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GiftCardHome:
    def __init__(self, driver):
        self.driver = driver

    GIFT_CARD_URUN_CLICK = (By.XPATH, "//h2/a[text()='$25 Virtual Gift Card']")

    def gift_urunune_tikla(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (GiftCardHome.GIFT_CARD_URUN_CLICK)))
        self.driver.find_element(*GiftCardHome.GIFT_CARD_URUN_CLICK).click()
