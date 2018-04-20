from EventCrawl.Resources.Pages.Page import Page
import re


class EventsPage(Page):

    def find_events(self, soup, limit):
        return soup.find_all(class_=re.compile('_24er'), limit=limit)
