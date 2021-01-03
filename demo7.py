# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 14:16
# @File : demo7.py
# @Software : PyCharm

# 列表
nameList = []

nameList2 = ["小张", "小王", "小李"]
print(nameList2[0])
print(nameList2[1])
print(nameList2[2])

# 列表中可以存储混合类型
testList = [1, "测试"]
print(type(testList[0]))
print(type(testList[1]))

# 遍历
for name in nameList2:
    print(name)

i = 0
length = len(nameList2)
while i < length:
    print(nameList2[i])
    i += 1

# 增加
print("------增加前，名单列表的数据------")
for name in nameList2:
    print(name)
print("------增加后，名单列表的数据------")
nameList2.append("小胡")
for name in nameList2:
    print(name)

# 把列表作为元素追加
a = [1, 2]
b = [3, 4]
a.append(b)
print(a)

# 将b列表中的每个元素，逐一追加到a列表中
a.extend(b)
print(a)

# 第一个元素表示下标，第二个表示元素
a.insert(1, 3)
print(a)

# 删
print("------删除后，名单列表的数据------")
del nameList2[2]
for name in nameList2:
    print(name)

print("------弹出末尾最后一个元素后，名单列表的数据------")
nameList2.pop()
for name in nameList2:
    print(name)

# 从前往后删除第一个匹配的元素
nameList2.remove("小王")
print("------删除后，名单列表的数据------")
for name in nameList2:
    print(name)

# 改
print("------修改后，名单列表的数据------")
nameList2[0] = "小胡"
for name in nameList2:
    print(name)

# 查
findName = input("请输入你要查找的学生姓名")
if findName in nameList2:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")

# 左闭右开
a = ["a", "b", "c", "a", "b"]
print(a.index("a", 1, 4))
print(a.count("b"))

# 反转，排序
b = [1, 4, 2, 3]
print(b)
b.reverse()
print(b)

b.sort()
print(b)
b.sort(reverse=True)
print(b)
