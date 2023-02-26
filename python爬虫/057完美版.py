# editor hc
# date: 2023/2/26 22:59
import urllib.request
import urllib.parse
url='https://www.baidu.com/s?wd='
name='周杰伦'
namecode=urllib.parse.quote(name)
url=url+namecode
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
