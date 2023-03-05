# editor hc
# date: 2023/3/3 17:27
'''
selenium
是一种用于web程序测试的工具
测试直接运行在浏览器中，就像真正的用户操作一样
支持通过各种driver驱动真实浏览器完成测试
模拟浏览器功能，自动执行网页中的js代码，实现动态加载功能
'''
from selenium import webdriver #导入selenimu
import random
import urllib.request
from lxml import etree
url='https://www.jd.com/'
# 创建浏览器操作对象
path="D:/pylearnV0.1/chromedriver.exe" #<---浏览器文件驱动路径
broswer=webdriver.Chrome(path)
# 访问网址
broswer.get(url)
proxies_pool=[
    {'http': '117.57.118.185:8089'},
    {'http': '120.236.64.75:9002'},
    {'http': '123.182.58.30:8089'},
    {'http': '111.224.212.160:8089'},
    {'http': '36.6.158.26:8089'},
    {'http': '85.185.201.26:80'},
    {'http': '103.108.9.213	:8080'},
    {'http': '185.74.6.248:8080'},
    {'http': '34.66.5.144:8888'},
    {'http': '113.161.59.136:8080'},
]
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
proxies=random.choice(proxies_pool)
request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
# print(content)

# page_source获取网页源码
content2=broswer.page_source
print(content2)