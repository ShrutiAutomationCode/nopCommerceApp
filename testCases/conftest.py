import pytest
from selenium import webdriver

"""
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    return driver
"""


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver


"""
If we comment this pytest_addoption method then we will this error
pytest: error: unrecognized arguments: --browser chrome
"""


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
