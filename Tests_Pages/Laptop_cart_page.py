from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LaptopCartpage:
    def __init__(self, driver):
        self.driver = driver

    LAPTOP_ADD_TO_CART_BUTTON = ((
        By.CSS_SELECTOR, "input[id^='add-to-cart']"))
    SHOPPING_CART_CLICK = ((By.XPATH, "//a[text()='shopping cart']"))

    def laptop_add_to_cart_bas(self):
        self.driver.find_element(
            *LaptopCartpage.LAPTOP_ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (LaptopCartpage.SHOPPING_CART_CLICK)))

    def sebet_linkine_bas_mehsulu_bax(self):
        self.driver.find_element(*LaptopCartpage.SHOPPING_CART_CLICK).click()
