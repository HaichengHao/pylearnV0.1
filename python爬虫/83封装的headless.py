from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def share_broswer():
    options=Options
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    options.binary_location(path)
    broswer=webdriver.Chrome(options=options)
    return broswer

broswer=share_broswer()
url='https://www.baidu.com'
broswer.get(url)
