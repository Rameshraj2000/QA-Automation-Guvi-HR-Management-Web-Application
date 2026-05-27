from locators.locator import Pagelocator
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

#class working steps on login page
class LoginPage(BasePage):

    def username_field(self):
        return self.find_visible(Pagelocator.user_name).is_displayed()

    def password_field(self):
        return self.find_visible(Pagelocator.pass_field).is_displayed()

    def login(self, email, password):
        self.send_keys(Pagelocator.user_name, email)
        self.send_keys(Pagelocator.pass_field, password)
        self.click(Pagelocator.log_btn)

    def logout(self, email, password):
        self.send_keys(Pagelocator.user_name, email)
        self.send_keys(Pagelocator.pass_field, password)
        self.click(Pagelocator.log_btn)

    def click_logout(self):
        self.click(Pagelocator.logout_dropdown)
        self.click(Pagelocator.logout_btn)

    def click_forgot_pass(self):
        self.click(Pagelocator.forgot_pass)

    def forgot_user(self, hint):
        element = self.find_visible(Pagelocator.forgot_user)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()

        elements = Pagelocator.reset_password
        option = self.find_visible(elements)
        option.click()

    def reset_visible(self):
        return self.find_visible(Pagelocator.reset_pass_msg).is_displayed()





