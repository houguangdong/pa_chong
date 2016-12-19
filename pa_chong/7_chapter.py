#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
数据清洗
'''

import re
import string

from urllib2 import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict


def ngrams(input, n):
    input = re.sub('\n+', " ", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    print input
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i: i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
print ngrams
print "2-grams count is: "+str(len(ngrams))


def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams1(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i: i+n])
    return output


ngrams1 = ngrams1(input, 2)
ngrams1 = OrderedDict(sorted(ngrams1.items(), key=lambda t: t[1], reverse=True))
print ngrams1