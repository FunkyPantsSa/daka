# from yanzhnegma import base64change
url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAeCAYAAAC7Q5mxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKNSURBVGhD7Zc9csMgEEZ1PA6kA7jPAdxQ+AauUqtx4SN4Jo0O4PEVyC5iEawWCXk1SWHeDGNHPwievxWkcw0VTaCSJlDJcQK7z/wtjp31B0qsnPHLWfPluv4n/L2Clzg6Z+ATv6+1YbqlDt5nH47XMVw7153yZm7Q59M6w45j6x/hRmC8mfz8dR44jGSb0V5gzJUCEZpknDSb7Gjna/oai3ANv7bH+41/RDWPPkgwzj7DsUAUfLaFLgfXw3kvPQFGscF4Bwcgb49AAictCUSixAoJKMvA9Rnhx1kcX2N09jyJShM2MQnqTn2hMOC8IBdGsAaW7sXZIUjcKxAf5yVJ5RZStSlQSB9h4V48J89YJJZjUoYEpXApF4D08vQhqwKxdI19wReFQHpvcQaQWpSbQEmVBFIfdvUXYJSTFst4IReTuyx7RJhZAKWZ+xQOtUAmiZJTU74kUCrVtwTOovKkoVjjjC9xJhcXmsK7sSAQS/d77uSIBGZtI3UZMAp/jyD7TYFxMUml4DFIHpV4Wq54TCxrAJ6+BEs3q5ijEhjLtiJ5KZTYLIXUNzRecZtQGc9lian0kmhbE+Vi+ZYWFnh8+JxBWVzUkSUcy3dPCoEon7ed/QTypKUrLK3UQW5IZgkYQU7c8600v7BUIQiMx6BV7QEL0Ltxb/kSadL4CkslDuJiMgssBIocvYjQ5LG95bDQ7y7mPeFyY00ljq1cvsj/CETeLeXY5873qIS0mARopZb2fil/JLAwWf/vWGg1SYzvQU3yUqakiZK8XHnvlwKjqWC3QBLHG584WOPXLESmfR2QOsZwLUlKF5YyMKqGhiZQSROopAlU0gQqaQKVNIFKmkAlTaCSJlBJE6jCuV+eT1jXQ5eSKQAAAABJRU5ErkJggg=='
# url2 = url.split(',')[1]
#
# try:
#     base64change(url2)
#     print('go-1')
# except:
#     print('not_1')
#
# #
# try:
#     base64change(url)
#     print('go_2')
# except:
#     print('not_2')

# encoding:utf-8

import requests
import token

token

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
# f = open('[本地文件]', 'rb')
# img = base64.b64encode(f.read())

params = {"image":url}
access_token = 'BAIDUID=B80FF2477A8E435EB2B984A6E47CBC00:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2145916555; path=/; domain=.baidu.com; version=1'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())


def token():
    # encoding:utf-8
    import requests

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=gYovtVWrR3HQphD6dlCzsL1t&client_secret=gYovtVWrR3HQphD6dlCzsL1t'
    response = requests.get(host)
    if response:
        print(response.json())
    return response