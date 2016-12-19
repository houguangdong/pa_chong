# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.switch_to import SwitchTo
from cProfile import Profile

driver = webdriver.Firefox()
driver.get('http://www.google.com')


inputElement = driver.find_element_by_name("q")
print inputElement
inputElement.send_keys("cheese!")
inputElement.submit()
try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print driver.title
finally:
    driver.quit()

# 通过ID定位元素
<div id="coolestWidgetEvah">xxx</div>
element = driver.find_element_by_id("coolestWidgetEvah")
or
element = driver.find_element(by=By.ID, value="coolestWidgetEvah")

# 通过类名定位
<div class="cheese"><span>Cheddar</span></div>
<div class="cheese"><span>Gouda</span></div>

cheeses = driver.find_element_by_class_name("cheese")
or
cheeses = driver.find_element(By.CLASS_NAME, "cheese")

# 通过标签名
<input name = 'cheese' type="text"/>

cheese = driver.find_element_by_name('cheese')
or
cheese = driver.find_element(By.NAME, 'cheese')

# 通过连接文本
<a href="http://www.google.com/search?q=cheese">cheese</a>
cheese = driver.find_element_by_link_text("cheese")
or
cheese = driver.find_element(By.LINK_TEXT, "cheese")

# 按链接文本部分匹配定位
<a href="http://www.google.com/search?q=cheese">search for cheese</a>
<a href="http://www.google.com/search?q=cheese">cheese</a>
cheese = driver.find_element_by_partial_link_text("cheese")
or
cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")

# 通过CSS
<div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>
cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
or
cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

# 通过XPATH
<input type="text" name="example" /> 
<INPUT type="text" name="other" />
<div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>
inputs = driver.find_element_by_xpath("//input")
or
inputs = driver.find_element(By.XPATH, "//input")

# 使用JavaScript
element = driver.execute_script("return $('.cheese')[0]")

#发现所有的紧挨着label元素的input元素的例子：
labels = driver.find_element_by_name('label')
inputs = driver.execute_script("var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" + "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)

# 获取文本的值
element = driver.find_element_by_id("element_id")
print element.text

# 用户输入-填写表格
select = driver.find_element_by_tag_name("select")
allOptions = select.find_element_by_tag_name("option")
for option in allOptions:
    print "Value is:" + option.get_attribute("value")
    option.click()
    
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_tag_name("select"))
select.deselect_all()
select.select_by_visible_text("Edam")

# 提交
driver.find_element_by_id("submit").click()

# 自带提交
element.submit()

# 在窗口或者框架间移动
driver。sitch_to.window("windowName")


<a href="somewhere.html" target="windowName">Click here to open a new window</a>
for handle in driver.window_handles:
    driver.switch_to.window(handle)

driver.switch_to.frame("frameName")


# 弹出对话框：
alert = driver.switch_to_alert()

# 导航：历史和位置
driver.forward()
driver.back()

# Cookies
driver.get("http://www.example.com")
driver.add_cookie({'name': 'key', 'value': 'value', 'path': '/'})
for cookie in driver.get_cookies():
    print '%s --> %s' % (cookie['name'], cookie['value'])
    
driver.delete_cookie('CookieName')
driver.delete_all_cookies()

# 拖拽操作
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_name('source')
target = driver.find_element_by_name('target')
ActionChains(driver).drag_and_drop(element, target).perform()


# HtmlUnit Driver
driver = webdriver。Remote("http://localhost:4444:wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
driver = webdriver.Remote("http://localhost:4444:wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)

# profile
profile = webdriver.FirefoxProfile()
Profile.native_events_enabled = True
driver = webdriver.Firefox(profile)

driver = webdriver。Ie()
driver = webdriver.Chrome()
# def by_url_get_info(self, url):
#     ff = webdriver.Firefox()
#     ff.get(url)
#     pass