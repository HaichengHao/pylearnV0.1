# editor hc
# date: 2023/2/27 19:09
import urllib.request
import urllib.parse
url='https://www.baidu.com/s?wd=ip'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
}
request=urllib.request.Request(url=url,headers=headers)
proxies={'http':'114.233.71.160 : 9000'}
# handler build_opener open
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
with open('D:/pylearnV0.1/Data/daili.html',mode='w',encoding='utf-8') as fp:
    fp.write(content)