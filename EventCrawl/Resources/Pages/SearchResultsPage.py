from EventCrawl.Resources.Pages.Page import Page
from EventCrawl.Resources.Pages.EventsPage import EventsPage
import re


class SearchResultsPage(Page):
    def get_attribute_with_xpath(self, xpath, attribute):
        element = self.browser.driver.find_element_by_xpath(xpath)
        return element, element.get_attribute(attribute)

    def like_venue(self):
        like_button_xpath = '//*[starts-with(@id, "xt_uniq_")]/div/div[1]/a/' \
                            'following-sibling::div/span/div/div/div[2]/span/button'
        like_button, like_button_class = self.get_attribute_with_xpath(like_button_xpath, 'class')
        # when page is liked, the class attribute name contains 'PageLiked'; else, the name is 'PageLike'
        if 'PageLiked' in like_button_class:
            return
        like_button.click()

    def navigate_to_page(self):
        link = Page.get_attribute_with_xpath(self, '//*[starts-with(@id, "xt_uniq_")]/div/div[1]/a', 'href')
        event_venue_link = re.sub('\?ref=br_rs', 'events', link)
        self.browser.driver.get(event_venue_link)
        return EventsPage(self.browser, event_venue_link)
