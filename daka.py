import sys
import io
from selenium import webdriver
import time
import requests
import base64

# usragent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 建立chrome浏览器对象，括号里是Chromedriver在你的电脑上的路径，需要修改
browser = webdriver.Chrome('/Users/rockontrol/Desktop/daka/chromedriver')

# 基本信息，需要修改
xuehao = '20171818'
name = '马清杰'
password = '158314'

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


but = browser.find_element_by_class_name("van-button")
browser.execute_script("arguments[0].click();", but)


try:
    wenxintishi=browser.find_element_by_class_name('van-button')
    print('find')
    wenxintishi.click()
except:
    time.sleep(2)
    print('not find')
    # browser.get(url2)


try:
    browser.find_element_by_class_name('sign-in-btn')
    print('跳转成功')
    browser.find_element_by_class_name('sign-in-btn')

except:
    print('跳转失败，重新跳转')
    browser.get(url2)
    time.sleep(3)
    browser.find_element_by_class_name('sign-in-btn')
    browser.find_element_by_class_name('van-button').click()

# 关闭有个温馨提示的框
try:
    wenxintishi=browser.find_element_by_class_name('van-button')
    print('find')
    wenxintishi.click()
except:
    time.sleep(2)
    print('not find')
    # browser.get(url2)

time.sleep(3)



time.sleep(3)
browser.find_element_by_class_name('sign-in-btn').click()
browser.find_elements_by_xpath('//label')[0].click()
browser.find_elements_by_xpath('//label')[6].click()
browser.find_elements_by_xpath('//label')[14].click()

time.sleep(2)

image = browser.find_element_by_tag_name('img').get_attribute('src')
print(image)

# print(image.split(',')[1])
try :
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print('gun')
except:
    pass
#保存验证码到本地
#from yanzhnegma import base64change
#base64change(image)


