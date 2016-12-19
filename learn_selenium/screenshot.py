# -*-coding:utf-8 -*-

import time
import re


from selenium import webdriver
from PIL import Image, ImageDraw, ImageFont
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def take_screenshot(url, reg=None, is_max=True, save_path=''):
    driver = webdriver.Firefox()
    # 设置浏览器宽、高
    if is_max:
        driver.maximize_window()
    driver.get(url)
    time.sleep(2) 
    # 方法1
#     element_list = driver.find_elements_by_class_name("myclass")
#     ele_list = []
#     for i in element_list:
#         if not i.location or not i.size or not i.text:
#             continue
#         loc = i.location
#         size= i.size  
#         e_text = i.text
#         ele_list.append((e_text, loc, size))
#     print ele_list
    
    # 方法2
    # print driver.page_source #这个函数获取页面的html
    data = driver.page_source.encode('utf-8')
    bs = BeautifulSoup(data)
    data_1 = bs.find_all(text=re.compile(reg))
    tag_list = []
    for z in data_1:
        new_data = str(bs.find(text=z).parent)
        idx = new_data.index(" ")
        tg = new_data[1: idx] 
        if tg and tg not in tag_list:
            tag_list.append(new_data[1:idx])
            ele_list = get_element(driver=driver, reg=reg, tag_list=tag_list)
#         new_string = "<span class='myclass2>" + str(z) + "</span>"
#         data.replace(str(z), new_string)
        
    # get total width and height
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
#     ele_list = []
#     if reg and 0:
#         ele_list = get_element(driver, reg)
    resource_path = save_path + "/screen_shot.png"
#     # save the webpage as screenshot
    driver.get_screenshot_as_file(resource_path)
    driver.close()
    draw_img(ele_list, total_width, total_height, resource_path, save_path)


def get_element(driver, reg=None, tag_list=None):
    ele_list = []
    for tag in tag_list:
        element_list = driver.find_elements_by_tag_name(tag)
        if not element_list:
            continue
        for element in element_list:
            zheng_ze = re.compile(reg)
            e_text = element.text
            print e_text
            if re.match(zheng_ze, e_text):
                loc = element.location
                size= element.size  
                ele_list.append((e_text, loc, size))
    return ele_list


def draw_img(element_list, total_width=0, total_height=0, resource_path='', save_xpath=''):
    # img1 for location, img2 for identifier
    img = Image.open(resource_path)
    img1 = Image.new("RGBA", (total_width, total_height), "white")
    img2 = Image.new("RGBA", (total_width, total_height), "white")
    i = 0
    print element_list
    for t, l, s in element_list:
#         if len(t) > 2 and re.search(re.compile(r"^\+.*\+$"), t): # t[0] == '+' and t[-1] == '+'
        if len(t) > 2:
            rangle=(int(l['x']),int(l['y']),int(l['x']+s['width']),int(l['y']+s['height']))
            frame=img.crop(rangle)
            # save the element's image  
            frame.save(save_xpath + "/img/"+str(i)+".png")
            tmp_img = Image.new("RGBA", (s['width'],s['height']), "gray")
            # paste the element and iden to img1 and img2
            img1.paste(frame,rangle)
            img2.paste(tmp_img,rangle)
            draw = ImageDraw.Draw(img2)
            i_font = ImageFont.truetype(save_xpath + '/Arial/Arial.ttf', 36) 
            draw.text((int(l['x']),int(l['y'])),str(i), fill=(0,0,0), font = i_font)
             
            # save the 1.5X element's image
            resize_f = frame.resize((s['width']*2,s['height']*2), Image.ANTIALIAS)
            resize_f.save(save_xpath + "/150img/"+str(i)+".png")
            i = i + 1
#             print t, l, s

    # save img1 and img2
    img1.save(save_xpath + "/pass.png")
    img2.save(save_xpath + "/iden.png")
  
    
import urllib
from io import open
import cStringIO

import socket  
import time  
import struct  
import os  


def get_world():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    sock.settimeout(1)  
    e=0  
    try:  
        sock.connect(('10.117.170.200', 4243))  
        print 'connect...'  
    except socket.timeout,e:  
        print 'timeout',e  
    except socket.error,e:  
        print 'error',e  
    except e:  
        print 'any',e  
    if not e: 
#         while (1):  
        filename = 'C:/Users/ghou.VMWAREM/Desktop/waanan/img/1.png'           # 输入文件名  
        FILEINFO_SIZE = struct.calcsize('128sI') # 128sI                             # 编码格式大小  
        print FILEINFO_SIZE, '55555'
        fhead = struct.pack('128sI', filename, os.stat(filename).st_size)     # 按照规则进行打包  
        print fhead, '2222', os.stat(filename).st_size
#             sock.send(fhead) #发送文件基本信息数据      C:/Users/ghou.VMWAREM/Desktop/waanan/img/1.png
        fp = open(filename, 'rb')  
        sock.send(str(os.stat(filename).st_size))
        sock.send("eng")
        sock.send("\n")
        while 1:        #发送文件  
            filedata = fp.read(1024)  
            print filedata
            if not filedata:  
                break  
            sock.send(filedata)  
        print "sending over..."  
        fp.close()  
    
    
#这是动态生成图片文件名的函数，就是取的url里的文件名  
def changeName(url) :   
    if url :  
        s=url.split('/')  
    return s[-1]  


imgPath = 'C:/Users/ghou.VMWAREM/Desktop/waanan/img2/'  #存放图片的本地路径
folder = 'C:/Users/ghou.VMWAREM/Desktop/waanan/img/'


#保存图片的函数，很简单的fileIO  
def savImg(folder) : 
    imageList = os.listdir(folder) 
    for img_num in imageList:
        image = Image.open(folder + img_num)
        buf = cStringIO.StringIO()
        image.save(buf, image.format, quality=75)
        data = buf.getvalue()
#         imgName = changeName(url)
        p = imgPath + img_num
        output = open(p, 'wb+')   
        print len(data)
        output.write(data)  
    output.close()  
    
    
if __name__ == "__main__":
    url = "file:///C:/Users/ghou.VMWAREM/Desktop/waanan/Dashboard/index.html"
    save_path = "C:/Users/ghou.VMWAREM/Desktop/waanan"
    reg = '\+.*\+'
#     take_screenshot(url, reg=reg, save_path=save_path)
#     savImg(folder)
    get_world()
    
