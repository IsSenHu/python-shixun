# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/4 1:04 下午
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request, urllib.parse

# 获取一个get请求
response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))

# 获取一个post请求
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
print(response.status)
print(response.getheaders())
print(response.getheader("Content-Type"))

# 伪装是一个浏览器
url = "https://www.douban.com"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/87.0.4280.88 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
