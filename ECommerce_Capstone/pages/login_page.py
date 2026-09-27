from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.signup_login_link = (
            By.LINK_TEXT,
            "Signup / Login"
        )

        self.email_field = (
            By.CSS_SELECTOR,
            "input[data-qa='login-email']"
        )

        self.password_field = (
            By.CSS_SELECTOR,
            "input[data-qa='login-password']"
        )

        self.login_button = (
            By.CSS_SELECTOR,
            "button[data-qa='login-button']"
        )

    def click_signup_login(self):

        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.signup_login_link
            )
        )

        element = self.driver.find_element(
            *self.signup_login_link
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        WebDriverWait(
            self.driver,
            15
        ).until(
            EC.url_contains("/login")
        )

    def enter_email(self, email):

        email_field = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.email_field
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            email_field
        )

        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):

        password_field = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.password_field
            )
        )

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):

        login_button = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.login_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            login_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

    def login(self, email, password):

        self.enter_email(email)

        self.enter_password(password)

        self.click_login()