import requests
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
from selenium import webdriver

browser = RoboBrowser(history=True, parser='html.parser')
browser.open('https://www.facebook.com')
login_form = browser.get_form(id='login_form')
login_form['email'].value = 'sherman.tempman@outlook.com'
login_form['pass'].value = 'bubbleTea13'
browser.submit_form(login_form)
# print(login_form)

# print(browser.parsed)

search_form = browser.get_forms()
# print(search_form)
search_form[0]['q'].value = 'vogue theatre vancouver'
browser.submit_form(search_form[0])

# browser.follow_link()
# print(browser.url)
# print(browser.parsed)
# for link in browser.find_all('a'):
#     print(link.get('href'))
