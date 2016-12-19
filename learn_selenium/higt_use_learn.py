# -*-coding: utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _weakref import proxy


ff = webdriver.Firefox()
ff.get('http://www.python.org')
# 第一种延迟加载的方式     含蓄的加载 Implicit Waits example.
# try:
#     # top属于 myDynamicElement
#     element = WebDriverWait(ff, 2).until(EC.presence_of_element_located((By.ID, "top")))
#     print element
# finally:
#     ff.quit()
    
# 第二种
# wait = WebDriverWait(ff, 5)
# element1 = wait.until(EC.element_to_be_clickable(By.ID, 'someid'))
# print element1


# 第三种
# ff.implicitly_wait(6)
# ff.get('http://www.baidu.com')
# element2 = ff.find_element_by_id("myDynamicElement")
# print element2


# 远程WebDriver 取得一个截图
driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
driver.get('http://www.google.com')
driver.get_screenshot_as_file('/Screenshots/google.png')


# Using a FirefoxProfile
fp = webdriver.FirefoxProfile()
driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, browser_profile=fp)

# Using a FirefoxProfile
options = webdriver.ChromeOptions()
driver = webdriver.Remote(desired_capabilities=options.to_capabilities())


PROXY = "localhost:8080"
desired_capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
desired_capabilities['proxy'] = {
    'httpProxy' : PROXY,
    'ftpProxy' : PROXY,
    'sslProxy' : PROXY,
    'noProxy' : PROXY,
    'proxyType': "MANUAL",
    'class' : "org.openqa.selenium.Proxy",
    'autodetect': False,
}

driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=desired_capabilities)


#　firefox proxy
from selenium.webdriver.common.proxy import *
myProxy = "host:8080"
proxy = Proxy({
    'httpProxy' : myProxy,
    'ftpProxy' : myProxy,
    'sslProxy' : myProxy,
    'noProxy' : '',
    'proxyType': ProxyType.MANUAL,
})
driver = webdriver.Firefox(proxy=proxy)
caps = webdriver.DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(caps)
driver = webdriver.Remote(desired_capabilities=caps)
