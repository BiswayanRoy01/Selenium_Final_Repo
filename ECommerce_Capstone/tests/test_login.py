from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


def test_login(driver):

    config = ConfigReader()

    login_page = LoginPage(driver)

    login_page.click_signup_login()

    login_page.login(
        config.get_login_email(),
        config.get_login_password()
    )

    assert "Logged in as" in driver.page_source