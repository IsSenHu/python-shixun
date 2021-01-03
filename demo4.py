# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 11:14
# @File : demo4.py
# @Software : PyCharm

# 前闭后开
for i in range(5):
    print(i)

for i in range(0, 11, 3):   # 从0开始到11结束，步进值为3
    print(i)

for i in range(-10, -100, -3):
    print(i)

name = "chengdu"
for x in name:
    print(x, end="\t")

a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i])

# while
i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i + 1))
    print("i=%d" % i)
    i += 1

# 1-100求和
n = 100
y = 0
x = 1
while x <= n:
    y += x
    x += 1
print(y)

# while和else配合使用
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "等于5")
