def json1(data):
    import json
    s = json.dumps(data)
    s1 = json.loads(s)
    # print (s1["words_result"])
    s2 = str(s1["words_result"])
    # print(s2.replace(' ', '')[11:15])
    return s2.replace(' ', '')[11:15]

def json11(data):
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

def json2(data):
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
# data = {'words_result': [{'words': 'FBG'}], 'log_id': 1341586120244199424, 'words_result_num': 1}
# s= json(data)
# print(s)

# print(s2['words'])
# s3 = json(s2)
# print(s2)


url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAeCAYAAAC7Q5mxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAITSURBVGhD7ZY7joMwEIa52bY+kKu9wlbbu0izR6CmipQDbJeGE0TKCby/HxPAmMBgHgvyJ00ExB7sT4PtQmeSyAITyQITyQITyQITCQTWWolCF8V4CFX7PjEeyPOFdmGUuvItKtn/X6iH/3dpMNYSU/2ZEL/v5tUHPWKQSPmacJtKjgkkSORFx5rX6uLkiZuZ4gaQSOnvA64bCYRCrVgCm8pruGu5atXFGBFoRrmNwKkMCXTyZFryGYwJ5MMUiOeKM+uIwPqmxcAnPYgSGCmGapPgx1zb4IqICyyKT1QeZ14NPIG10oJVNoHAqmyuJ4EJYxxOFkKpljRkMc9Y4+kKpM1LP5H3ysnTgGwxSGAkZgqUftedteZVmDDejc7+gQebGa8KSWAk1hG4VAVivZOm+mZKJIHhq2cL/PD3nvUqcOE10K5/TmIh77bFJBYSaNY69W0Ehn0gdpM1kM3QJuIlTj3/LSDQvM+K2ncX5hIRaHHHGPdJT9hUEgS6dxh5htMINDTr46jEmQIbccTmAgXvvNaDJA2c++yxhiS+OVjTObCTBNcYI9YBexnSl2dAQysQfZ7+USKBQBIXBrcS29XVjlalBfKibV6S2oHqwWmg+wzh5VKeLiQujPRKRJbz0Be3PqcQGK+6bTi8wL3EEYcWuLc8wyEF7vnJhhxO4H8RR5xiE9mTLDCRLDCRLDCRLDAJrf8A1Yhth0/tJlEAAAAASUVORK5CYII='
# url2 = 'iVBORw0KGgoAAAANSUhEUgAAAFAAAAAeCAYAAAC7Q5mxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKNSURBVGhD7Zc9csMgEEZ1PA6kA7jPAdxQ+AauUqtx4SN4Jo0O4PEVyC5iEawWCXk1SWHeDGNHPwievxWkcw0VTaCSJlDJcQK7z/wtjp31B0qsnPHLWfPluv4n/L2Clzg6Z+ATv6+1YbqlDt5nH47XMVw7153yZm7Q59M6w45j6x/hRmC8mfz8dR44jGSb0V5gzJUCEZpknDSb7Gjna/oai3ANv7bH+41/RDWPPkgwzj7DsUAUfLaFLgfXw3kvPQFGscF4Bwcgb49AAictCUSixAoJKMvA9Rnhx1kcX2N09jyJShM2MQnqTn2hMOC8IBdGsAaW7sXZIUjcKxAf5yVJ5RZStSlQSB9h4V48J89YJJZjUoYEpXApF4D08vQhqwKxdI19wReFQHpvcQaQWpSbQEmVBFIfdvUXYJSTFst4IReTuyx7RJhZAKWZ+xQOtUAmiZJTU74kUCrVtwTOovKkoVjjjC9xJhcXmsK7sSAQS/d77uSIBGZtI3UZMAp/jyD7TYFxMUml4DFIHpV4Wq54TCxrAJ6+BEs3q5ijEhjLtiJ5KZTYLIXUNzRecZtQGc9lian0kmhbE+Vi+ZYWFnh8+JxBWVzUkSUcy3dPCoEon7ed/QTypKUrLK3UQW5IZgkYQU7c8600v7BUIQiMx6BV7QEL0Ltxb/kSadL4CkslDuJiMgssBIocvYjQ5LG95bDQ7y7mPeFyY00ljq1cvsj/CETeLeXY5873qIS0mARopZb2fil/JLAwWf/vWGg1SYzvQU3yUqakiZK8XHnvlwKjqWC3QBLHG584WOPXLESmfR2QOsZwLUlKF5YyMKqGhiZQSROopAlU0gQqaQKVNIFKmkAlTaCSJlBJE6jCuV+eT1jXQ5eSKQAAAABJRU5ErkJggg=='
print(url.split(',')[1])
# {'log_id': 8214246568169546265, 'words_result_num': 1, 'words_result': [{'words': ' NWx C'}]}
from recognize import recognize2
json4 = recognize2(url)
a = json2(json4)
print(a)