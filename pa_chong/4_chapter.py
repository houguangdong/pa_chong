#-*- coding:utf8 -*-
'''
Created on 12/10/2016

@author: ghou
'''

'''
使用API
'''

import re
import datetime
import random
import json

from urllib2 import urlopen 
from bs4 import BeautifulSoup
from urllib2 import HTTPError

# 第四章 解析json数据

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')
print getCountry("50.78.253.58")
 
 
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}], "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)
 
print jsonObj.get("arrayOfNums")
print jsonObj.get("arrayOfNums")[1]
print jsonObj.get("arrayOfNums")[1].get('number') + jsonObj.get("arrayOfNums")[2].get("number")
print jsonObj.get("arrayOfFruits")[2].get('fruit')


random.seed(datetime.datetime.now())

def getLinks4(articleUrl):
    html5 = urlopen("http://en.wikipedia.org" + articleUrl)
    bs5 = BeautifulSoup(html5)
    return bs5.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
  
  
def getHistoryIPs(pageUrl):
    # 编辑历史页面URL链接格式是:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print "history url is: " + historyUrl
    html6 = urlopen(historyUrl)
    bsObj = BeautifulSoup(html6)
    # 找出class属性是"mw-anonuserlink"的链接
    # 他们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class": "wm-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList
  
  
def getCountry4(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')
 
  
links = getLinks4("/wiki/Python_(programming_language)")
 
while len(links) > 0:
    for link in links:
        print '-------------------------', link.attrs['href']
        historyIPs = getHistoryIPs(link.attrs['href'])
        print historyIPs, '+++++++++++++'
        for historyIP in historyIPs:
            country = getCountry4(historyIP)
            if country is not None:
                print historyIP + "is from" + country
    newLink = links[random.randint(0, len(links)-1)].attrs['href'] 
    links = getLinks4(newLink)
