# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 18:38
# @File : demo10.py
# @Software : PyCharm
import os

# 文件操作
f = open("test.txt", "w")   # 打开文件，w模式，文件不存在就新建

f.write("hello world, i am here!--1\r")  # 将字符串写入文件中
f.write("hello world, i am here!--2\r")  # 将字符串写入文件中
f.write("hello world, i am here!--3")  # 将字符串写入文件中

f.close()   # 关闭文件

f2 = open("test.txt", "r")
content = f2.read(5)    # read方法，读取指定的字符，开始时定位在文件头部，每执行一次后移动指定字符数
print(content)

content = f2.read(5)
print(content)

f2.close()

f3 = open("test.txt", "r")
content = f3.readlines()    # 返回的是一个列表，元素是每一行的内容

i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
f3.close()

f4 = open("test.txt", "r")
content = f4.readline()     # 一次性读一行
print("1:%s" % content)
content = f4.readline()
print("2:%s" % content)
f4.close()

os.rename("test.txt", "test1.txt")
