#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
用爬虫测试网站
'''

import unittest
from urllib2 import urlopen 
from urllib import unquote
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
        url = "http://pythonscraping.com/pages/javascript/draggableDemo.html"
        driver.get(url)
        print "Setting up the test"
 
    def tearDown(self):
        print "Tearing down the test"
         
    def test_twoPlusTwo(self):
        total = 2 + 2
        self.assertEqual(4, total)
    
    def test_drag(self):
        global driver
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()
        self.assertEqual("You are definitely not a bot!", driver.find_element_by_id("message").text)


class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print 'Done!'

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        # 使用第五章介绍的方法返回随机链接
        pass

    @classmethod
    def setUpClass(cls):
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)
 
    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)

    
if __name__ == '__main__':
    unittest.main()
    
driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python" in driver.title
driver.close()


driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/files/form.html")
firstnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")


# 方法1
firstnameField.send_keys("Hou")
lastnameField.send_keys("GuangDong")
submitButton.click()


# 方法2
# actions = ActionChains(driver).click(firstnameField).send_keys("ni").click(lastnameField).send_keys('hao').send_keys(Keys.RETURN)
# actions.perform()

 
print driver.find_element_by_tag_name("body").text
driver.close()


driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver.get("http://pythonscraping.com/pages/javascript/draggableDemo.html")

print driver.find_element_by_id("message").text

element = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("div2")
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()

print driver.find_element_by_id("message").text

# 截屏
driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/")
driver.get_screenshot_as_file("tmp/pythonscraping.png")    