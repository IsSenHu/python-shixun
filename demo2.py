# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/2 23:37
# @File : demo2.py
# @Software : PyCharm
"""
import keyword

print("标准化输出字符串")
a = 10
print("这是变量: ", a)

print(keyword.kwlist)
"""

# 格式化输出 %s %d
age = 18
print("我的名字是: %s, 我的国籍是: %s" % ("胡森", "中国"))
print("我的年纪是: %d岁" % age)

print("aaa", "bbb", "ccc", sep=".")

print("hello", end="")
print("world", end="\t")
print("python", end="\n")
print("end")

# 输入
password = input("请输入密码")
print("您刚刚输入的密码是: ", password)

# 变量类型
a = 10
print(type(a))

# 强制类型转换
a = int(password)
b = a + 100
print(b)

