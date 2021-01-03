# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 13:52
# @File : demo6.py
# @Software : PyCharm

# 单引号
word = '字符串'
# 双引号
sentence = "这是一个句子"
# 三引号
paragraph = """
        这是一个段落
        可以由多行组成
"""

print(word)
print(sentence)
print(paragraph)

my_str = "I'm a student"
print(my_str)

# 转义
my_str2 = 'I\'m a student'
print(my_str2)

cd = "chengdu"
print(cd[0])    # [起始位置:结束位置:步进值]
print(cd[0:5])
print(cd[1:7:2])
print(cd[:5])
print(cd + ",你好")
print(cd * 3)
print("hello\nchengdu")
# 不进行转义
print(r"hello\nchengdu")