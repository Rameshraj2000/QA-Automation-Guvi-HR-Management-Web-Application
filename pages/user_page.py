import time

from locators.locator import Pagelocator
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#class working steps on user page
class UserPage(BasePage):

    def search_user(self, hint):
        element = self.find_visible(Pagelocator.emp_user)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()
    def search_user_role(self):
        return self.click(Pagelocator.user_role)
    def search_user_drop(self):
        return self.click(Pagelocator.ess_user)

    def user_page(self):
        self.search_user_role()
        self.search_user_drop()

    def username_key(self, hint):
        element = self.find_visible(Pagelocator.emp_name)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()
        time.sleep(2)
        option = Pagelocator.employee_hint
        element = self.find_visible(option)
        element.click()

    def user_search_stat(self):
        return self.click(Pagelocator.user_status_user)
    def user_search_drop(self):
        return self.click(Pagelocator.enable_field)
    def click_search(self):
        return self.click(Pagelocator.user_search_btn)

    def user_search_act(self):
        self.user_search_stat()
        self.user_search_drop()
        self.click_search()

    def is_user_present(self, username):
        locator = (By.XPATH, f"//div[@role='row']//div[text()='{username}']")

        try:
            self.find_visible(locator)
            return True
        except:
            return False

