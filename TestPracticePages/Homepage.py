import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setupp")
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def test_loginleri_dene(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    def test_mesajlarini_dogrula(self):
        try:
            mesaj = self.driver.find_element(By.ID, "error").text
            return mesaj
        except:
            mesaj = self.driver.find_element(By.XPATH, "//div/h1").text
            return mesaj
