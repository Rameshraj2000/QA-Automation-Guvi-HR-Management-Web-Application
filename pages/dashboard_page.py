from locators.locator import Pagelocator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time

#class working steps on dasnboard page
class DashBoardpage(BasePage):

    def admin_items(self):
        return self.find_visible(Pagelocator.admin_item)

    def pim_items(self):
        return self.find_visible(Pagelocator.pim_item)
    def leave_items(self):
        return self.find_visible(Pagelocator.leave_item)

    def click_leave_item(self):
        self.click(self.leave_items())
    def time_item(self):
        return self.find_visible(Pagelocator.time_item)
    def recruitment_item(self):
        return self.find_visible(Pagelocator.recruitment_item)
    def myinfo_item(self):
        return self.find_visible(Pagelocator.myinfo_item)
    def click_myinfo(self):
        self.click(self.myinfo_item())
    def performance_item(self):
        return self.find_visible(Pagelocator.performance_item)
    def dashboard_item(self):
        return self.find_visible(Pagelocator.dashboard_item)
    def click_admin_tab(self):
        return self.click(Pagelocator.admin_item)
    def click_add_user(self):
        return self.click(Pagelocator.add_user)
    def click_user_role(self):
        return self.click(Pagelocator.user_role)
    def click_user_dropdown(self):
        return self.click(Pagelocator.ess_user)
    def click_emp_name(self):
        return self.click(Pagelocator.emp_name)

    def emp_hint(self, hint):
        element = self.find_visible(Pagelocator.emp_name)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()

        # small wait for suggestions to appear
        time.sleep(1)

        option = Pagelocator.employee_hint
        element = self.find_visible(option)
        element.click()

    def click_status(self):
        return self.click(Pagelocator.status_field)
    def click_status_drop(self):
        return self.click(Pagelocator.enable_field)
    def username_key(self, hint):
        element = self.find_visible(Pagelocator.emp_user)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()

    def enter_password(self, pas):
        element = self.find_visible(Pagelocator.emp_pass)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(pas).perform()

    def confirm_password(self, pas):
        element = self.find_visible(Pagelocator.emp_conf_pass)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(pas).perform()

        elements = self.find_visible(Pagelocator.save_btn)
        elements.click()

    def user_personal_check(self):
        return self.find_visible(Pagelocator.user_personal_field)
    def personal_detail_visible(self):
        element = self.find_visible(Pagelocator.user_personal)
        element.click()

    def user_contact_check(self):
        return self.find_visible(Pagelocator.user_contact_field)
    def user_contact_visible(self):
        element = self.find_visible(Pagelocator.user_contact)
        element.click()

    def user_emergency_check(self):
        return self.find_visible(Pagelocator.user_emergency_field)
    def user_emergency_visible(self):
        element = self.find_visible(Pagelocator.user_emergency)
        element.click()

    def user_dependant_check(self):
        return self.find_visible(Pagelocator.user_dependant_field)
    def user_dependant_visible(self):
        element = self.find_element(Pagelocator.user_dependant)
        element.click()

    def user_immigration_check(self):
        return self.find_visible(Pagelocator.user_immigration_field)
    def user_immigration_visible(self):
        element = self.find_element(Pagelocator.user_immigration)
        element.click()

    def user_job_check(self):
        return self.find_visible(Pagelocator.user_job_field)
    def user_job_visible(self):
        element = self.find_element(Pagelocator.user_job)
        element.click()

    def user_salary_check(self):
        return self.find_visible(Pagelocator.user_salary_field)
    def user_salary_visible(self):
        element = self.find_element(Pagelocator.user_salary)
        element.click()

    def user_report_check(self):
        return self.find_visible(Pagelocator.user_report_field)
    def user_report_visible(self):
        element = self.find_element(Pagelocator.user_report)
        element.click()

    def user_qualification_check(self):
        return self.find_visible(Pagelocator.user_qualification_field)
    def user_qualification_visible(self):
        element = self.find_element(Pagelocator.user_qualification)
        element.click()

    def user_membership_check(self):
        return self.find_visible(Pagelocator.user_membership_field)
    def user_membership_visible(self):
        element = self.find_element(Pagelocator.user_membership)
        element.click()

    def click_assign_leave(self):
        return self.click(Pagelocator.assign_leave_btn)

    def user_leave(self, hint):
        element = self.find_visible(Pagelocator.leave_employee_name)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()

        elements = Pagelocator.leave_emp_drop
        options = self.find_visible(elements)
        options.click()

    def leave_type(self):
        element = self.find_visible(Pagelocator.leave_type)
        element.click()

    def leave_type_drop(self):
        element = self.find_visible(Pagelocator.leave_type_drop)
        element.click()

    def from_leave_dates(self, hint):
        element = self.find_visible(Pagelocator.leave_from_date)
        element.click()
        element.clear()
        element.send_keys(hint)

    def to_leave_dates(self, hint):
        element = self.find_visible(Pagelocator.leave_to_date)
        element.click()
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(hint)
        element.send_keys(Keys.TAB)

    def leave_partial(self):
        element = self.find_visible(Pagelocator.leave_days)
        element.click()

    def leave_partial_drop(self):
        element = self.find_visible(Pagelocator.leave_days_drop)
        element.click()

    def leave_half_full(self):
        element = self.find_visible(Pagelocator.leave_days_duration)
        element.click()

    def leave_half_drop(self):
        element = self.find_visible(Pagelocator.leave_duration_drop)
        element.click()


    def leave_comments(self, hint):
        element = self.find_visible(Pagelocator.leave_comments)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(hint).perform()

    def assign_leave(self):
        button = self.find_clickable(Pagelocator.leave_assign_btn)
        button.click()

    def wait_leave_popup(self):
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(Pagelocator.leave_confirm_popup)
        )

    def click_ok_leave(self):
        self.wait_leave_popup()
        self.find_clickable(Pagelocator.leave_ok_btn).click()


    def check_leave_success(self):
        return self.find_visible(Pagelocator.leave_message)

    def emp_claim_click(self):
        return self.find_clickable(Pagelocator.emp_claim).click()

    def emp_claim_btn(self):
        return self.find_clickable(Pagelocator.emp_claim_btn).click()

    def emp_claim_event(self):
        self.find_clickable(Pagelocator.emp_claim_event).click()

        element = self.find_clickable(Pagelocator.emp_claim_event_drop)

        element.click()

    def emp_claim_currency(self):
        self.find_visible(Pagelocator.emp_claim_currency).click()

        element = self.find_visible(Pagelocator.emp_claim_currency_drop)

        element.click()

    def emp_claim_remarks(self, hint):
        return self.send_keys(Pagelocator.emp_claim_remarks, hint)

    def emp_claim_create_btn(self):
        return self.find_clickable(Pagelocator.emp_claim_create_btn).click()

    def emp_claim_submit(self):
        return self.find_clickable(Pagelocator.emp_claim_sub_btn).click()

    def emp_claim_myclaim(self):
        return self.find_visible(Pagelocator.emp_claim_myclaim).click()

    #function to check whether the claim is present in the user page or not
    def verify_claim_created(self, claim_text):
        locator = (
            By.XPATH,
            f"//div[@role='row']//div[contains(normalize-space(),'{claim_text}')]"
        )

        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        return element.is_displayed()


    def verify_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Pagelocator.success_toast)
        )

    # function used to check whether leave request has been submitted
    def verify_leave_created(self, employee_name):
        locator = (
            By.XPATH,
            f"//div[@role='cell'][contains(normalize-space(),'{employee_name}')]"
        )

        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        return element.is_displayed()

