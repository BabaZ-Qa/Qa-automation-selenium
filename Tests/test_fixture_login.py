import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")


@pytest.fixture()
def Login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class='radius']").click()
    mesaj = driver.find_element(By.ID, "flash").text
    return mesaj


A1 = Login("ifejife", "hfuehf")
A2 = Login("tomsmith", "fefef")
A3 = Login("tomsmith", "SuperSecretPassword!")


def test_login_user(Login):
    assert "Your username is invalid!" in A1


def test_login_pass(Login):
    assert 'Your password is invalid!' in A2


def test_login_succ(Login):
    assert "You logged into a secure area!" in A3


driver.quit()
