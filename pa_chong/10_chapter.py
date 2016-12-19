#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
采集JavaScript
'''

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# 菲波那切数列
# <script>
# var f = function(){
#     var a = 1;
#     var b = 1;
#     return function(){
#         var temp = b;
#         b = a + b;
#         a = temp;
#         return b;
#     }
# }
# var f = f();
# console.log(f + ' is in the Fibonacci sequence');
# console.log(f + ' is in the Fibonacci sequence');
# console.log(f + ' is in the Fibonacci sequence');
# </script>


driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print driver.find_element_by_id("content").text
driver.close()


driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
pageSource = driver.page_source
bs19 = BeautifulSoup(pageSource)
print bs19.find(id="content").get_text()
driver.close()


driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print driver.find_element_by_id("content").text
    driver.close()


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print "Timing out after 10 seconds and returning"
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


driver = webdriver.PhantomJS(executable_path='D:\\python2.7\\relationship\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print driver.page_source