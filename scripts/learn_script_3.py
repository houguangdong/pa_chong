'''
Created on 2/6/2017

@author: ghou
'''


class HouGuangDong(object):

    @classmethod
    def store(cls, xing, age, entities={}):
        print xing, age, entities


HouGuangDong.store('hou', 17, {'13':'12'})


a = [
'2',
'37',
'38',
]

b = [
'vRA',
'VIO',
'Marvin2.0.0',
]


dictionary = dict(zip(a, b))
print dictionary
