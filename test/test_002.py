'''
@author: ghou
'''
import os
import re

from functools import reduce


def pre_edit(string_items):    
    def reducer(acc, y):
        print acc, y
        for i in acc:  
            acc.pop()
        print acc, '2222'
        acc.append(y)                                                                                   
        return acc
    result = reduce(reducer,string_items,[])      
    return result


text = "JGood is a handsome boy, he is cool, clever, and so on..."
print re.sub(r'\s', '-', text) 


ori = "Locale.addBundle('en"
filepath = "platform/sencha-platform/csp-content/locale/zh_TW/datatype.js"


def get_locale_replaced(old_str, source_path):
    '''replace locale string in the old str, get locale string from source_path'''
    #path: aa/bb/cc/locale/xx/abc.js ,xx is locale string
    if source_path.find(os.path.sep)> 0:
        sep = os.path.sep
    else:
        sep="/"

    locale =  source_path.split(sep)[-2]
    #Note that en must be the last two characters.
    if old_str.endswith('en'):
        print old_str,'1111', locale
        new_str = old_str[:-2]+locale
        return new_str
    else:
        return old_str
    


def ma(stri):
    reg = re.compile("(en)")
    if reg.match(stri):
        print '111111'
        
        
def sub1(stri):
    reg_1 = re.compile(".*Vcac\.content\.locale\.(.*)")
    cont = re.split(reg_1, stri)
    print cont


# def message_format():
#     str_new = "aaddd'a"
#     a = MessageFormat.format(str_new)
#     print a


if __name__ == '__main__':
#     a = [1,2,3,4]
#     z = pre_edit(a)
#     print z, '111'

#     print get_locale_replaced(ori,filepath)
#     ma('Een')
    sub1("xxxVcac.content.locale.en")
#     message_format()
    
    
    import re
    link = re.compile("\d+")
    content = "laowang-222haha"
    info = re.sub(link,'www.cnpythoner.com',content)
    print info
   