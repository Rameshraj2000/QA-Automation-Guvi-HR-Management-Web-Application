import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardpage
from pages.user_page import UserPage

#Validate presence of the newly created user in the admin user list
@allure.feature("Search User")
@allure.story("Check New User")
def test_search_user(setup):
    logging_page = LoginPage(setup)
    dash_board = DashBoardpage(setup)
    user_login_page = UserPage(setup)

    logging_page.login("Admin", "admin123")
    dash_board.click_admin_tab()
    user_login_page.search_user("test_user@13")
    user_login_page.user_page()
    user_login_page.username_key("Chris John Joe")
    user_login_page.user_search_act()
    assert user_login_page.is_user_present("test_user@13")