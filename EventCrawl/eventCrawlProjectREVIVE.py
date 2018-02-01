import datetime
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
# TODO: ^ replace these sleeps after with webdriverwait plz

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--start-maximized')
# Change this to be the place where you put chromedriver.exe
chromedriver_path_location = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path_location, options=options)
# TODO: set a polling time limit for elements to appear on the page
# wait = WebDriverWait(driver, 5)
facebook_url = 'http://www.facebook.com'
driver.get(facebook_url)

# log into Facebook
email_field = driver.find_element_by_xpath('//*[@id="email"]')
email_field.send_keys('sherman.tempman@outlook.com')
password_field = driver.find_element_by_xpath('//*[@id="pass"]')
password_field.send_keys('bubbleTea13')
login_button = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login_button.submit()

# ids are dynamic, so have to search for them
# TODO: replace these sleeps after with webdriverwait plz
time.sleep(10)
search_field = driver.find_element_by_xpath('//*[starts-with(@id, "u_")]/input[2]')
search_field.send_keys('vogue theatre vancouver')
search_button = driver.find_element_by_xpath('//*[starts-with(@id, "js_")]/form/button')
search_button.submit()

# TODO: replace these sleeps after with webdriverwait plz
time.sleep(10)
places_container_xpath = '//*[starts-with(@id, "xt_uniq_")]/div/div[1]/a'
like_button = driver.find_element_by_xpath(f'{places_container_xpath}/following-sibling::div/span/div/div/div[2]'
                                           f'/span/button')
like_button_class = like_button.get_attribute('class')
# when page is liked, the class attribute name contains 'PageLiked'; else, the name is 'PageLike'
if 'PageLiked' in like_button_class:
    pass
else:
    like_button.click()

places_container = driver.find_element_by_xpath(places_container_xpath)
# check the first place in the places container
venue_link = places_container.get_attribute('href')
# go to the first venue link with events
event_venue_link = re.sub('\?ref=br_rs', 'events', venue_link)
driver.get(event_venue_link)

time.sleep(10)
# dump the page into beautiful soup html parser
venue_events_html = driver.page_source
soup = BeautifulSoup(venue_events_html, 'html.parser')
# we no longer need the web page to be open, as we saved the page
driver.close()

current_date_time = datetime.datetime.today().strftime('%m-%d-%Y-%H-%M-%S')
file_path = f'C:\\Users\dordas\PycharmProjects\doge-funicular\EventCrawl\EventFiles\{current_date_time}.txt'
print(f'Writing event information to file: {current_date_time}.txt...')
with open(file_path, 'a+') as event_file:
    # TODO: add check if page has events; search for '... does not have any upcoming events.'
    # no_upcoming_events = soup.find_all(class_=re.compile(''))
    upcoming_events_divs = soup.find_all(class_=re.compile('_24er'), limit=5)
    for event_cell in upcoming_events_divs:
        event_month = event_cell.table.tbody.tr.td.span.span.text
        event_day = event_cell.table.tbody.tr.td.span.span.next_sibling.text
        event_link = facebook_url + event_cell.table.tbody.tr.td.next_sibling.div.div.a['href']
        event_name = event_cell.table.tbody.tr.td.next_sibling.div.div.a.span.text
        event_time = event_cell.table.tbody.tr.td.next_sibling.div.div.next_sibling.span.text
        event_venue = event_cell.table.tbody.tr.td.next_sibling.next_sibling.div.div.a.text
        event_location = event_cell.table.tbody.tr.td.next_sibling.next_sibling.div.div.next_sibling.text

        # write all info to a file, the file appears in the same place this script is located
        event_file.write(f'Event Date: {event_month} {event_day}\nTime: {event_time}\nEvent Venue: {event_venue}\n'
                         f'Event Name: {event_name}\nEvent Web link: {event_link}\n\n')

# optional TODO: user input venues
# optional TODO: url shortener

driver.quit()
