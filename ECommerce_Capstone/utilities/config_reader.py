import configparser
import os

from dotenv import load_dotenv


class ConfigReader:

    def __init__(self):

        load_dotenv()

        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config.read(config_path)

    def get_url(self):

        return self.config["environment"]["url"]

    def get_browser(self):

        return self.config["environment"]["browser"]

    def get_implicit_wait(self):

        return int(
            self.config["timeouts"]["implicit_wait"]
        )

    def get_explicit_wait(self):

        return int(
            self.config["timeouts"]["explicit_wait"]
        )

    def get_login_email(self):

        return os.getenv("LOGIN_EMAIL")

    def get_login_password(self):

        return os.getenv("LOGIN_PASSWORD")