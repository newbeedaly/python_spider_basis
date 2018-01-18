#-*- coding:utf-8 -*-
# 使用python的urllib库爬取百度首页的全部内容

import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

# file文件的一些常见属性
print(file.info())
print(file.getcode())
print(file.geturl())

# 爬取全部内容
data = file.read()
# 爬去一行内容
# dataline = file.readline()
# 一般放入一个list列表中
# datalines = file.readlines()
# 打印
# print(data)

fhandle=open("C:/Users/bpkj3/Desktop/python爬虫入门/baidu.html","wb")
fhandle.write(data)
fhandle.close()
