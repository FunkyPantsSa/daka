
import requests
def recognize(url):

    '''
    通用文字识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    # f = open('[本地文件]', 'rb')
    # img = base64.b64encode(f.read())
    img = url
    params = {"image":img}
    #tocken 由上面的touken()生成
    access_token = '24.a509ec003ba616574232f9fdbaa92f57.2592000.1611282539.282335-23167872'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    response = response.json()
    return response

def tocken():
    import requests
    # client_id 为网官获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=  网官获取的AK  &client_secret=  官网获取的SK  '
    response = requests.get(host)
    if response:
        print(response.json())

def json1(data):
    import json
    s = json.dumps(data)
    s1 = json.loads(s)
    # print (s1["words_result"])
    s2 = str(s1["words_result"])
    # print(s2.replace(' ', '')[11:15])
    # print(s2)
    s3 = s2.replace(' ', '')
    # print(s3)
    return s3[11:15]

# url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAeCAYAAAC7Q5mxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKNSURBVGhD7Zc9csMgEEZ1PA6kA7jPAdxQ+AauUqtx4SN4Jo0O4PEVyC5iEawWCXk1SWHeDGNHPwievxWkcw0VTaCSJlDJcQK7z/wtjp31B0qsnPHLWfPluv4n/L2Clzg6Z+ATv6+1YbqlDt5nH47XMVw7153yZm7Q59M6w45j6x/hRmC8mfz8dR44jGSb0V5gzJUCEZpknDSb7Gjna/oai3ANv7bH+41/RDWPPkgwzj7DsUAUfLaFLgfXw3kvPQFGscF4Bwcgb49AAictCUSixAoJKMvA9Rnhx1kcX2N09jyJShM2MQnqTn2hMOC8IBdGsAaW7sXZIUjcKxAf5yVJ5RZStSlQSB9h4V48J89YJJZjUoYEpXApF4D08vQhqwKxdI19wReFQHpvcQaQWpSbQEmVBFIfdvUXYJSTFst4IReTuyx7RJhZAKWZ+xQOtUAmiZJTU74kUCrVtwTOovKkoVjjjC9xJhcXmsK7sSAQS/d77uSIBGZtI3UZMAp/jyD7TYFxMUml4DFIHpV4Wq54TCxrAJ6+BEs3q5ijEhjLtiJ5KZTYLIXUNzRecZtQGc9lian0kmhbE+Vi+ZYWFnh8+JxBWVzUkSUcy3dPCoEon7ed/QTypKUrLK3UQW5IZgkYQU7c8600v7BUIQiMx6BV7QEL0Ltxb/kSadL4CkslDuJiMgssBIocvYjQ5LG95bDQ7y7mPeFyY00ljq1cvsj/CETeLeXY5873qIS0mARopZb2fil/JLAwWf/vWGg1SYzvQU3yUqakiZK8XHnvlwKjqWC3QBLHG584WOPXLESmfR2QOsZwLUlKF5YyMKqGhiZQSROopAlU0gQqaQKVNIFKmkAlTaCSJlBJE6jCuV+eT1jXQ5eSKQAAAABJRU5ErkJggg=='
# a = recognize(url)
# print(type(a))
# type(a)
# k = json1(a)
# print(k)
