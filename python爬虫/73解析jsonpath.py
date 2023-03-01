# editor hc
# date: 2023/3/1 23:41
import json
import jsonpath
obj=json.load(open('store.json','r',encoding='utf-8'))
print(obj)
# {'store': {'book': [{'category': '修真', 'author': '六道', 'title': '坏蛋是怎样练成的', 'price': 8.95}, {'category': '修改', 'author': '天蚕土豆', 'title': '斗破苍穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰变', 'isbn': '0-395-19395-8', 'price': 22.99}], 'bicycle': {'color': '黑色', 'price': 19.95}}}

# 书店所有书的作者
author_list=jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author_list)
# ['六道', '天蚕土豆', '唐家三少', '南派三叔']

# 所有的作者
alauthor_list=jsonpath.jsonpath(obj,'$..author')
print(alauthor_list)

# store下面的所有元素
tag_list=jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)
# [[{'category': '修真', 'author': '六道', 'title': '坏蛋是怎样练成的', 'price': 8.95}, {'category': '修改', 'author': '天蚕土豆', 'title': '斗破苍穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰变', 'isbn': '0-395-19395-8', 'price': 22.99}], {'author': '南派三叔', 'color': '黑色', 'price': 19.95}][[{'category': '修真', 'author': '六道', 'title': '坏蛋是怎样练成的', 'price': 8.95}, {'category': '修改', 'author': '天蚕土豆', 'title': '斗破苍穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰变', 'isbn': '0-395-19395-8', 'price': 22.99}], {'author': '南派三叔', 'color': '黑色', 'price': 19.95}]

# store里边所有的价格(price)
price_list=jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# 第三本书
third_book=jsonpath.jsonpath(obj,'$.store.book[2].title')
print(third_book)
# ['斗罗大陆']

# 最后一本书
final_book=jsonpath.jsonpath(obj,'$..book[(@.length-1)].title')
print(final_book)
# ['星辰变']

# 前两本书
rank12_book=jsonpath.jsonpath(obj,'$..book[0,1].title')
# 或者写成rank12_book=jsonpath.jsonpath(obj,'$..book[:2].title')
print(rank12_book)
# ['坏蛋是怎样练成的', '斗破苍穹']

# 找到包含版本号的书  ,条件过滤需要在圆括号前加一个问号
vernum_book=jsonpath.jsonpath(obj,'$..book[?(@.isbn)].title')
print(vernum_book)
# ['斗罗大陆', '星辰变']

# 哪本书超过了10块
pricemt10=jsonpath.jsonpath(obj,'$..book[?(@.price>10)].title')
print(pricemt10)
# ['斗破苍穹', '星辰变']