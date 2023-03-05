# editor hc
# date: 2023/3/2 22:10
'''
BeautifulSoup简称bs4
'''
import bs4
from bs4 import BeautifulSoup
# 通过解析本地文件，来对bs4进行讲解
soup=BeautifulSoup(open('D:/pylearnV0.1/python爬虫/75bs4.html', encoding='utf-8'), 'lxml')
print(soup)
# 解析服务器返回的内容为：Beautiful(response.read().decode,lxml)

# 根据标签查找各节点  ，注意，找到的是第一个符合条件的数据
print(soup.a)
# <a href="">码农1号</a>

# attrs是获取标签的属性以及属性的值
print(soup.a.attrs)
# {'href': '职业'}


# bs4的一些参数
# 1.find
print(soup.find('a'))
# <a href="职业">码农1号</a>
print(soup.find('a',title="a2"))
# <a href="坑爹的broswer" title="a2">百度</a>
print(soup.find('a',class_="a1"))

# 2.find_all ，返回的是一个列表
print(soup.find_all('a'))#返回的是所有的a标签
# [<a href="职业">码农1号</a>, <a href="坑爹的broswer">百度</a>]
# 获取所有的span
print(soup.find_all('span'))
# [<span>哈哈哈</span>]

# 获取所有a标签和span
print(soup.find_all(['a','span']))#<---返回所有的a标签和span，注意，返回是一个列表，所以要想一起输出，一定要把他们放入一个列表内
# [<a class="a1" href="职业">码农1号</a>, <span>哈哈哈</span>, <a href="坑爹的broswer" title="a2">百度</a>]

#limit的作用是查找前几个数据
print(soup.find_all('li',limit=2))
# [<li>张三</li>, <li>李四</li>]

# 3.select（‘推荐’）select返回的是一个列表，返回的是多个数据
print(soup.select('a')[1])
# <a href="坑爹的broswer">百度</a>
print(soup.select('a'))
# [<a class="a1" href="职业">码农1号</a>, <a href="坑爹的broswer" title="a2">百度</a>]

# 获取a1的属性，可以通过"."代表class,我们把这种操作叫类选择器
print('获取a1的属性')
print(soup.select('.a1'))
# [<a class="a1" href="职业">码农1号</a>]

print(soup.select('#l1'))
# [<li id="l1">张三</li>]


# 属性选择器 ---通过属性来获取对应的标签
# 查找到li标签中有id的标签
print(soup.select('li[id]'))
# [<li id="l1">张三</li>,<li id="l2">李四</li>]

# 查找到li标签中id为l2的标签
print(soup.select('li[id="l2"]'))
# [<li id="l2">李四</li>]

# 层级选择器

# 后代选择器
# 找到div下面的li
print(soup.select('div li'))
# [<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>]


# 子代选择器
# 某标签的第一级子标签
# 注意：很多的计算机编程语言中如果不加空格会报错，但bs4中不会报错
print(soup.select('div > ul > li'))
# [<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>]

# 找到a标签和li标签的所有对象
print(soup.select('a,li'))
# [<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>, <a class="a1" href="职业">码农1号</a>, <a href="坑爹的broswer" title="a2">百度</a>]



# 节点信息
# 获取节点内容
obj=soup.select('#d1')[0]
# print(obj.string)
# None <--注意，如果标签对象中只有内容，那么.string和get_text()都可以使用
# 但是，如果标签中除了内容还有标签，那么.string获取不到数据，而.gettext()可以
print(obj.get_text())
# geigeigei

# 节点的属性
obj1=soup.select('#p1')[0]
#.name获取的是标签的名字
print(obj1.name)
# p

#将属性值作为一个字典返回
# print(obj1.attrs)

# 获取节点的属性
obj2=soup.select('#p1')[0]
print(obj2.attrs.get('class'))
# ['p1']
print(obj2.get('class'))
# ['p1']
print(obj2['class'])
# ['p1']