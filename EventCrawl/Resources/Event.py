class Event:
    def __init__(self, event):
        self.event = event

    def get_event_date(self):
        return f'{self.event.table.tbody.tr.td.span.span.text} {self.event.table.tbody.tr.td.span.span.next_sibling.text}'

    def get_event_link(self):
        facebook_url = 'http://www.facebook.com'
        return f'{facebook_url}{self.event.table.tbody.tr.td.next_sibling.div.div.a["href"]}'

    def get_event_name(self):
        return self.event.table.tbody.tr.td.next_sibling.div.div.a.span.text

    def get_event_time(self):
        return self.event.table.tbody.tr.td.next_sibling.div.div.next_sibling.span.text

    def get_event_venue(self):
        return self.event.table.tbody.tr.td.next_sibling.next_sibling.div.div.a.text