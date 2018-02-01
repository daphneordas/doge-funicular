class Page:
    def __init__(self, browser, url):
        self.url = url
        self.browser = browser
        self.browser.driver.get(self.url)
