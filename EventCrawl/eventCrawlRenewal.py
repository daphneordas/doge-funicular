from EventCrawl.Resources.Browser import Browser
from EventCrawl.Resources.Pages.LoginPage import LoginPage


path = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
browser = Browser('chromedriver', path, ['--disable-notifications', '--start-maximized'])

facebook_url = 'http://www.facebook.com'
login_page = LoginPage(browser, facebook_url)
login_page.enter_email('sherman.tempman@outlook.com')
login_page.enter_password('bubbleTea13')
login_page.submit_login()

browser.close_browser()
browser.cleanup_browser()
