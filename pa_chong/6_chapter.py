#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
读取文档
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
from io import StringIO
from io import open
import csv
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from zipfile import ZipFile
from io import BytesIO


textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print textPage.read()
  
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print str(textPage.read())

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
content = bytes(content, "utf-8")
content = content.decode("utf-8")
print content

data = urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for row in csvReader:
    print row

data1 = urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile1 = StringIO(data1)
dictReader = csv.DictReader(dataFile1)
print dictReader.fieldnames
for row in dictReader:
    print row
    
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
     
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
     
    content = retstr.getvalue()
    retstr.close()
    return content
 
pdfFile = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print outputString
pdfFile.close()    

wordFile = urlopen("http://www.pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
print xml_content.decode('utf-8')
wordObj = BeautifulSoup(xml_content.decode('utf-8'))
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print "<h1>"
            closeTag = "</h1>"
    except AttributeError:
        # 不打印标签
        pass
    print textElem.text
    print closeTag, '111'
