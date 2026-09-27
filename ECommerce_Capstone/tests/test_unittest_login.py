import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


class TestUnittestLogin(unittest.TestCase):

    def setUp(self):

        config = ConfigReader()

        service = Service(
            ChromeDriverManager().install()
        )

        self.driver = webdriver.Chrome(
            service=service
        )

        self.driver.maximize_window()

        self.driver.implicitly_wait(
            config.get_implicit_wait()
        )

        self.driver.get(
            config.get_url()
        )

    def test_login(self):

        config = ConfigReader()

        login_page = LoginPage(
            self.driver
        )

        login_page.click_signup_login()

        login_page.login(
            config.get_login_email(),
            config.get_login_password()
        )

        self.assertIn(
            "Logged in as",
            self.driver.page_source
        )

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main()