# editor hc
# date: 2023/2/26 11:47
# urllib.request : 用于打开和读取URL
'''
urllib.request.urlopen的语法格式 urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)
参数说明
url:统一资源定位符
data:数据，默认值为none，urllib判断参数data是否为none从而区分请求方式，或参数data为none，则代表请求方式为get，反之为post，发送post请求，参数data以字典形式存储数据，并将参数data以字典类型转换成字节类型才能完成post请求
urlopen函数返回的结果是一个http.client.HTTPResponse对象
'''
import urllib.request
# print(urllib.request.urlopen('https://www.bing.com').read())
url = 'https://www.ldkxs.org/'
# 发送请求
resp=urllib.request.urlopen(url)
html = resp.read().decode('gbk') #decode()可以将二进制类型转化为字符串类型++
# 以下几段代码纯属是重新回忆V0.0内容
with open('D:/pylearnV0.1/test.txt','w') as file:
    file.write(html)
print(html)

