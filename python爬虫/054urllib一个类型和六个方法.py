# editor hc
# date: 2023/2/26 16:24
import urllib.request
url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

# 一个类型和六个方法
print(type(response))
# <class 'http.client.HTTPResponse'>
# resoponse是HTTPResponse的类型

# 先不写解码的东西
# 按照一个字节一个字节去读
# content=response.read()
# print(content)

# content=response.read(5) #read(5)就是读五个字节
# print(content)

# content=response.readline() #readline()读取一行
# print(content)

# content=response.readlines() #按行读取
# print(content)

# 返回状态码
print(response.getcode())

# 返回url地址
print(response.geturl())

# 返回一些状态信息和响应头
print(response.getheaders())
