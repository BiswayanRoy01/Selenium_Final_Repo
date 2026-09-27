from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def create_driver(browser="chrome"):

        if browser.lower() == "chrome":

            options = webdriver.ChromeOptions()

            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")

            service = Service(
                ChromeDriverManager().install()
            )

            driver = webdriver.Chrome(
                service=service,
                options=options
            )

            driver.maximize_window()

            return driver

        else:

            raise ValueError(
                f"Unsupported browser: {browser}"
            )