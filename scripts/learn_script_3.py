'''
Created on 2/6/2017

@author: ghou
'''


class HouGuangDong(object):

    @classmethod
    def store(cls, xing, age, entities={}):
        print xing, age, entities


HouGuangDong.store('hou', 17, {'13':'12'})