# editor hc
# date: 2023/3/4 18:28
'''
什么是phantomjs
是一个无界面浏览器
支持页面元素的查找，js的执行
由于不运行css和gui渲染，运行效率要比真实的浏览器快很多
如何使用？
获取PhantomJS.exe文件路径path
broswer=webdriver.PhantomJS(path)
broswer.get(url)
扩展：保存屏幕快照:broswer.save_screenshot('baidu.jpg')
'''
from selenium import webdriver
import urllib.request
import time
import random
from lxml import etree
url='https://www.baidu.com'
path='D:/pylearnV0.1/phantomjs.exe'
broswer=webdriver.PhantomJS(path)
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

# broswer.save_screenshot('D:/pylearnV0.1/Data/baidu.png')

time.sleep(2)
input=broswer.find_element_by_id("kw")
input.send_keys("周杰伦")
time.sleep(2)
bdys_button=broswer.find_element_by_id("su")

# 点击百度一下
bdys_button.click()
js_bottom='document.documentElement.scrollTop=100000'
broswer.execute_script(js_bottom)

broswer.save_screenshot('D:/pylearnV0.1/Data/jaychou.png')