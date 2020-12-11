from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
        self.login_link = (By.LINK_TEXT, "Log In")
        self.logout_link = (By.LINK_TEXT, "Logout")
        self.error_message_text = (By.XPATH, "//div[@class='msg-error']")

    def open_page(self):
        self.driver.get("https://harvardartmuseums.org/user/login")

    def login(self, username, password):
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_link).click()

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def is_login_link_displayed(self):
        return self.driver.find_element(*self.login_link).is_displayed()

    def get_error_message_login_failed(self):
        return self.driver.find_element(*self.error_message_text).text
