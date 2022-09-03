#coding=utf-8
import requests
from past.builtins import raw_input
from selenium import webdriver
from selenium.webdriver import Chrome
# 代理服务器
resp = requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=370000')
print(resp.text.split(':')[0])
print(resp.text.split(':')[1])
chrome_option = webdriver.ChromeOptions()
# 设置代理
chrome_option.add_argument("--proxy-server=http://"+resp.text)
print("--proxy-server=http://"+resp.text)
driver = Chrome(executable_path=r'./chromedriver.exe',options=chrome_option)
driver.get("http://www.ip.cn/")
print(driver.current_url) #获取当前页面的地址
print(driver.page_source.encode("utf-8"))  #获取当前页面的内容


