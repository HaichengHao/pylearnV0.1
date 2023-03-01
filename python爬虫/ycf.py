# editor hc
# date:  '2023/2/27 13:39',
proxies_pool=[
    {'http':'114.233.71.160:9000'},
    {'http':'111.225.153.132:8089'},
    {'http':'180.105.117.139:8089'},
    {'http':'111.225.152.68:8089'},
    {'http':'36.138.56.214:3128'},
    {'http':'175.100.72.95:57938'},
    {'http':'198.199.74.99:59166'},
    {'http':'176.100.216.154:8087'},
    {'http':'4.16.68.158:443'},
    {'http':'161.35.70.249:8080'},
]
from  lxml import etree
import urllib.request
import urllib.parse
import random
proxies=random.choice(proxies_pool)
def creat_request(page):
    base_url='https://movie.douban.com/subject/35267208/comments?'
    # https://movie.douban.com/subject/35267208/comments?comment_id=3649271279
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'

    }
    data={
        'start':(page-1)*20,
        'limit':'500',
        'status':'F',
        'sort':'new_score',
    }
    data=urllib.parse.urlencode(data)#<--get请求之后不需要再加encode()方法
    url=base_url+data
    request=urllib.request.Request(url=url,headers=headers)#get请求这里不写data
    return request

def get_content(request):
    handller = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handller)
    response = opener.open(request)
    # response=urllib.request.urlopen(request)

    tree=etree.HTML(response.read().decode('utf-8'))
    result=tree.xpath('//span[@class="short"]/text()')
    return result


def down_load(page,result):
    with open('D:/pylearnV0.1/YCF/doubancomment'+str(page)+'txt',mode='w',encoding='utf-8') as file:
        file.write(str(result))
# 主程序运行
if __name__ == '__main__':
    start_page=int(input('请输入起始的页码:'))
    end_page=int(input('请输入结束的页码:'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)# 调用creat_request()方法，每一页都有自己请求对象的定制
        content = get_content(request)#调用get_content方法，获取响应数据
        down_load(page,content)

