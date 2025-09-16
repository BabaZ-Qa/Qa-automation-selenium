import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("test_setup")
class TestCartButton:
    def test_adds_products_to_cart(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.find_element(
            By.XPATH, "//h2/a[text()='14.1-inch Laptop']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "input[id^='add-to-cart']").click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//a[text()='shopping cart']")))
        self.driver.find_element(
            By.XPATH, "//a[text()='shopping cart']").click()
        mesaj = self.driver.find_element(
            By.XPATH, "//td/a[text()='14.1-inch Laptop']").text
        assert mesaj == "14.1-inch Laptop"
