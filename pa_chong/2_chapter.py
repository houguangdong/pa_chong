#-*- coding:utf8 -*-
'''
Created on 12/10/2016

@author: ghou
'''

'''
复杂HTML解析
'''

import re
from urllib2 import urlopen 
from bs4 import BeautifulSoup

# 数据采集第二章    例子2
url2 = "http://www.pythonscraping.com/pages/warandpeace.html"
html2 = urlopen(url2)
bsObj2 = BeautifulSoup(html2)

name_list = bsObj2.findAll("span", {'class': 'green'})
for name in name_list:
    print name.get_text()
     
a = bsObj2.findAll({'h1', 'h2', 'h3'})
a = bsObj2.findAll("span", {'class': {'green': "red"}})
a = len(bsObj2.findAll(text='the prince'))
allText = bsObj2.findAll(id='text')
print allText[0].get_text()
bsObj2.findAll(id="text")
bsObj2.findAll("", {"id":"text"})
bsObj2.findAll(class_="green")
bsObj2.findAll("", {"class": "green"})

# 子标签
url3 = "http://www.pythonscraping.com/pages/page3.html"
html3 = urlopen(url3)
bs = BeautifulSoup(html3)
for child in bs.find("table", {"id": "giftList"}).children:
    print child
  
# 兄弟标签
for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings: 
    print sibling

# 父标签
print bs.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

# 正在表达式
images = bs.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print image['src']
print bs.findAll(lambda tag: len(tag.attrs) == 2)