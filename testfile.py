def json(data):
    import json
    s = json.dumps(data)
    s1 = json.loads(s)
    # print (s1["words_result"])
    s2 = str(s1["words_result"])
    # print(s2.replace(' ', '')[11:15])
    return s2.replace(' ', '')[11:15]




data = {'words_result': [{'words': 'FBG'}], 'log_id': 1341586120244199424, 'words_result_num': 1}
s= json(data)
print(s)

# print(s2['words'])
# s3 = json(s2)
# print(s2)