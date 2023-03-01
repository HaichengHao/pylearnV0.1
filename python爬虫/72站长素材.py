# editor hc
# date: 2023/2/28 18:02

#//https://sc.chinaz.com/tupian/qinglvtupian_1.html #第一页的地址
# //https://sc.chinaz.com/tupian/qinglvtupian_2.html
# https://sc.chinaz.com/tupian/qinglvtupian_3.html
proxies_pool=[
    {'http': '114.233.71.160:9000'},
    {'http': '111.225.153.132:8089'},
    {'http': '180.105.117.139:8089'},
    {'http': '111.225.152.68:8089'},
    {'http': '36.138.56.214:3128'},
    {'http': '175.100.72.95:57938'},
    {'http': '198.199.74.99:59166'},
    {'http': '176.100.216.154:8087'},
    {'http': '4.16.68.158:443'},
    {'http': '161.35.70.249:8080'},
]

import urllib.request
import urllib.parse
import random
from lxml import etree
proxies=random.choice(proxies_pool)

def creat_request(page):
    if (page==1):
        url='https://sc.chinaz.com/tupian/qinglvtupian.html'

    else:
        url='https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'
    headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request


def get_content(request):
        handler=urllib.request.ProxyHandler(proxies=proxies)
        opener=urllib.request.build_opener(handler)
        response=opener.open(request)
        content=response.read().decode('utf-8')
        return content
def down_load(content):
    tree=etree.HTML(content)
    src_list=tree.xpath('//img/@data-original')
    picname_list=tree.xpath('//img/@alt')
    for i in range(len(picname_list)):
        name=picname_list[i]
        src=src_list[i]
        url='https:'+src
        # print(name,url)
        urllib.request.urlretrieve(url=url,filename='D:/pylearnV0.1/Data/'+name+'.jpg')


if __name__ == '__main__':
    start_page=int(input('请输入开始页:'))
    end_page=int(input('请输入结束页:'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)
        content=get_content(request)
        down_load(content)