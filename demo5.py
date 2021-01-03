# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 11:28
# @File : demo5.py
# @Software : PyCharm

# i = 0
# while i < 10:
#     i = i + 1
#     print("-"*30)
#     if i == 5:
#         # 跳出整个循环
#         break
#     print(i)

i = 0
while i < 10:
    i = i + 1
    print("-"*30)
    if i == 5:
        # 结束本次循环，立即开始下次循环
        continue
    print(i)

# 打印九九乘法表
x = 1
y = 1
while x <= 9:
    while y <= x:
        print("%d * %d = %d" % (y, x, x * y), end="\t")
        y += 1
    print("")
    y = 1
    x += 1
