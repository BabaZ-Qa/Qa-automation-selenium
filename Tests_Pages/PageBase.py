from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        return element

    def wait_element_presence(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(locator))
        return element

    def wait_alert_present(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            expected_conditions.alert_is_present(locator))
        return element

    def wait_element_visible(self, locator):
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator))
        return element
