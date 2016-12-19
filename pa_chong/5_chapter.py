#-*- coding:utf8 -*-
'''
Created on 12/10/2016

@author: ghou
'''

'''
存储数据
'''

import re
import os
import csv
import datetime
import time
import random
import pymysql

from urllib2 import urlopen 
from bs4 import BeautifulSoup
from urllib import urlretrieve
import smtplib
from email.mime.text import MIMEText


# 第五章
html7 = urlopen("http://www.pythonscraping.com")
bs7 = BeautifulSoup(html7)
imageLocation = bs7.find("a", {"id": "logo"}).find("img")['src']
urlretrieve(imageLocation, "logo.jpg")
  
  
downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"
   
   
def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url
   
   
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
       
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path
   
   
html8 = urlopen("http://www.pythonscraping.com")
bsObj8 = BeautifulSoup(html8)
downloadList = bsObj8.findAll(src=True)
   
   
for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print fileUrl
  
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
  
  
csvFile = open("../files/test.csv", "w+")
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()
  
  
html9 = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs9 = BeautifulSoup(html9)
# 主对比表格是当前页面上的第一个表格
table = bs9.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")
  
csvFile = open("../files/editors.csv", "wt")
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()
 
# 链接mysql
conn = pymysql.connect(host='10.117.171.135', unix_socket='/tmp/mysql.sock', user='root', passwd='qwe123456', db='mysql')
cur = conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id=4")
print cur.fetchone()
cur.close()
conn.close()
  
conn1 = pymysql.connect(host='10.117.171.135', unix_socket='/tmp/mysql.sock', user='root', passwd='qwe123456', db='mysql', charset='utf8')
cur1 = conn1.cursor()
cur1.execute("use scraping")
 
random.seed(datetime.datetime.now())
 
 
def store(title, content):
    cur1.execute("insert into pages (title, content) values(\"%s\", \"%s\")", (title, content))
    cur1.connection.commit()
 
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
 
links = getLinks("/wiki/Kevin_Bacon")
 
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) -1)].attrs["href"]
        print newArticle
        links = getLinks(newArticle)
finally:
    cur1.close()
    conn1.close()
 
conn2 = pymysql.connect(host='10.117.171.135', unix_socket='/tmp/mysql.sock', user='root', passwd='qwe123456', db='mysql', charset='utf8')
cur2 = conn2.cursor()
cur2.execute("use wikipedia")
 
def insertPageIfNotExists(url):
    cur2.execute("select * from pages where url=%s", (url))
    if cur2.rowcount == 0:
        cur2.execute("insert into pages (url) values (%s)", (url))
        conn2.commit()
        return cur2.lastrowid
    else:
        return cur2.fetchone()[0]
     
def insertLink(fromPageId, toPageId):
    cur2.execute("select * from links where fromPageId=%s and toPageId=%s", (int(fromPageId), int(toPageId)))
    if cur2.rowcount == 0:
        cur2.execute("insert into links (fromPageId, toPageId) values (%s, %s)", (int(fromPageId), int(toPageId)))
        conn2.commit()
         
pages = set()
 
def getLinks2(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj2 = BeautifulSoup(html)
    for link in bsObj2.findAll('a', href=re.compile("^(/wiki/)((?!:).)*$")): 
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # 遇到一个新页面, 加入集合并搜索里面的词条链接
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks2(newPage, recursionLevel + 1)
getLinks2("/wiki/Kevin_Bacon", 0)
cur2.close()
conn2.close()

# 发邮件
msg = MIMEText("The body of the email is here")
msg['Subject'] = "An Email Alert"
msg['From'] = "ghou@vmware.com"
msg['To'] = "1737785826@qq.com"
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'lianxi@qq.com'
    msg['To'] = '1737785826@qq.com'
    
s1 = smtplib.SMTP("localhost")
s1.send_message(msg)
s1.quit()
bsObj3 = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj3.find("a", {'id': 'answer'}).attrs['title']=="NO"):
    print "It is not Christmas yet."
    time.sleep(3600)
bsObj4 = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to https://isitchristmas.com, it is Christmas")