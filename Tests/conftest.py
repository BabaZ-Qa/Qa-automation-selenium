import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
