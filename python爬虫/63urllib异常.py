# editor hc
# date: 2023/2/27 15:59
import urllib.request
import urllib.parse

# url='https://www.狗蛋儿.com'
url = 'https://blog.csdn.net/m0_68111267/article/details/129038108'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
}
try:
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('你错了,HTTP错误。。。')
except urllib.error.URLError:
    print('链接写错了')