from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()


class TestHomepage:
    def test_homep(self):
        driver.get("https://demowebshop.tricentis.com/")
        expected_result = ["BOOKS", "COMPUTERS", "ELECTRONICS",
                           "APPAREL & SHOES", "DIGITAL DOWNLOADS", "JEWELRY", "GIFT CARDS"]
        actual_result = [item.text for item in driver.find_elements(
            By.XPATH, "//ul[@class='top-menu']/li/a")]
        assert expected_result == actual_result
        driver.quit()
