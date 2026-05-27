from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#function to work on cross browser
def get_driver(browser="chrome"):

    if browser == "chrome":

        options = Options()

        options.add_argument("--start-maximized")

        # disable password manager popup
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        options.add_experimental_option(
            "prefs",
            prefs
        )

        # additional popup blocking
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-save-password-bubble")

        driver = webdriver.Chrome(options=options)

    else:
        raise Exception("Invalid Browser")

    return driver