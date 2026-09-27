from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.products_link = (
            By.CSS_SELECTOR,
            "a[href='/products']"
        )

    def click_products(self):

        products_link = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.products_link
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            products_link
        )

        self.driver.execute_script(
            "arguments[0].click();",
            products_link
        )

        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.url_contains("/products")
        )