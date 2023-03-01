# editor hc
# date: 2023/2/27 18:04
# 为什么要学习headler
'''
urllib.request.urlopen(url) <--不能定制请求头
urllib.request.Request(url,headers,data) <--可以定制请求头
Handler
    可以定制更高级的请求头（随着业务逻辑的复杂，请求对象的定制已经满足不了我们的需求，动态cookie和
    代理不能使用请求对象的定制）
'''

# 使用handler来访问百度，获取网页源码
import urllib.request
import urllib.parse
url='https://www.baidu.com'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
}
# data={
#
# }
request=urllib.request.Request(url=url,headers=headers)
# handler  build_opener open
# 1.获取handler对象
handler = urllib.request.HTTPHandler()
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用open方法
response=opener.open(request)

# response=urllib.request.urlopen()
content=response.read().decode('utf-8')
# with open('D:/pylearnV0.1/Data/')