# editor hc
# date: 2023/2/27 8:04
import urllib.request
import urllib.parse
# post请求
url='https://fanyi.baidu.com/sug'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
data={
    'kw':'spider',

}
# post的请求一定要编码
data=urllib.parse.urlencode(data).encode('utf-8')
print(data)
'''
class Request:

    def __init__(self, url, data=None, headers={},  <--第二个参数是data
                 origin_req_host=None, unverifiable=False,
                 method=None):
                 '''
# post请求的参数必须要进行编码
request=urllib.request.Request(url=url,data=data,headers=headers)
# post的请求参数是不会拼接在url后边的而是需要放在请求对象定制的参数中
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
print(response)
# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
# 将data=urllib.parse.urlencode(data)改为data=urllib.parse.urlencode(data).encode('utf-8')

# 获取响应的数据
content=response.read().decode('utf-8')
print(type(content))
# <class 'str'>
# 将字符串转变为Jason对象
print(content)
import json
obj=json.loads(content)
print(obj)
# {'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'}, {'k': 'Spider', 'v': '[电影]蜘蛛'}, {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'}, {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'}, {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}]}


# post请求的参数必须进行编码
# 编码之后必须调用encode方法
# 参数是放在请求对象定制的方法中