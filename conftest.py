import pytest
from utils.driver_factory import get_driver

# Pytest fixture for browser setup and teardown
@pytest.fixture(scope='function')

def setup():
    driver = get_driver('chrome')
    driver.get('https://opensource-demo.orangehrmlive.com') #Webpage URL
    driver.maximize_window()

    yield driver

    driver.quit()