import sys
import io
from selenium import webdriver
# usragent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码


#建立chrome浏览器对象，括号里是Chromedriver在你的电脑上的路径
browser = webdriver.Chrome('/Users/rockontrol/Desktop/daka/chromedriver')

#基本信息
xuehao = 'xxxx'
name = 'xxx'
password = 123456

#登录页面
url = 'https://wxyqfk.zhxy.net/?yxdm=14262#/login'
browser.set_window_size(598,702)
# 访问登录页面
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(5)

# print(browser.page_source.encode('utf-8').decode())
#定位输入框并输入相关信息
browser.find_elements_by_class_name("van-field__control")[0] .send_keys(xuehao)
browser.find_elements_by_class_name("van-field__control")[1] .send_keys(name)
browser.find_elements_by_class_name("van-field__control")[3] .send_keys(password)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)
browser.find_element_by_xpath('//button').click()
browser.implicitly_wait(3)

#地址重定向到登陆后页面
url2 = 'https://wxyqfk.zhxy.net/?yxdm=14262#/clockIn'
browser.set_window_size(598,702)
browser.get(url2)
browser.implicitly_wait(5)

#关闭有个温馨提示的框
browser.find_element_by_class_name('van-button').click()



# #输入用户名
# username = browser.find_element_by_name('user')
# username.send_keys('学号')
#
# #输入密码
# password = browser.find_element_by_name('pwd')
# password.send_keys('密码')
#
# #选择“学生”单选按钮
# student = browser.find_element_by_xpath('//input[@value="student"]')
# student.click()
#
# #点击“登录”按钮
# login_button = browser.find_element_by_name('btn')
# login_button.submit()
#
# #网页截图
# browser.save_screenshot('picture1.png')
# #打印网页源代码
# print(browser.page_source.encode('utf-8').decode())
#
# browser.quit()
