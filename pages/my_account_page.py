from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

        self.logout_link = (By.LINK_TEXT, "Logout")

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def logout(self):
        self.driver.find_element(*self.logout_link).click()

