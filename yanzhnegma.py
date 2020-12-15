def yanzheng(yanzheng):

    import base64
    import os
    # imgdata = base64.b64decode(yanzheng)

    lens = len(yanzheng)
    lenx = lens - (lens % 4 if lens % 4 else 4)

    try:
        result = base64.decodebytes(yanzheng[:lenx])
        print('flase')

    except:
        pass
        print('go')


    imgdata = base64.b64decode(yanzheng, '-_')
    # imgdata = base64.urlsafe_b64decode(yanzheng)

    file = open('1.jpg', 'wb')
    file.write(imgdata)
    file.close()

