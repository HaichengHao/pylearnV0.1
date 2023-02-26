# editor hc
# date: 2023/2/26 10:30

'''
urllib.request : 用于打开和读取URL
urllib.error : 包含提出的异常urlib.request
urllib.parse : 用于解析URL
urllib.robotparser : 用于解析robots.txt文件
'''
import urllib.parse


kw = {'wd':'马士兵'}
# 编码
result=urllib.parse.urlencode(kw)
print(result)
# wd=%E9%A9%AC%E5%A3%AB%E5%85%B5
# https://cn.bing.com/search?q=%E9%A9%AC%E5%A3%AB%E5%85%B5%E6%95%99%E8%82%B2&form=ANNTH1&refig=7b01da15dde448a0be086108c0ea3cc7&sp=2&lq=0&qs=SC&pq=ma%27shi%27b&sk=PRES1SC1&sc=10-8&cvid=7b01da15dde448a0be086108c0ea3cc7

# 解码
print(urllib.parse.unquote(result))
# wd=马士兵
