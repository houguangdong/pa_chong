#-*- coding:utf8 -*-
'''
Created on 12/10/2016

@author: ghou
'''

'''
开始采集
'''

import re
import datetime
import random

from urllib2 import urlopen 
from bs4 import BeautifulSoup

# 第三章
url4 = "http://en.wikipedia.org/wiki/Kevin_Bacon"
html4 = urlopen(url4)
bs4 = BeautifulSoup(html4)
 
for link in bs4.findAll("a"):
    if "href" in link.attrs:
        print link.attrs['href']
 
for link in bs4.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print link.attrs['href']

# seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html5 = urlopen("http://en.wikipedia.org" + articleUrl)
    bs5 = BeautifulSoup(html5)
    return bs5.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
 
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print newArticle
    links = getLinks(newArticle)

pages1 = set()
def getLinks1(pageUrl):
    global pages1 
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bs = BeautifulSoup(html)
    try:
        print bs.h1.get_text()
        print bs.find(id="mw-content-text").findAll("p")[0]
        print bs.find(id='ca-edit').find("span").find("a").attrs["href"]
    except AttributeError:
        print '页面缺少一些熟悉，不过不用担心'
    for link in bs.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages1:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print newPage
                pages1.add(newPage)
                getLinks1(newPage)

getLinks1("")

page = set()
random.seed(datetime.datetime.now())
# 获取页面所有内链列表
def getInternalLinks(bsObj3, includeUrl3):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj3.findAll("a", href=re.compile("^(/|.*"+includeUrl3+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外联的列表
def getExternalLinks(bsObj3, excludeUrl3):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj3.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl3+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html3 = urlopen(startingPage)
    bsObj3 = BeautifulSoup(html3)
    externalLinks = getExternalLinks(bsObj3, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj3, startingPage)
        return getInternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print "随机外链是:"+externalLink
    followExternalOnly(externalLink)
    
followExternalOnly("http://oreilly.com")

# 收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html3 = urlopen(siteUrl)
    bsObj3 = BeautifulSoup(html3)
    internalLinks = getInternalLinks(bsObj3, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj3, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print link
    for link in internalLinks:
        if link not in allIntLinks:
            print "即将获取链接的URL是:"+link
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")
