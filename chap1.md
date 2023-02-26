#第一章
##课程介绍  
1 urllib简介  
* urllib是Python自带的标准库中用于网络请求的库
* 通常用于爬虫开发、API、数据获取和测试
>urllib库的四大模块
>* urllib.request : 用于打开和读取URL
>>urllib.request库   
>>模拟浏览器发起一个http请求，并获取请求响应结果
>>>* urllib.request.urlopen的语法格式
urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)
>>>* 参数说明  
>>>* url:统一资源定位符
>>>* data:数据，默认值为none，urllib判断参数data是否为none从而区分请求方式，或参数data为none，则代表请求方式为get，反之为post，发送post请求，参数data以字典形式存储数据，并将参数data以字典类型转换成字节类型才能完成post请求
>>>* urlopen函数返回的结果是一个http.client.HTTPResponse对象
>* urllib.error : 包含提出的异常urlib.request  
>* urllib.parse : 用于解析URL
>* urllib.robotparser : 用于解析robots.txt文件  


2 发送请求    
3 ip代理  
4 使用cookie  
5 错误解析  
6 request库











