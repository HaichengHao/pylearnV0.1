# editor hc
# date: 2023/3/4 10:22
import urllib.request
from selenium import webdriver
import random
from lxml import etree
url='https://www.baidu.com/'
path='D:/pylearnV0.1/chromedriver.exe'
broswer=webdriver.Chrome(path)
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
proxies=random.choice(proxies_pool)
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

}
request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
# 找到类名为su的类
input=broswer.find_element_by_id('su')
# 找到类名为su的属性值
print(input.get_attribute('class'))
# bg s_btn

# 获取su类的标签名
print(input.tag_name)
# input

# 获取元素文本
a=broswer.find_element_by_link_text('新闻')
print(a.text)