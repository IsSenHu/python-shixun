# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 18:55
# @File : catch.py
# @Software : PyCharm

# 异常处理
"""
try:
    print("-------test1")
    f = open("123.txt", "r")
    print("-------test2")
except IOError:
    print("产生错误了")

# 获取错误描述
try:
    print("-------test1")
    f = open("123.txt", "r")
    print("-------test2")
except Exception as result:     # Exception可以承接任何异常
    print("产生错误了")
    print(result)
"""

# try catch finally
try:
    f = open("123.txt", "r")
except Exception as result:
    print("发生异常")
    print(result)
finally:
    print("程序执行完毕")
