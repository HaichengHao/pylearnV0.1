# editor hc
# date: 2023/2/26 17:25
import urllib.request
url='https://www.baidu.com'
# response=urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# print(content)
'''
<html>
<head>
	<script>
		location.replace(location.href.replace("https://","http://"));
	</script>
</head>
<body>
	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>
其实我们遇到了反扒，所以数据返回的不完整，我们可以通过用户代理来伪装'''


# 利用用户代理
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
# 因为urlopen()方法中不能存储字典，所以headers不能传进去
# 请求对象需要定制
# response=urllib.request.urlopen(url,headers) 还按以前这样写是不行的，因为headers必须是一个字符串或者是Request对象

'''
class Request:

    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
                 我们可以看到Request()中第二个参数是data,所以我们这次需要写上变量名
                 注意：因为参数顺序问题，不能直接写url和headers
                 '''


request=urllib.request.Request(url=url,headers=headers)#这次我们将headers也加入到请求当中
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)

