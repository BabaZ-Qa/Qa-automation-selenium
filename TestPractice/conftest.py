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
        print("You did not enter a browser")
    if env == "qa":
        base_url = "https://qa-practicetestautomation.com/practice-test-login/"
    elif env == "dev":
        base_url = "https://dev-practicetestautomation.com/practice-test-login/"
    elif env == "test":
        base_url = "https://test-practicetestautomation.com/practice-test-login/"
    elif env == "prod":
        base_url = "https://practicetestautomation.com/practice-test-login/"
    else:
        print("You did not enter an environment")
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Automation Report"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_file = Path("raporlar", today.strftime("%Y-%m-%d"))
    report_file.mkdir(parents=True, exist_ok=True)
    rapor = report_file / f"rapor {today.strftime("%H-%M")}.html"
    config.option.htmlpath = rapor
    config.option.self_contained_html = True
