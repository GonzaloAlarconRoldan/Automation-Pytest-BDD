from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """DON'T FORGET TO REPLACE FOR THE RIGHT LOCATORS"""
    signup_btn = (By.XPATH, "//a[@onclick='AbrirUsuario();']")
    email_txt = (By.ID, "user_username")
    pass_txt = (By.ID, "user_password")
    login_btn = (By.XPATH, "//a[contains(text(),'login')]")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """PAGE ACTIONS FOR LOGIN PAGE"""

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to check sign up link"""
    def is_signup_link_exist(self):
        return self.is_visible(self.login_btn)

    """this is used to login to the web app"""
    def do_login(self, username, password):
        self.do_send_keys(self.email_txt, username)
        self.do_send_keys(self.pass_txt, password)
        self.do_click(self.login_btn)
