# editor hc
# date: 2023/2/27 12:27
# 获取豆瓣电影第一页的数据并保存起来
import urllib.request
import urllib.parse
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'
headers={
    'Accept':  '*/*',
    # 'Accept-Encoding':  'gzip, deflate, br',
    'Accept-Language':  'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':  'keep-alive',
    'Cookie':  'bid=ieseciCXnLQ; douban-fav-remind=1; ll="118237"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1677471669%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1677472667; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1677472667; _pk_id.100001.4cf6=c201698d0642f143.1646475606.3.1677472713.1677378452.',
    'Host':  'movie.douban.com',
    'Referer':  'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
    'sec-ch-ua':  '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile':  '?0',
    'sec-ch-ua-platform':  '"Windows"',
    'Sec-Fetch-Dest':  'empty',
    'Sec-Fetch-Mode':  'cors',
    'Sec-Fetch-Site':  'same-origin',
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56',
    'X-Requested-With':  'XMLHttpRequest',
}

# data={
# }
# data=urllib.parse.urlencode(data).encode('utf-8')
# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
# 获取响应的数据
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
# import json
# obj=json.loads(content)
# print(obj)
# 数据下载到本地
# open方法默认使用的是'gbk',如果我们想保存汉字，就需要在open方法中指定编码格式为'utf-8'
with open('D:/pylearnV0.1/Data/douban.json',mode='w',encoding='utf-8') as file:
    file.write(content)
    # json保存后可以通过快捷键'ctrl+alt+l'来快速格式