# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/4 3:55 下午
# @File : testRe.py
# @Software : PyCharm

import re

# 创建模式对象
pat = re.compile("AA")  # 此处的AA是正则表达式，用来验证其他的字符串
m = pat.search("CBA")
print(m)

m = pat.search("ABCAA")
print(m)

m = pat.search("AABCAACCAAA")   # search方法进行查找比对
print(m)

# 没有模式对象
m = re.search("asd", "Aasd")    # 前面的字符串是规则，后面的字符串是被校验的字符串
print(m)

print("-" * 60)

m = re.findall("a", "ASDaDFGAa")    # 前面的字符串是规则，后面的字符串是被校验的字符串
print(m)

m = re.findall("[A-Z]", "ASDaDFGAa")    # 表示找到A到Z之间的大写字母
print(m)

m = re.findall("[A-Z]+", "ASDaDFGAa")
print(m)

print("-" * 60)

m = re.sub("a", "A", "abcdcasd")    # 找到a用A替换，在第三个字符串中查找
print(m)

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)
