# editor hc
# date: 2023/2/26 15:50
# 使用urllib来获取百度首页的代码
import urllib.request
import urllib.parse
import sys
url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 获取响应中的页面的源码
# read()方法 ，返回的是二进制的内容
# 我们要将二进制的数据转换为字符串
content=response.read()

# 二进制->字符串
html=content.decode('utf-8')



# 回忆一波文件写入
'''
with open('D:/pylearnV0.1/python爬虫/demo.html','w') as newfile :
    newfile.write(html)
'''


# 打印数据
print(html)