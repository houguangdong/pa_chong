#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''
from django.templatetags.i18n import language

'''
图像识别与文字处理
'''

import time
import subprocess
import requests
from PIL import Image, ImageFilter
from PIL import ImageOps
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver


kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    
    # 对图片进行阀值过滤, 然后保存
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    
    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newFilePath, "output"])
    
    # 打开文件读取结果
    outputFile = open("output.txt", 'r')
    print outputFile.read()
    outputFile.close()
    
cleanFile("1.jpg", "1_bak.png")


# 创建新的selenium driver
driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
# driver = webdriver.Firefox()
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# 单机图书预览按钮
driver.find_element_by_id("siteLogoImg").click()
imageList = set()

# 等待页面加载完成
time.sleep(5)
# 当向右箭头可以点击时  开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载的新页面(一次可以加载多个页面 但是重复的页面不能加载到集合中)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(page)

driver.quit()

# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print f.read()


def main(self):
    language = "eng"
    fontName = "captchaFont"
    directory = "<path to images>"
    
def runAll(self):
    self.createFontFile()
    self.cleanImages()
    self.renameFiles()
    self.extractUnicode()
    self.runShapeClustering()
    self.runMfTraining()
    self.runCnTraining()
    self.createTessData()
    

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html)
# 收集需要处理的表单数据 (包括验证码和输入字段)
imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
formBuildId = bsObj.find("input", {"name": "form_build_id"})["value"]
captchaSid = bsObj.find("input", {"name": "captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name": "captcha_token"})["value"]

captchaUrl = "http://pythonscraping.com" + imageLocation
urlretrieve(captchaUrl, "captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "r")
# 清理识别结果中的空格和换行符
captchaResponse = f.read().replace(" ", "").replace("\n", "")
print "Captcha solution attempt: " + captchaResponse

if len(captchaResponse) == 5:
    params = {
            "captcha_token": captchaToken, "captcha_sid": captchaSid,
            "form_id": "comment_node_page_form", "form_build_id": formBuildId,
            "captcha_response": captchaResponse, "name": "Ryan Mitchell",
            "subject": "I come to seek the Grail",
            "comment_body[und][0][value]": "...and I am definitely not a bot"  
            }
    r = requests.post("http://www.pythonscraping.com/comment/reply/10", data=params)
    responseObj = BeautifulSoup(r.text)
    if responseObj.find("div", {"class": "message"}) is not None:
        print responseObj.find("div", {"class": "message"}).get_text()
else:
    print "There was a problem reading the CAPTCHA correctly!"

