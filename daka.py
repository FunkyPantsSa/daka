import sys
import io
from selenium import webdriver
import time
import requests

# usragent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 建立chrome浏览器对象，括号里是Chromedriver在你的电脑上的路径，需要修改
browser = webdriver.Chrome('/Users/rockontrol/Desktop/daka/chromedriver')

# 基本信息，需要修改
xuehao = 'xxxx'
name = 'xxx'
password = 'xxxx'

# 登录页面
url = 'https://wxyqfk.zhxy.net/?yxdm=14262#/login'
browser.set_window_size(598, 702)
# 访问登录页面
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(5)
time.sleep(3)
# print(browser.page_source.encode('utf-8').decode())
# 定位输入框并输入相关信息
browser.find_elements_by_class_name("van-field__control")[0].send_keys(xuehao)
browser.find_elements_by_class_name("van-field__control")[1].send_keys(name)
browser.find_elements_by_class_name("van-field__control")[3].send_keys(password)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)
# browser.sleep(3)
browser.find_element_by_xpath('//button').click()
browser.implicitly_wait(3)

# 地址重定向到登陆后页面
url2 = 'https://wxyqfk.zhxy.net/?yxdm=14262#/clockIn'
browser.set_window_size(598, 702)
browser.get(url2)
browser.implicitly_wait(10)

# 关闭有个温馨提示的框
browser.find_element_by_class_name('van-button').click()
time.sleep(3)
browser.find_element_by_class_name('sign-in-btn').click()
browser.find_elements_by_xpath('//label')[0].click()
browser.find_elements_by_xpath('//label')[6].click()
browser.find_elements_by_xpath('//label')[14].click()

time.sleep(2)

# image = browser.find_element_by_tag_name('img').get_attribute('src')
# print(image)
# # 通过requests发送一个get请求到图片地址，返回的响应就是图片内容
# r = requests.get(image)
#
# # 将获取到的图片二进制流写入本地文件
# with open('yanzheng.png', 'wb') as f:
#     # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入png中
#     f.write(r.content)

