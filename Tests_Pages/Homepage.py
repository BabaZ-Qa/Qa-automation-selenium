from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def laptop_urunune_tikla(self):
        self.driver.find_element(
            By.XPATH, "//h2/a[text()='14.1-inch Laptop']").click()

    def sehifedeki_yukari_kisimdaki_nesneleri_dogrula(self):
        real_result = [item.text for item in self.driver.find_elements(
            By.XPATH, "//ul[@class='top-menu']/li/a")]
        return real_result
