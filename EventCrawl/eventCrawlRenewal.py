import os
import datetime
import time
# TODO: ^ replace these sleeps after with webdriverwait plz
from EventCrawl.Resources.Browser import Browser
from EventCrawl.Resources.Pages.LoginPage import LoginPage
from EventCrawl.Resources.Event import Event


working_file_path = os.getcwd()
chromedriver_path_location = f'{working_file_path}\Resources\webdriver\chromedriver.exe'
browser = Browser('chromedriver', chromedriver_path_location, ['--disable-notifications', '--start-maximized'])
# proxy setup for running at office
# browser = Browser('chromedriver', chromedriver_path_location, ['--disable-notifications', '--start-maximized',
#                                                                '--proxy-server=http://proxy-us.intel.com:911'])
facebook_url = 'http://www.facebook.com'

login_page = LoginPage(browser, facebook_url)
login_page.navigate_to_page()
login_page.enter_email('sherman.tempman@outlook.com')
login_page.enter_password('bubbleTea13')
home_page = login_page.submit_login()

# TODO: replace these sleeps after with webdriverwait plz
time.sleep(10)
home_page.enter_search('vogue theatre vancouver')
search_results_page = home_page.submit_search()

# TODO: replace these sleeps after with webdriverwait plz
time.sleep(10)
# !small warning!: the xpath in these following 2 methods seem to be flaky
# it fails more often the more I crawl the webpage
search_results_page.like_venue()
events_page = search_results_page.navigate_to_page()

# TODO: replace these sleeps after with webdriverwait plz
time.sleep(10)
venue_events_html = events_page.get_page_html()

# we no longer need the web page to be open, as we saved the page
browser.close_browser()

current_date_time = datetime.datetime.today().strftime('%m-%d-%Y-%H-%M-%S')
file_path = f'{working_file_path}\EventFiles\{current_date_time}.txt'
print(f'Writing event information to file: {current_date_time}.txt...')
# Pycharm gives an error if I don't specify the encoding
with open(file_path, 'a+', encoding='utf8') as event_file:
    upcoming_events = events_page.find_events(venue_events_html, 5)
    for event in upcoming_events:
        new_event = Event(event)
        event_date = new_event.get_event_date()
        event_link = new_event.get_event_link()
        event_name = new_event.get_event_name()
        event_time = new_event.get_event_time()
        event_venue = new_event.get_event_venue()

        event_file.write(f'Event Date: {event_date}\nTime: {event_time}\nEvent Venue: {event_venue}\n'
                         f'Event Name: {event_name}\nEvent Web link: {event_link}\n\n')

# optional TODO: user input venues
# optional TODO: url shortener

browser.cleanup_browser()
