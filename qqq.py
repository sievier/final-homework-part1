# Python selenium http/socks5:

#coding=utf-8
import requests
from past.builtins import raw_input
from selenium import webdriver
from selenium.webdriver import Chrome
# 代理服务器

resp = requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=370000')
print(resp.text.split(':')[0])
print(resp.text.split(':')[1])
# proxyHost = resp.text.split(':')[0]
# print(type(resp.text.split(':')[0]))
# proxyPort = resp.text.split(':')[1]
# proxyType='socks5' #socks5
#
# # 代理隧道验证信息
# service_args = [
#     "--proxy-type=%s" % proxyType,
#     "--proxy=%(host)s:%(port)s" % {
#         "host" : proxyHost,
#         "port" : proxyPort,
#     }
#     ]

chrome_option = webdriver.ChromeOptions()
# 设置代理
chrome_option.add_argument("--proxy-server=http://"+resp.text)
print("--proxy-server=http://"+resp.text)
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://125.123.18.114:4226

# self.driver =
# self.driver.set_window_size(1440, 900)


# 要访问的目标页面
# targetUrl = "http://baidu.com"

driver = Chrome(executable_path=r'./chromedriver.exe',options=chrome_option)
# webdriver.PhantomJS()
# driver.get(targetUrl)

# print(driver.title)
# print(driver.page_source.encode("utf-8"))

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# baseurl = "http://www.ip.cn/"
# driver = webdriver.PhantomJS()

driver.get("http://www.ip.cn/")
print(driver.current_url) #获取当前页面的地址
print(driver.page_source.encode("utf-8"))  #获取当前页面的内容
# content = driver.find_element_by_id('result').text
# print(content)
# print(driver.find_element_by_id('result').text.split('\n')[1].split('位置：')[1])
#
# while True:
#     ip = raw_input('输入你要查询的IP地址:（输入Q退出）')
#     if ip == "Q":
#         break
#     targetUrl = baseurl + ip
#     driver.get(targetUrl)
#     content = driver.find_element_by_id('result').text
#     print(content)
#     print(driver.find_element_by_id('result').text.split('\n')[1].split('位置：')[1])
# driver.quit

# driver.quit()

