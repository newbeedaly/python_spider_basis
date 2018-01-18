# 对禁止爬取的网页爬取内容,如:csdn的博客

import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
# 方法一:使用build_opener()修改报头
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko)")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data=opener.open(url).read()

# 方法二：使用add_header()添加包头
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko)")
data=urllib.request.urlopen(req).read()

# 获取句柄,并写入文件中
fhandle=open("C:/Users/bpkj3/Desktop/python爬虫入门/blog.html","wb")
fhandle.write(data)
fhandle.close()