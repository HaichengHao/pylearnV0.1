# editor hc
# date: 2023/3/4 11:05
'''
点击:click()
输入:send_keys()
后退操作:browser.back()
前进操作:browser.forword()

'''
from selenium import webdriver
import urllib.request
import random
from lxml import etree
import time
# 创建浏览器对象
path='D:/pylearnV0.1/chromedriver.exe'
broswer=webdriver.Chrome(path)
url='https://www.baidu.com'
broswer.get(url)
# # 睡眠两秒
# time.sleep(2)
# # 获取文本框的对象
# input=broswer.find_element_by_id('kw')
# # 在文本框中输入’周杰伦‘
# input.send_keys('周杰伦')
# time.sleep(2)
# # 定位到’百度一下‘
# button=broswer.find_element_by_id('su')
# # 点击’百度一下‘
# button.click()
# time.sleep(2)
# # 滑动到底部
# js_bottom='document.documentElement.scrollTop=100000'
# broswer.execute_script(js_bottom)
# time.sleep(2)
# # 点击下一页
# nxtpage_button=broswer.find_element_by_class_name('n')
# nxtpage_button.click()
# time.sleep(2)
# # 滑动到底部
# broswer.execute_script(js_bottom)
# time.sleep(2)
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
broswer.get(url)
# 睡眠两秒
time.sleep(2)
# 获取文本框的对象
input=broswer.find_element_by_id('kw')
# 在文本框中输入’周杰伦‘
input.send_keys('周杰伦')
time.sleep(2)
# 定位到’百度一下‘
button=broswer.find_element_by_id('su')
# 点击’百度一下‘
button.click()
time.sleep(2)
# 滑动到底部
js_bottom='document.documentElement.scrollTop=100000'
broswer.execute_script(js_bottom)
time.sleep(2)
# 点击下一页
nxtpage_button=broswer.find_element_by_class_name('n')
nxtpage_button.click()
time.sleep(2)
# 滑动到底部
broswer.execute_script(js_bottom)
time.sleep(2)
# 获取下一页的按钮，不过这次用find_element_by_xpath来实现
nxtpage_button2=broswer.find_element_by_xpath('//a[@class="n"]')
# 点击下一页
nxtpage_button2.click()
time.sleep(2)
# 滑动到底部
broswer.execute_script(js_bottom)
time.sleep(2)

# 回到上一页
broswer.back()
time.sleep(2)

# 又回到刚才那一页
broswer.forward()
time.sleep(3)

# 退出
broswer.quit()