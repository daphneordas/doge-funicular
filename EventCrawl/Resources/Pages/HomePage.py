from EventCrawl.Resources.Pages.Page import Page


class HomePage(Page):
    def enter_search(self, search_terms):
        search_field = self.browser.driver.find_element_by_xpath('//*[starts-with(@id, "u_")]/input[2]')
        search_field.send_keys(search_terms)

    def submit_search(self):
        search_button = self.browser.driver.find_element_by_xpath('//*[starts-with(@id, "js_")]/form/button')
        search_button.submit()