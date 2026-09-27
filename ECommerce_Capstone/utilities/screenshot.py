import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def take_screenshot(driver, test_name):

        screenshot_folder = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "screenshots"
        )

        os.makedirs(
            screenshot_folder,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"{test_name}_{timestamp}.png"
        )

        file_path = os.path.join(
            screenshot_folder,
            file_name
        )

        driver.save_screenshot(file_path)

        print(
            f"\nScreenshot saved: {file_path}"
        )

        return file_path