from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Base page contains reusable Selenium methods
# like click, send_keys and wait handling.
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # function to use whether element is visible in webpage with one argument passed
    def find_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    # function to use whether element is clickable in webpage with one argument passed
    def find_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )

    # function to get a single web element in the webpage
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    # function to click with one argument passed
    def click(self, locator):
        element = self.find_clickable(locator)

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    # function to pass keys in the webpage with two arguments passed
    def send_keys(self, locator, text, clear_first=True):
        element = self.find_visible(locator)

        if clear_first:
            element.clear()

        element.send_keys(text)


