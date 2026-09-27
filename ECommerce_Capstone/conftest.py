import pytest

from utilities.driver_factory import DriverFactory
from utilities.config_reader import ConfigReader
from utilities.screenshot import Screenshot


@pytest.fixture
def driver(request):

    config = ConfigReader()

    driver = DriverFactory.create_driver(
        config.get_browser()
    )

    driver.implicitly_wait(
        config.get_implicit_wait()
    )

    driver.get(
        config.get_url()
    )

    yield driver

    # Take screenshot if test failed
    if request.node.rep_call.failed:

        Screenshot.take_screenshot(
            driver,
            request.node.name
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )


def pytest_configure(config):

    if hasattr(config, "_metadata"):

        config._metadata["Project"] = (
            "ECommerce Selenium Automation"
        )

        config._metadata["Framework"] = (
            "Selenium + PyTest + POM"
        )

        config._metadata["Browser"] = "Chrome"

        config._metadata["Application"] = (
            "AutomationExercise"
        )