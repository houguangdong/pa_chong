# -*- coding: utf-8 -*-
'''
Created on 2/15/2017

@author: ghou
'''
# 1 os.chdir() 方法用于改变当前工作目录到指定的路径。
import os, sys
path = "C:\\Users\\ghou.VMWAREM\\workspace\\network_data_collection"
# 查看当前工作目录
retval = os.getcwd()
print "当前工作目录为 %s" % retval
# 修改当前工作目录
os.chdir(path)
# 查看修改后的工作目录
retval = os.getcwd()
print "目录修改成功 %s" % retval

# 2 把json字典写入一个文件中
# f.write(json.dumps(comments))

# copy 文件
def copy_file(source_path, target_path):
    import shutil
    for parent,dirnames,filenames in os.walk(source_path):
        for filename in filenames:
            if not filename.endswith(".rc"): 
                continue
            file_path=parent  + "\\" + filename
            new_path = target_path + "\\" + filename
            shutil.copyfile(file_path, new_path)