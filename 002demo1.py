# editor hc
# date: 2023/2/26 12:48
import urllib.request
import urllib.parse
url = 'https://www.shuwulou.cc/login.php?do=login'
data={'UserName':'nikofox','UserPwd':'HHCzio20.'}
# 发送请求
resp=urllib.request.urlopen(url,data= bytes(urllib.parse.urlencode(data),encoding='utf-8'))
# 响应内容
html=resp.read().decode('gbk')
print(html)