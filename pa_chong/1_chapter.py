#-*- coding:utf8 -*-
'''
Created on 12/10/2016

@author: ghou
'''

'''
第１章   初见网络爬虫
'''

from urllib2 import urlopen 
from bs4 import BeautifulSoup
from urllib2 import HTTPError


url = "http://www.pythonscraping.com/pages/page1.html"
html = urlopen(url)
bsObj = BeautifulSoup(html)
print bsObj.h1
 
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
     
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print title