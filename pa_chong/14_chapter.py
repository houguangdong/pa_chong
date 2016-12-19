#-*- coding:utf8 -*-
'''
Created on 12/18/2016

@author: ghou
'''

'''
远程采集
'''


import socks
import socket
from urllib import urlopen
from selenium import webdriver

# 方法一
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print urlopen("http://icanhazip.com").read()

# 方法二
service_args = ['--proxy=localhost:9150', '--proxy-type=socks5']
driver = webdriver.PhantomJS(executable_path='<path to PhantomJS>', service_args=service_args)
driver.get("http://icanhazip.com")
print driver.page_source
driver.close()