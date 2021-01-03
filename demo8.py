# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 15:04
# @File : demo8.py
# @Software : PyCharm

# 元组
tup1 = ()  # 创建空的元组
# tup2 = (50) # 不是元组
print(type(tup1))
# print(type(tup2))

tup3 = (50,)
print(type(tup3))

tup = ("abc", "def", 2000, 2020)
print(tup[0])
print(tup[-1])
print(tup[1:5])

tupS = tup3 + tup
print(tupS)

# del tupS    # 删除整个元组变量
# print(tupS) # 会报错

# 字典
info = {"name": "吴彦祖", "age": 18}
print(info["name"])
# print(info["gender"])   # 直接访问会报错
print(info.get("gender", "m"))  # 没找到可以设定默认值

# 增
info["id"] = 20140310100125
print(info["id"])
# 删
print("删除前: %s" % info)
del info["name"]
print("删除后: %s" % info)
print("清空前: %s" % info)
info.clear()
print("清后: %s" % info)
# 改
info["name"] = "吴彦祖"
info["age"] = 20
print(info)
info["age"] = 18
print(info)
# 查
print(info.keys())  # 得到所有的键
print(info.values())  # 得到所有的值
print(info.items())  # 得到所有的项，每个键值对是一个元组

print("-" * 20)
for key in info.keys():
    print(info[key])
print("-" * 20)
for value in info.values():
    print(value)
print("-" * 20)
for key, value in info.items():
    print("key=%s value=%s" % (key, value))

# 使用枚举函数同时拿到列表中的下标和值
print("-" * 20)
myList = ["a", "b", "c", "d"]
for i, x in enumerate(myList):
    print("index=%s value=%s" % (i, x))

# 集合
print("-" * 20)
s = {1, 1, 2, 2, 3, 3}
print(s)
