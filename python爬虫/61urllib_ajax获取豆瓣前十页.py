# editor hc
# date:  '2023/2/27 13:39',
import urllib.request
import urllib.parse

def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'
    headers = {
        'Accept': '*/*',
        # 'Accept-Encoding':  'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'bid=ieseciCXnLQ; douban-fav-remind=1; ll="118237"; ap_v=0,6.0; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1677472667; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1677472667; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1677476745%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=c201698d0642f143.1646475606.4.1677476745.1677472713.; _pk_ses.100001.4cf6=*',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data={
        'start':(page-1)*20,
        'limit':20,
    }
    data=urllib.parse.urlencode(data)#<--get请求之后不需要再加encode()方法
    url=base_url+data
    request=urllib.request.Request(url=url,headers=headers)#get请求这里不写data
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content


def down_load(page,content):
    with open('D:/pylearnV0.1/Data/douban'+str(page)+'.json',mode='w',encoding='utf-8') as file:
        file.write(content)
# 主程序运行
if __name__ == '__main__':
    start_page=int(input('请输入起始的页码:'))
    end_page=int(input('请输入结束的页码:'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)# 调用creat_request()方法，每一页都有自己请求对象的定制
        content = get_content(request)#调用get_content方法，获取响应数据
        down_load(page,content)

