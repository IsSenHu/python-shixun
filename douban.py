# -*- coding = utf-8 -*-
# @Author : 胡森
# @Time : 2021/1/4 10:39 上午
# @File : douban.py
# @Software : IntelliJ IDEA

import re
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

base_url = "https://movie.douban.com/top250"
start = 0
find_link = re.compile(r'<a href="(.*?)">')    # 创建正则表达式对象，表示规则
find_img_src = re.compile(r'class="" src="(.*?)" width="100"/>', re.S)  # re.S 让换行符包含在字符中
find_title = re.compile(r'<span class="title">(.*)</span>')
find_other = re.compile(r'<span class="other">(.*)</span>')
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_inq = re.compile(r'<span class="inq">(.*)</span>')
find_bd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 得到指定一个URL的网页内容
def ask_url(url):
    head = {
        # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def name_is_exists(tag):
    return tag.has_attr("name")


def get_data(base_url):
    data_list = []
    for i in range(0, 10):
        url = base_url + str(i * 25)
        html = ask_url(url)
        # 逐一解析数据
        # BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种:
        # Tag   标签及其内容：拿到它所找到的第一个内容
        # NavigableString   标签里的内容（字符串）
        # BeautifulSoup     表示整个文档
        # Comment           是一个特殊的NavigableString，输出的内容不包含注释符号
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            # print(item)
            data = []
            item = str(item)
            # 获取到影片详情的连接
            link = re.findall(find_link, item)[0]
            data.append(link)
            img_src = re.findall(find_img_src, item)[0]
            data.append(img_src)
            titles = re.findall(find_title, item)
            data.append(titles)
            other = re.findall(find_other, item)[0]
            data.append(other)
            rating = re.findall(find_rating, item)[0]
            data.append(rating)
            judge = re.findall(find_judge, item)[0]
            data.append(judge)
            inq = re.findall(find_inq, item)
            if inq:
                data.append(inq[0])
            else:
                data.append(" ")
            bd = re.findall(find_bd, item)[0]
            data.append(bd.strip())
            data_list.append(data)
        # print(type(bs.head))
        # print(type(bs.title.string))
        # print(bs.a.attrs)   # 获取标签的属性
        # print(bs.a.string)
        # # 文档的遍历
        # print(bs.head.contents)
        # # 文档的搜索
        # t_list = bs.find_all("a")   # 会查找与字符串完全匹配的内容
        # print(t_list)
        # # 正则表达式搜索
        # t_list = bs.find_all(re.compile("a"))
        # print("-" * 30)
        # print(t_list)
        # # 方法：传入一个函数，根据函数要求搜索
        # print("-" * 30)
        # t_list = bs.find_all(name_is_exists)
        # for item in t_list:
        #     print(item)
        # t_list = bs.find_all(id="inp-query")
        # for item in t_list:
        #     print(item)
        # t_list = bs.find_all(text=re.compile("\d"))
        # for item in t_list:
        #     print(item)
        # t_list = bs.find_all("a", limit=3)
        # for item in t_list:
        #     print(item)
        # css选择器
        # t_list = bs.select("title")
        # for item in t_list:
        #     print(item)
        # print("-" * 30)
        # t_list = bs.select(".mnav")
        # for item in t_list:
        #     print(item)
        # print("-" * 30)
        # t_list = bs.select("#inp-query")
        # for item in t_list:
        #     print(item)
        # print("-" * 30)
        # t_list = bs.select("input[name=search_text]")
        # for item in t_list:
        #     print(item)
        # print("-" * 30)
        # t_list = bs.select("head > title")
        # for item in t_list:
        #     print(item)
    return data_list


def main():
    data_list = get_data("https://movie.douban.com/top250?start=")
    print(data_list)


if __name__ == '__main__':
    # 调用函数
    main()
