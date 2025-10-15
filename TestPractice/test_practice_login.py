"""
Login Page Test
Author: Babazahid Zayidov
Description: Tests login functionality with valid and invalid credentials using DDT and POM.
"""

from TestPracticePages.Homepage import HomePage
import pytest
from ddt import ddt, data, unpack
import unittest


@pytest.mark.usefixtures("test_setup")
@ddt
class TestLoginPage(unittest.TestCase):
    InvalidUsername = ("fh", "ef", "Your username is invalid!")
    InvalidPassword = ("student", "fe", "Your password is invalid!")
    ValidLogin = ("student", "Password123", "Logged In Successfully")

    @data(InvalidUsername, InvalidPassword, ValidLogin)
    @unpack
    def test_logins(self, username, password, expected_message):
        homepage = HomePage(self.driver)
        homepage.test_login_functionality(username, password)

        message = homepage.test_login_messages()
        assert message == expected_message, f"Expected '{expected_message}', but got '{message}'"
