from EventCrawl.Resources.Pages.Page import Page


class LoginPage(Page):
    def enter_email(self, email):
        email_field = self.browser.driver.find_element_by_xpath('//*[@id="email"]')
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.browser.driver.find_element_by_xpath('//*[@id="pass"]')
        password_field.send_keys(password)

    def submit_login(self):
        login_button = self.browser.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_button.submit()
