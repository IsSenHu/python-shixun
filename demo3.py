# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/3 10:53
# @File : demo3.py
# @Software : PyCharm

# if True:
#     print("True")
#     print("Answer")
# else:
#     print("False")
# print("end")
import random

score = 77
if 90 <= score <= 100:
    print("本次考试，等级为A")
elif 80 <= score < 90:
    print("本次考试，等级为B")
elif 70 <= score < 80:
    print("本次考试，等级为C")
else:
    print("本次考试，等级为E")

x = random.randint(0, 2)    # 随机生成[0, 2]的随机数，0、1、2
print(x)
