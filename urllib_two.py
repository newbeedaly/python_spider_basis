#-*- coding:utf-8 -*-
# 使用python的urllib库爬取百度首页的全部内容

import urllib.request

file = urllib.request.urlretrieve("http://www.imooc.com",filename="C:/Users/bpkj3/Desktop/python爬虫入门/imooc.html")

# 清除缓存
urllib.request.urlcleanup()

# url的编码解码
quote = urllib.request.quote("http://www.sina.com.cn")
print(quote)
unquote = urllib.request.unquote(quote)
print(unquote)


