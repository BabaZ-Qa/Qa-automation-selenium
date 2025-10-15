from pathlib import Path
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(
            GeckoDriverManager().install()))
    else:
        print("Hic bir tarayici girmediniz")
    if env == "qa":
        base_url = "https://qa-demowebshop.tricentis.com/"
    elif env == "dev":
        base_url = "https://dev-demowebshop.tricentis.com/"
    elif env == "test":
        base_url = "https://test-demowebshop.tricentis.com/"
    elif env == "prod":
        base_url = "https://demowebshop.tricentis.com/"
    else:
        print("Environment girmediniz")
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Otomasyon Raporu"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    bugun = datetime.now()
    rapor_klasoru = Path("raporlar", bugun.strftime("%Y-%m-%d"))
    rapor_klasoru.mkdir(parents=True, exist_ok=True)
    rapor = rapor_klasoru / f"rapor {bugun.strftime("%H-%M")}.html"
    config.option.htmlpath = rapor
    config.option.self_contained_html = True
