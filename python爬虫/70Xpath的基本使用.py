# editor hc
# date: 2023/2/28 10:45
from lxml import etree
# xpath有两种解析的文件
# 本地文件
# 服务器文件 response.read().decode('utf-8')

# 解析本地文件使用的是 etree.parse('文件路径')
# 解析服务器响应文件使用的是 etree.HTML(response.read().decode(utf-8))

tree=etree.parse('D:/pylearnV0.1/Data/70Xpath的基本使用.html')
print(tree)

#
# tree.xpath('xpath路径')
'''
1.路径查询
    // 查找所有子孙节点，不考虑层级关系
    / 找直接子节点
2.谓词查询
    //div[@id]
    //div[@id='maincontent']
3.属性查询
    //@class
4.模糊查询
    //div[contains(@id,'he')]
    //div[starts-with(@id,'he')]
    
5.内容查询
    //div/h1/text()
6.逻辑运算
    //div[@id='head' and @class="s_down"]
    //title | //price
'''

# 查找ul下面的li，text()获取内容
# 1.路径查询
#     // 查找所有子孙节点，不考虑层级关系
#     / 找直接子节点
li_list=tree.xpath('//ul/li/text()')
print(li_list)
# ['北京', '上海', '广州', '深圳']
# 判断列表的长度
print(len(li_list))
# 4

# 查找所有带id属性的标签
# text()获取标签中的内容
# 2.谓词查询
#     //div[@id]
#     //div[@id='maincontent']
li_list1=tree.xpath('//ul/li[@id]/text()')
print(li_list1)
# ['北京', '上海']
print(len(li_list1))
# 2

# 找到id为l1的标签,注意引号的问题，单引号里如果有字符串要写双引号
li_list2=tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list2)
# ['北京']

# 3.属性查询
# //@class

# 查找到id为l1的标签的属性值
li_list3=tree.xpath('//ul/li[@id="l1"]/@class')
print(li_list3)
# ['c1']


# 4.模糊查询
#     //div[contains(@id,'he')]
#     //div[starts-with(@id,'he')]

# 查找id里面包含l的li标签
li_list4=tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list4)
# ['北京', '上海']

# 查询id以c开头的li标签
li_list5=tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(li_list5)
# ['广州', '深圳']


# 6.逻辑运算
#     //div[@id='head' and @class="s_down"]
#     //title | //price

# 查询id为l1和class为c1的数据
li_list6=tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
print(li_list6)
# ['北京']

li_list7=tree.xpath('//ul/li[@id="l1"]/text()| //ul/li[@id="c3"]/text()')
print(li_list7)
# ['北京', '广州']
