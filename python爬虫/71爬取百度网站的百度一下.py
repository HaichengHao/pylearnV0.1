# editor hc
# date: 2023/2/28 15:39

# 获取源码
# 解析服务器响应的文件
# 地址池
proxies_pool=[
    {'http': '114.233.71.160:9000'},
    {'http': '111.225.153.132:8089'},
    {'http': '180.105.117.139:8089'},
    {'http': '111.225.152.68:8089'},
    {'http': '36.138.56.214:3128'},
    {'http': '175.100.72.95:57938'},
    {'http': '198.199.74.99:59166'},
    {'http': '176.100.216.154:8087'},
    {'http': '4.16.68.158:443'},
    {'http': '161.35.70.249:8080'},
]


import random
import urllib.request
from lxml import etree
proxies=random.choice(proxies_pool)
url='https://www.baidu.com/'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器访问服务器
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
# response=urllib.request.urlopen(request)
# content=response.read().decode('utf-8')
#
# 获取网页源码
content=response.read().decode('utf-8')

# 解析服务器响应的文件
tree=etree.HTML(content)

# 获取我们想要的数据
result=tree.xpath('//input[@id="su"]/@value')


print(result)
# ['百度一下']
# xpath返回值是一个列表
# 我们可以通过按照访问列表下标的方式来返回列表里的内容
print(result[0])
# 百度一下