import time

import requests
from selenium.webdriver import Chrome

from selenium import webdriver
import warnings


# import time
#
# from selenium import webdriver
#
# chromeOptions = webdriver.ChromeOptions()
#
# # 设置代理
# chromeOptions.add_argument("--proxy-server=http://ip:port")
# # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
# browser = webdriver.Chrome(chrome_options=chromeOptions)
#
# # 查看本机ip，查看代理是否起作用
# browser.get("https://www.baidu.com/")
# time.sleep(20)
# print(browser.page_source)
#
# # 退出，清除浏览器缓存
# browser.quit()

warnings.filterwarnings("ignore")
import pandas as pd

url = 'https://www.sogou.com/sogou?interation=1728053249&interV=&pid=sogou-wsse-c7dec8e09376bf8e&query=疫情感染&page={}&ie=utf8'

driver = Chrome('./chromedriver')


def get_driver():
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
    # print(driver.page_source.encode("utf-8"))  #获取当前页面的内容
    return driver



href_list = []
topic_list = []
time_list = []
laiyuan_list = []

# 获取不同页数的网页信息
def next_page(page):
    # 解决加载超时出错

    try:


        driver.get(url.format(str(page)))
        time.sleep(1)
    except TimeoutError:
        return print("TimeoutError")


# 获取网页信息
def get_urls():
    try:
        main = driver.find_element_by_class_name("results")

        for context in main.find_elements_by_class_name("vrwrap"):
            url = []
            title = context.find_element_by_class_name("vr-title")
            href = title.find_element_by_tag_name("a").get_attribute("href")  # 链接
            topic = title.text  # 标题

            time1 = context.find_element_by_class_name("fz-mid").find_elements_by_tag_name("span")
            laiyuan = time1[0].text  # 新闻来源
            time2 = time1[1].text  # 时间

            url.append(href)
            url.append(topic)
            url.append(time2)
            url.append(laiyuan)
            # print(url)  # 显示当前新闻内容

            href_list.append(href)
            topic_list.append(topic)
            time_list.append(time2)
            laiyuan_list.append(laiyuan)

    except Exception as err:
        print("未爬取成功：", err)
        time.sleep(10)

f = 1 

def main():
    global f
    global driver
    driver.close()
    driver = get_driver()
    for i in range(1, 100):
        # if(i!=1):driver.quit()
        if(i%20==0):
            driver.close()
            driver = get_driver()
            dframe = pd.DataFrame({'链接': href_list, '主题': topic_list, '时间': time_list, '来源': laiyuan_list})
            dframe.to_csv('sougou_urls.csv', index=False, sep=',', encoding='utf_8_sig')
        # if(f==1):
        #     driver1.quit()
        #     if(i%1==0): driver2 = get_driver()
        #     driver = driver2
        #     f = 0
        # else:
        #     driver2.quit()
        #     if (i % 1 == 0): driver1 = get_driver()
        #     driver = driver1
        #     f = 1

        next_page(i)
        print("爬取第{}页内容".format(i))
        get_urls()

    driver.quit()
    print("爬取搜狗新闻完成！")


if __name__ == '__main__':
    main()


# import time
#
# from selenium import webdriver
#
# chromeOptions = webdriver.ChromeOptions()
#
# # 设置代理
# chromeOptions.add_argument("--proxy-server=http://ip:port")
# # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
# browser = webdriver.Chrome(chrome_options=chromeOptions)
#
# # 查看本机ip，查看代理是否起作用
# browser.get("https://www.baidu.com/")
# time.sleep(20)
# print(browser.page_source)
#
# # 退出，清除浏览器缓存
# browser.quit()


# #coding=utf-8
# import requests
#
# #请求地址
# targetUrl = "https://www.baidu.com"
#
# #代理服务器
# proxyHost = "ip"
# proxyPort = "port"
#
# proxyMeta = "http://%(host)s:%(port)s" % {
#
#     "host" : proxyHost,
#     "port" : proxyPort,
# }
#
# #pip install -U requests[socks]  socks5
# # proxyMeta = "socks5://%(host)s:%(port)s" % {
#
# #     "host" : proxyHost,
#
# #     "port" : proxyPort,
#
# # }
#
# proxies = {
#
#     "http"  : proxyMeta,
#     "https"  : proxyMeta
# }
#
# resp = requests.get(targetUrl, proxies=proxies)
# print resp.status_code
# print resp.text