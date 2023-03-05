# editor hc
# date: 2023/3/2 10:14




proxies_pool=[
    {'http':'114.102.46.64:8089'},
    {'http':'125.65.40.199:12345'},
    {'http':'123.245.249.70	:8089'},
    {'http':'111.225.153.123:8089'},
    {'http':'222.190.208.191:8089'},
    {'http':'94.102.228.118:32650'},
    {'http':'103.163.231.218:8080'},
    {'http':'37.211.129.125:8080'},
    {'http':'103.46.11.182:8080'},
    {'http':'125.209.110.126:8080'}
]
import json
import jsonpath
import random
import urllib.request
import urllib.parse
proxies=random.choice(proxies_pool)

url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1677724038727_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers={
    # ':authority':' dianying.taobao.com',
    # ':method':' GET',
    # ':path':' /cityAction.json?activityId&_ksTS=1677724038727_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme':' https',
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'bx-v':'2.2.3',
    'cookie':'t=c2db7fb937c67b9a3fb644e60ad5b6d2; cna=XGCGHKsMexcCAd2wccrmBDCV; xlly_s=1; cookie2=1c8c566c1bb997a68a582c2c005ab47c; v=0; _tb_token_=5b5116413b375; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=c0RABecio0m0GloGasHuQeIhDRghZPaAjrsT6BrRFN6g0wPOiKdH9e7rhNSFD4C..; l=fBNSx2zVTQqev6DhBO5Iourza77T4IRb4oFzaNbMiIEGa6OCtFTD9NCsMfGMSdtjgTCcxeKrl5ZFzdLHR3AgCc0c07kqm08I3xvtaQtJe; isg=BCQkkP-uHJezV28knGktVS6o9SIWvUgnRpmRzj5Fa--y6cSzZ82ktxhHqUFxFYB_',
    'referer':'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112aRmBNzW&city=110100',
    'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'

}
request=urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content=response.read().decode('utf-8')
# print(content)
content=content.split(sep='(')[1].split(sep=')')[0]
print(content)
with open('D:/pylearnV0.1/Data/taopiaopiao.json',mode='w',encoding='utf-8') as fp:
    fp.write(content)
obj=json.load(open('D:/pylearnV0.1/Data/taopiaopiao.json','r',encoding='utf-8'))
regionname_list=jsonpath.jsonpath(obj,'$..regionName')
print(regionname_list)
