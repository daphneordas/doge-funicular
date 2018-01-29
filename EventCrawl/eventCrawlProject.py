import requests
from bs4 import BeautifulSoup

# login info: sherman.tempman@outlook.com  bubbleTea13
# log into facebook
facebook_login_data = {"email":"sherman.tempman@outlook.com", "pass":"bubbleTea13"}
facebook_session = requests.session()
#/login.php?login_attempt=1&lwv=100 ; https://www.facebook.com/login
facebook_login_request = facebook_session.post("https://www.facebook.com/login.php?login_attempt=1&amp;lwv=110", data=facebook_login_data)
print(facebook_login_request.status_code)

# for facebook search url, look for venue
facebook_search_data = {"q":"vogue theatre vancouver"}
facebook_search_request = facebook_session.get("https://www.facebook.com/search/top/", params=facebook_search_data)
# print("This is the url that we're searching for: %s" % facebook_search_request.url)
# print("Test print: %s" % facebook_search_request.content)
soup = BeautifulSoup(facebook_search_request.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
# find_page_link = soup.find_all('a')
# print(find_page_link)
# https://www.facebook.com/thevoguetheatrevancouver/events/
# press events tab (ex: https://www.facebook.com/pg/thevoguetheatrevancouver/events/)
# grab 5 divs of events in upcoming events (upcoming event page section tag: div class = _p6e _4-u3)
# process event info here
# open a file for writing with the following output: Event Date: , Time: , Event Venue: , Event Name: , Event web link:
# optional: link shortener
