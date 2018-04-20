from EventCrawl.Resources.Pages.Page import Page
from EventCrawl.Resources.Pages.HomePage import HomePage


class LoginPage(Page):
    def enter_email(self, email):
        self.enter_with_xpath('//*[@id="email"]', email)

    def enter_password(self, password):
        self.enter_with_xpath('//*[@id="pass"]', password)

    def submit_login(self):
        self.submit_with_xpath('//*[@id="loginbutton"]')
        return HomePage(self.browser, self.browser.driver.current_url)
