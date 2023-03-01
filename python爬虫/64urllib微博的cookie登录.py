# editor hc
# date: 2023/2/27 16:14
# 适用的场景，绕过登录，进入到某个页面

# 什么情况下访问不成功
# 请求头的信息不够，所以访问不成功

import urllib.request
import urllib.parse
url='https://weibo.cn/6451491586/info'
headers={
    # 带冒号的全都不好使
    # ':authority':' weibo.cn',
    # ':method':' GET',
    # ':path':' /6451491586/info',
    # ':scheme':' https',
    'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control':' max-age=0',
    # cookie中携带着信息，如果有登陆的cookie，那么我们就可以携带着cookie进入到登录之后的任何页面
    'cookie':' SUB=_2A25O-AUgDeRhGeFN71AX9yzNyD-IHXVqAqtorDV6PUJbkdANLXXMkW1NQDFRlWJ6AjLkl5MbV7JVU5Zq7wJ5x14h; _T_WM=11029437441; MLOGIN=1',
    'sec-ch-ua':' "Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' document',
    'sec-fetch-mode':' navigate',
    'sec-fetch-site':' none',
    'sec-fetch-user':' ?1',
    'upgrade-insecure-requests':' 1',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
}
# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)# get请求不写data
# 模拟浏览器发送请求
response=urllib.request.urlopen(request)
# 获取响应的数据
content=response.read().decode('utf-8')

# 尝试打印
print(content)

# 将数据保存到本地
with open('D:/pylearnV0.1/Data/weibo.html',mode='w',encoding='utf-8') as fp:
    fp.write(content)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 672: invalid start byte
# 报错了，被反扒了，检查确实是utf-8，因为并没有进入到个人信息页面，而是跳转到了登陆页面
# 那么登录页面不是utf-8