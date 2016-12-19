#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
穿越网页表单与登录窗口进行采集
'''

import requests

params = {"firstname": "Pyan", "lastname": "Mitchell"}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print r.text

params_1 = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r1 = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params_1)
print r1.text
 
files = {'uploadFile': open('C:/Users/ghou.VMWAREM/Desktop/waanan/img/1.png')}
r2 = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print r2.text
 
params_2 = {'username': 'Ryan', 'password': 'password'}
r3 = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params_2)
print "Cookie is set to:"
print r3.cookies.get_dict()
print '---------------'
print 'Going to profile page....'
r4 = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r3.cookies)
print r4.text
 
 
session = requests.Session()
params_3 = {'username': 'username', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params_3)
print "Cookie is set to:"
print s.cookies.get_dict()
print '---------------'
print 'Going to profile page....'
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print s.text
 
 
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('ryan', 'password')
r5 = requests.post("http://pythonscraping.com/pages/auth/login.php", auth=auth)
print r5.text

params = {
    "comments": {'fff': 'ddd'},
    "messages": {'zzz': 'hhh'}
}
# a = requests.get("http://10.117.171.135:8089/api/l10n/vSphere/1.0.0/vimclient/en_US")
# print a.text
newHttp1 = "http://10.117.171.135:8089/api/l10n/{productName}/{version}/{componentName}/{locale}".format(productName='aaa', version='333', componentName='nicaine', locale='ko')
r = requests.post(newHttp1, json=params)
print r.text, '11111'
f = requests.get(newHttp1)
print f.text, '222'