# editor hc
# date: 2023/2/26 21:49
# https://www.baidu.com/s?wd=周杰伦
# import urllib.request
# import urllib.parse
# url='https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6' #<--unicode编码
# nurl=urllib.parse.unquote(url)
# print(nurl)
# # https://www.baidu.com/s?wd=周杰伦

# url='https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
import urllib.request
import urllib.parse
# 设置ua
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
# kw={'name':'周杰伦'}
# namecode=urllib.parse.urlencode(kw)
# print(namecode)
# name=%E5%91%A8%E6%9D%B0%E4%BC%A6


# 对请求对象的定制
name='周杰伦'
namecode=urllib.parse.quote(name)
print(namecode)
# %E5%91%A8%E6%9D%B0%E4%BC%A6
url='https://www.baidu.com/s?wd='
url=url+namecode
request=urllib.request.Request(url=url,headers=headers)
# 模拟器向浏览器发送请求
respond=urllib.request.urlopen(request)
# 获取响应的内容并打印
content=respond.read().decode('utf-8')
print(content)
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
# 但我们将url改为'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'便能成功打印



