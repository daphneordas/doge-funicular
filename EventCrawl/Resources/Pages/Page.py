from bs4 import BeautifulSoup


class Page:
    def __init__(self, browser, url):
        self.url = url
        self.browser = browser

    def enter_with_xpath(self, xpath, value):
        field = self.browser.driver.find_element_by_xpath(xpath)
        field.send_keys(value)

    def submit_with_xpath(self, xpath):
        element = self.browser.driver.find_element_by_xpath(xpath)
        element.submit()

    def get_attribute_with_xpath(self, xpath, attribute):
        element = self.browser.driver.find_element_by_xpath(xpath)
        return element.get_attribute(attribute)

    def get_page_html(self):
        soup = BeautifulSoup(self.browser.driver.page_source, 'html.parser')
        return soup

    def navigate_to_page(self):
        self.browser.driver.get(self.url)
