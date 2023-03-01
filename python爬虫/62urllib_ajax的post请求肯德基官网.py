# editor hc
# date: 2023/2/27 15:13
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 3
# pageSize: 10


import urllib.request
import urllib.parse


def creat_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname':'北京',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10',
    }
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
    }
    data=urllib.parse.urlencode(data).encode('utf-8')#post必须编码
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content


def down_load(page,content):
    with open('D:/pylearnV0.1/Data/kfc'+str(page)+'.json',mode='w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入起始页:'))
    end_page=int(input('请输入结束页:'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)
        content=get_content(request)
        down_load(page,content)
