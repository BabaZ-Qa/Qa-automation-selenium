from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Testvisible:
    def test_mehsulun_adi_qiymetini_dogrulama(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//h2/a[text()='$25 Virtual Gift Card']")))
        driver.find_element(
            By.XPATH, "//h2/a[text()='$25 Virtual Gift Card']").click()
        ad = driver.find_element(
            By.XPATH, "//h1[contains(text(),'$25 Virtual Gift Card')]").text
        qiymet = driver.find_element(
            By.XPATH, "//span[contains(text(),'25.00')]").text
        assert ad == '$25 Virtual Gift Card'
        assert qiymet == '25.00'
        driver.quit()
