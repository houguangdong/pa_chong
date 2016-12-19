# -*-coding:utf-8-*-

import time

from selenium import webdriver
from PIL import Image, ImageDraw, ImageFont

# 
# driver = webdriver.Firefox()
# driver.get("http://10.117.169.164:9000/vco-controlcenter/#/control-app/workflows")
# 
# time.sleep(2) 
# 
# # get total width and height
# total_width = driver.execute_script("return document.body.offsetWidth")
# total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
# 
# img_list = driver.find_elements_by_tag_name('img')
# for element in img_list:
#     loc = element.location
#     size= element.size  
# 
# span_list = driver.find_elements_by_tag_name('span')
# for span in span_list:
#     pass


# i = 0
# while i < 10:
#     print i 
#     time.sleep(2)
#     i += 1
# print i, '11111'

# a = {}
# a[16] = {1, 3, 4, 5, 6, 8, 9, 10, 11, 12}
# c = {}
# for i, v in a.iteritems():
#     for _idx, b in enumerate(list(v)):
#         pass
# print c
# 
# c = [1, 3, 4, 5, 6, 8, 9, 10, 11, 12]
# d = []
# for idx, i in enumerate(c):
#     print idx, d
#     if idx == 0:
#         d.append(i)
#         print d
#     elif d[idx-1] + 1 == i:
#         print d
#         d.append(i)
# print d

# a = 'ÄãºÃ£¡ ÎÒÏë"Äã""'
# if a.endswith("") and a.startswith(""):
#     c = a.strip("\"")
#     b = '"' + c + '"'
#     print '11111'
# elif a.endswith(""):
#     b = a.strip("\"") + '"'
#     print '222222'
# elif a.startswith(""):
#     b = '"' + a.strip("\"")
#     print '333333'
# print b

# d = '"sdssdds""'
# print d[0], d[-2]
# if d[0]=="\"" or d[-1]=="\"":
#     if d.startswith('""') and d.endswith('""'):
#         d = '"' + d.strip("\"") + '"'
#         print '1111'
#         print d
#     elif d.endswith('""'):
#         d = d.rstrip("\"") + '"'
#         print d
#         print '22323'
#     elif d.startswith('""'):
#         d = '"' + d.lstrip("\"") 
#         print '22222'
#         print d
#     else:
#         d = d.strip("\"")
#         print '44444'
#         print d
        
    

# curr_value = "\"dsadadasdsad\""
# print curr_value[0], curr_value[-1]
# if curr_value[0]=="\"" or curr_value[-1]=="\"":
#     print '1111111'
#     print curr_value.strip("\"")
#     print curr_value[1:-1]


# import os 
# rootdir = "D:\\work\\g11n-grm\\l10n_parser\\tests\\data\\extjs\\"
# for parent, dirnames, filenames in os.walk(rootdir):
#     print parent, dirnames, filenames



# from urllib2 import Request
# import urllib2
# response = urllib2.urlopen(z)
# print response.read()