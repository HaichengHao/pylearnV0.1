# editor hc
# date: 2023/2/26 23:11
'''
解决多个参数的问题
urlencode:多个参数的时候
'''
import urllib.request
import urllib.parse
url='https://www.baidu.com/s?wd='
data={'wd':'周杰伦','sex':'男'}
newurl=urllib.parse.urlencode(data)
url=url+newurl
print(newurl)
print(urllib.parse.unquote(newurl))
# wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7
# wd=周杰伦&sex=男
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
