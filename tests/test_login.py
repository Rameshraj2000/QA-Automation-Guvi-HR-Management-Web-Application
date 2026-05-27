from pages.login_page import LoginPage
from utils.excel_reader import read_login_data, write_result

#Test Validate login functionality using multiple sets of credentials
def test_login_multiple_credentials(setup):
    login = LoginPage(setup)

    data, wb, sheet = read_login_data("test_data/Task_15 (1).xlsx")

    for row, username, password in data:

        login.login(username, password)

        if "dashboard" in setup.current_url.lower():
            write_result(wb, sheet, row, "PASS")
            login.click_logout()
        else:
            write_result(wb, sheet, row, "FAIL")

        setup.get("https://opensource-demo.orangehrmlive.com")

#Test Verify that the home URL is accessible
def test_home_url(setup):
    assert "orangehrmlive.com" in setup.current_url

#Test Validate presence of login fields
def test_user_pass_field(setup):
    login_page = LoginPage(setup)
    assert login_page.username_field()
    assert login_page.password_field()

# def test_login(setup):
#     login_page = LoginPage(setup)
#     login_page.login("Admin", "admin123")
#     assert "dashboard" in setup.current_url

#Test Verify "Forgot Password" link functionality
def test_forgot_pass(setup):
    login_page = LoginPage(setup)
    login_page.click_forgot_pass()
    login_page.forgot_user("dummy")
    assert login_page.reset_visible()