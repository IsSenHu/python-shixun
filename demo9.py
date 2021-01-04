# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 18:13
# @File : demo9.py
# @Software : PyCharm

# 函数
"""
def 函数名()
    code
"""


# 函数的定义
def print_info():
    print("-" * 20)
    print("人生苦短，我用Python")
    print("-" * 20)


print_info()
print_info()


# 带参数的函数
def add_2_num(a, b):
    c = a + b
    print(c)


add_2_num(11, 11)


# 带返回值的函数
def add_num(a, b):
    return a + b


print(add_num(9, 9))


# 返回多个值的函数
def dived(a, b):
    x = a / b
    z = a % b
    return x, z


s, y = dived(5, 2)
print("商: %d, 余数: %d" % (s, y))
print(f"商:{s}, 余数: {y}")

# 全局变量和局部变量相同名字
a = 100


def test1():
    a = 300    # 局部变量优先使用，就近原则
    print(a)


def test2():
    print(a)   # 没有局部变量默认使用全局变量


# 在函数中修改全局变量
def test3():
    global a    # 申明全局变量在函数中的标识符
    a = 200


test1()
test2()
test3()
test2()

if __name__ == '__main__':
    print("hello world")
