from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Browser:

    def __init__(self, driver_exe, path, options=[]):
        if driver_exe == 'chromedriver':
            chromedriver_path_location = path

        if options:
            webdriver_options = webdriver.ChromeOptions()
            for option in options:
                webdriver_options.add_argument(option)

        self.driver = webdriver.Chrome(chromedriver_path_location, options=webdriver_options)

    def wait_for_element(self):
        # TODO: for replacing sleeps with webdriverwait
        pass

    def close_browser(self):
        self.driver.close()

    def cleanup_browser(self):
        self.driver.quit()
