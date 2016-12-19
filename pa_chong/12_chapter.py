#-*- coding:utf8 -*-
'''
Created on 12/18/2016

@author: ghou
'''

'''
避开采集陷阱
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


session = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text)
print bsObj.find("table", {"class": "table-striped"}).get_text()


# driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver = webdriver.Firefox()
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print driver.get_cookies()
 
saveCookies = driver.get_cookies()
 
driver2 = webdriver.Firefox()
# driver2 = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()
for cookie in saveCookies:
    driver2.add_cookie(cookie)
 
driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print driver2.get_cookies()


# driver3 = webdriver.PhantomJS(executable_path='')
driver3 = webdriver.Firefox()
driver3.get("http://pythonscraping.com/pages/itsatrap.html")
links = driver3.find_elements_by_tag_name("a")
for link in links:
    if not link.is_displayed():
        print "The link"+link.get_attribute("href")+" is a trap"

fields = driver3.find_elements_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print "Do not change value of "+field.get_attname("name")