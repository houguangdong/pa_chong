#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
自然语言处理
'''

import re
import string
import operator
import pymysql

from urllib2 import urlopen
from bs4 import BeautifulSoup
from random import randint
from nltk import word_tokenize
from nltk import Text
from nltk.book import *


# def cleanInput(input):
#     input = re.sub('\n+', " ", input)
#     input = re.sub('\[[0-9]*\]', "", input)
#     input = re.sub(' +', " ", input)
#     input = bytes(input, "UTF-8")
#     input = input.decode("ascii", "ignore")
#     cleanInput = []
#     input = input.split(' ')
#     for item in input:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
#             cleanInput.append(item)
#     return cleanInput
# 
# def ngrams(input, n):
#     input = cleanInput(input)
#     output = {}
#     for i in range(len(input)-n+1):
#         ngramTemp = " ".join(input[i: i+n])
#         if ngramTemp not in output:
#             output[ngramTemp] = 0
#         output[ngramTemp] += 1
#     return output
# 
# content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# ngrams = ngrams(content, 2)
# sortedNgrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
# print sortedNgrams
# 
# 
# def wordListSum(wordList):
#     sum = 0
#     for word, value in wordList.item():
#         sum += value
#     return sum
# 
# def retrieveRandomWord(wordList):
#     randIndex = randint(1, wordListSum(wordList))
#     for word, value in wordList.item():
#         randIndex -= value
#         if randIndex <= 0:
#             return word
#         
# def buildWordDict(text):
#     # 剔除换行符和引号
#     text = text.replace("\n", " ")
#     text = text.replace("\"", "")
#     # 保证每个标点符号都和前面的单词在一起
#     # 这样不会被剔除, 保留在马尔可夫链中
#     punctuation = [',', '.',';',':']
#     for symbol in punctuation:
#         text = text.replace(symbol, " "+symbol+" ")
#     
#     words = text.split(" ")
#     # 过滤空单词
#     words = [word for word in words if word != ""]
#     
#     wordDict = {}
#     for i in range(1, len(words)):
#         if words[i-1] not in wordDict:
#             # 为单词新建一个字典
#             wordDict[words[i-1]] = {}
#         if words[i] not in wordDict[words[i-1]]:
#             wordDict[words[i-1]][words[i]] = 0
#         wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
#     return wordDict
# 
# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# wordDict = buildWordDict(text)
# 
# # 生成链长为100的马尔可夫链
# length = 100
# chain = ""
# currentWord = "I"
# for i in range(0, length):
#     chain += currentWord+" "
#     currentWord = retrieveRandomWord(wordDict[currentWord])
# print chain

conn = pymysql.connect(host='10.117.171.135', unix_socket='/tmp/mysql.sock', user='root', passwd='qwe123456', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("use wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message
        
def getLinks(fromPageId):
    cur.execute("select toPageId from links where fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]
    
def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

# 链接树要么为空, 要么包含多个链接
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # 停止递归 返回结果
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # 若此节点页面无链接， 则跳过此节点
            return {}
    if targetPageId in linkTree.keys():
        print "TARGET"+str(targetPageId)+" FOUND!"
        raise SolutionFound("PAGE: " + str(currentPageId))
    
    for branchKey, branchValue in linkTree.items():
        try:
            print branchKey, '1111', branchValue
            # 递归建立链接树
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print e.message
            raise SolutionFound("PAGE: " + str(currentPageId))
    return linkTree

try:
    searchDepth(134951, 1, {}, 4)
    print "No solution found"
except SolutionFound as e:
    print e.message
    
tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print text


