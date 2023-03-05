# editor hc
# date: 2023/3/3 21:27
# import urllib.request
# import random
# from selenium import webdriver
# proxies_pool=[
#     {'http': '117.57.118.185:8089'},
#     {'http': '120.236.64.75:9002'},
#     {'http': '123.182.58.30:8089'},
#     {'http': '111.224.212.160:8089'},
#     {'http': '36.6.158.26:8089'},
#     {'http': '85.185.201.26:80'},
#     {'http': '103.108.9.213	:8080'},
#     {'http': '185.74.6.248:8080'},
#     {'http': '34.66.5.144:8888'},
#     {'http': '113.161.59.136:8080'},
# ]
# path="D:/pylearnV0.1/chromedriver.exe"
# broswer=webdriver.Chrome(path)
# url='https://www.jd.com/'
# broswer.get(url)
# proxies=random.choice(proxies_pool)
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
# }
# request=urllib.request.Request(url=url,headers=headers)
# handler=urllib.request.ProxyHandler(proxies=proxies)
# opener=urllib.request.build_opener(handler)
# response=opener.open(request)
#
# content=broswer.page_source
# print(content)

import urllib.request
from selenium import webdriver
path='D:/pylearnV0.1/chromedriver.exe'
broswer=webdriver.Chrome(path)
url='https://www.baidu.com/'
broswer.get(url)
# content=broswer.page_source
# print(content)

# 元素定位

# 根据id来找到对象
button=broswer.find_element_by_id('su')
print(button)

#根据标签属性的属性值来获取对象
button1=broswer.find_element_by_name('wd')
print(button1)

#根据xpath语句来获取对象
button2=broswer.find_elements_by_xpath('//input[@id="su"]') #<---返回多个值的时候就写成'elements'
print(button2)

# 根据标签的名字获取对象
button3=broswer.find_element_by_tag_name('input')
# button3=broswer.find_element(by='tag name',value='input') #<--这里只是用了新版本的语法
print(button3)

#使用bs4的语法来获取对象
button4=broswer.find_element_by_css_selector('#su')
print(button4)

#
button5=broswer.find_element_by_link_text('视频')
print(button5)
'''
2023/3/4 加强语法记忆
from selenium import webdriver
import urllib.request
url=''
path='D:/pylearnV0.1/chromedriver.exe'
broswer=webdriver.Chrome(path)
broswer.get(url)'''