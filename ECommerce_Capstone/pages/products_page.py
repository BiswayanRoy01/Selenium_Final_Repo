from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):

        self.driver = driver

        self.search_box = (
            By.ID,
            "search_product"
        )

        self.search_button = (
            By.ID,
            "submit_search"
        )

        self.products_title = (
            By.XPATH,
            "//h2[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SEARCHED PRODUCTS')]"
        )

    def search_product(self, product_name):

        # Wait until the Products page is loaded
        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.url_contains("/products")
        )

        # Wait for search box
        search = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.search_box
            )
        )

        # Scroll search box into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            search
        )

        # Enter product name
        search.clear()

        search.send_keys(product_name)

        # Wait for search button
        search_button = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.search_button
            )
        )

        # Scroll button into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            search_button
        )

        # Click using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            search_button
        )

    def get_search_results_title(self):

        element = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(
                self.products_title
            )
        )

        return element.text