from EventCrawl.Resources.Pages.Page import Page
from EventCrawl.Resources.Pages.SearchResultsPage import SearchResultsPage


class HomePage(Page):
    def enter_search(self, search_terms):
        self.enter_with_xpath('//*[starts-with(@id, "u_")]/input[2]', search_terms)

    def submit_search(self):
        self.submit_with_xpath('//*[starts-with(@id, "js_")]/form/button')
        return SearchResultsPage(self.browser, self.browser.driver.current_url)
