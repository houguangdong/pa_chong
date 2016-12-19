# -*-coding:utf-8-*-
'''
Created on 2016年7月13日

@author: ghou
'''

import urllib2
from copy import deepcopy
from math import ceil
from _pyio import __metaclass__


a = [1, 2, 3, 4]
b = []
b = deepcopy(a)
print b

class Singleton(object):
     
    def __new__(cls, *arg, **wk):
        if not hasattr(cls, '_instance'):
            obj = super(Singleton, cls)
            cls._instance = obj.__new__(cls, *arg, **wk)
        return cls._instance
 
 
class MyClass(Singleton):
    a = 1
     
 
one = MyClass()
two = MyClass()
 
two.a = 2
print one.a
 
 
class Borg(object):
     
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
 
 
class MyClass2(Borg):
    a = 5
     
 
thre = MyClass2()
fou = MyClass2()
 
fou.a = 6
# print thre.a
 
print id(thre)
print id(fou)
 
print thre == fou
print thre is fou
print id(thre.__dict__)
print id(fou.__dict__)
     



#方法3:本质上是方法1的升级（或者说高级）版  
#使用__metaclass__（元类）的高级python用法  


class Singleton2(type):
    
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
        
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
#         return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2
    
six = MyClass3()
seven = MyClass3()

seven.a = 4
print six.a

print id(six)
print id(seven)

print six == seven
print six is seven

    
print '----------------------方法4--------------------------'  
#方法4:也是方法1的升级（高级）版本,  
#使用装饰器(decorator),  
#这是一种更pythonic,更elegant的方法,  
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的  


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x
        
e = MyClass4()
t = MyClass4()

t.a = 3
print e.a

print id(e)
print id(t)

print e == t
print e is t
e.x = 1
print e.x
print t.x

print '*' * 30

print ('hello python')
name = raw_input('what is your name?')
if name.endswith('hou'):
    print 'Hello hou'
elif name.endswith('guang'):
    print 'Hello guang'
else:
    print 'Hello dong'


def fib(n):
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b
fib(1000)


fruits = ['Banana', 'Apple', 'Lime']
list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]