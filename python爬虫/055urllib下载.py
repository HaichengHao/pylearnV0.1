# editor hc
# date: 2023/2/26 16:40
import urllib.request
# 下载一个网页,用urllib.request.urlretrieve(url,filename)
# url = 'http://www.baidu.com'
# urllib.request.urlretrieve(url,filename='D:/pylearnV0.1/python爬虫/baidu.html')


# 下载图片
# url='https://ts1.cn.mm.bing.net/th/id/R-C.4f4c44cbcb98f404a31919166addbe81?rik=ZKm31QXNsvshJA&riu=http%3a%2f%2fpic.qqbizhi.com%2fallimg%2fbbpic%2f92%2f992_7.jpg&ehk=8dwfkQ4VfH3ZSge9v8%2bm1n9jGn1y0hV8rhdhfm17Fwk%3d&risl=&pid=ImgRaw&r=0'
# urllib.request.urlretrieve(url,'D:/pylearnV0.1/python爬虫/1.jpeg')
# 下载一个视频

url = 'http://gossv.cfp.cn/videos/mts_videos/medium/temp/VCG42N1128920257.mp4'
urllib.request.urlretrieve(url,'D:/pylearnV0.1/python爬虫/video1.mp4')

