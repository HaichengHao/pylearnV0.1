# editor hc
# date: 2023/2/27 19:59
proxies_pool=[
    {'http':'114.233.71.160:9000'},
    {'http':'111.225.153.132:8089'},
    {'http':'180.105.117.139:8089'},
    {'http':'111.225.152.68:8089'},
    {'http':'36.138.56.214:3128'},
    {'http':'175.100.72.95:57938'},
    {'http':'198.199.74.99:59166'},
    {'http':'176.100.216.154:8087'},
    {'http':'4.16.68.158:443'},
    {'http':'161.35.70.249:8080'},
]

import random
import urllib.request
proxies=random.choice(proxies_pool)
url='https://www.baidu.com/'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
}
request=urllib.request.Request(url=url,headers=headers)
handller=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handller)
response=opener.open(request)
content=response.read().decode('utf-8')
with open('D:/pylearnV0.1/Data/baidu.html',mode='w',encoding='utf8') as fp:
    fp.write(content)
