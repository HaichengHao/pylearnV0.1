# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # def share_browser():
# #     options = Options()
# #     options.add_argument('--headless')
# #     options.add_argument('--disable-gpu')
# #
# #     # path是你自己的chrome浏览器的文件路径
# #     path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# #     options.binary_location = path
# #
# #     browser = webdriver.Chrome(options=options)
# #     return browser
# #
# #
# # browser = share_browser()
# #
# # url = 'https://www.baidu.com'
# #
# # browser.get(url)
# #
#
# import urllib.request
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrom_options=Options()
# chrom_options.add_argument(argument='--headless')
# chrom_options.add_argument(argument='--disable-gpu')
# path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrom_options.binary_location=path
#
# browser=webdriver.Chrome(options=chrom_options)
# url='https://www.baidu.com'
# browser.get(url)
# browser.save_screenshot('D:/pylearnV0.1/Data/BD.png')
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.binary_location=path

broswer=webdriver.Chrome(options=options)

url='https://www.baidu.com/'

broswer.get(url)
input=broswer.find_element(by='id',value='kw')
input.send_keys('周杰伦')
time.sleep(2)
bdys_button=broswer.find_element(by='id',value='su')
bdys_button.click()
time.sleep(2)

js_bottom='document.documentElement.scrollTop=100000'
broswer.execute_script(js_bottom)
time.sleep(2)
broswer.save_screenshot('D:/pylearnV0.1/Data/bd.png')