from tests.data_used_in_tests import *
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.login_page import LoginPage
from faker import Faker

fake = Faker("en")


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_01_log_in_log_out_passed(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(valid_email, valid_password)
        WebDriverWait(self.driver, 10, 0.5).until(ec.url_to_be, main_url)
        assert log_in.is_logout_link_displayed()
        log_in.logout()
        WebDriverWait(self.driver, 10, 0.5).until(ec.url_to_be, main_url)
        assert log_in.is_login_link_displayed()

    def test_02_log_in_failed_invalid_email(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(fake.email(), valid_password)
        self.driver.implicitly_wait(10)
        assert error_message == log_in.get_error_message_login_failed()

    def test_03_log_in_failed_invalid_password(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(valid_email, fake.word())
        self.driver.implicitly_wait(10)
        assert error_message == log_in.get_error_message_login_failed()

    def test_04_log_in_failed_password_blank(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(valid_email, blank_password)
        self.driver.implicitly_wait(10)
        assert error_message == log_in.get_error_message_login_failed()

    def test_05_log_in_failed_email_and_password_blank(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(blank_email, blank_password)
        self.driver.implicitly_wait(10)
        assert error_message == log_in.get_error_message_login_failed()

    def test_06_log_in_failed_email_blank(self):
        log_in = LoginPage(self.driver)
        log_in.open_page()
        log_in.login(blank_email, valid_password)
        self.driver.implicitly_wait(10)
        assert error_message == log_in.get_error_message_login_failed()