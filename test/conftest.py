import configparser

import allure
import pytest

from browser.driver_factory import Driver

config = configparser.ConfigParser()
config.read('auto_test.cfg')


@pytest.fixture
def driver():
    driver_name: str = config.get('BROWSER', 'driver')
    return Driver(driver_name)


def pytest_bdd_before_scenario(request):
    base_url: str = config.get('URL', 'url')
    driver = request.getfixturevalue('driver')
    driver.driver.get(base_url)


def pytest_bdd_after_scenario(request):
    driver = request.getfixturevalue('driver')
    driver.driver.quit()


