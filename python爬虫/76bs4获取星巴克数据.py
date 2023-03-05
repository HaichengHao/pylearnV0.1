# editor hc
# date: 2023/3/3 9:29
from bs4 import BeautifulSoup
import random
import urllib.request
from lxml import etree
proxies_pool=[
    {'http':'117.57.118.185:8089'},
    {'http':'120.236.64.75:9002'},
    {'http':'123.182.58.30:8089'},
    {'http':'111.224.212.160:8089'},
    {'http':'36.6.158.26:8089'},
    {'http':'85.185.201.26:80'},
    {'http':'103.108.9.213	:8080'},
    {'http':'185.74.6.248:8080'},
    {'http':'34.66.5.144:8888'},
    {'http':'113.161.59.136:8080'},

]
proxies=random.choice(proxies_pool)
url='https://www.starbucks.com.cn/menu/'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

}

request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)

content=response.read().decode('utf-8')
# print(content)
# 以下几行完全是为了闪回一下xpath的使用，怕忘。。。。
# tree=etree.HTML(content)
# result=tree.xpath('//strong/text()')
# print(result)

# Beautiful获取服务器文件就是Beautiful(response.read().decode(),'lxml')
soup=BeautifulSoup(content,'lxml')
name_list=soup.select('ul[class="grid padded-3 product"] strong')

print(name_list)
# print(result)
for item in name_list:
    print(item.string)
    # 或 print(item.get_text())