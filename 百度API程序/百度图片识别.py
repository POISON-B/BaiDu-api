import requests
import base64


def get_token():
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'

    data = {
        'grant_type': 'client_credentials',
        'client_id': 'tID6Y7Es4uPQ11X4wBO3xogG',
        'client_secret': 'ISVzQFzUuHiXrsqdqjhjxvqn3LfmqUru',
    }


    request = requests.post(token_url, data=data)
    return request.json()['access_token']


def get_text_fromsound(atoken):
    #车辆信息识别
    # speed_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car?access_token=' + atoken

    #菜品识别
    # speed_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token=' + atoken

    #logo识别
    speed_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/logo?access_token=' + atoken


    with open('04.jpg', 'rb') as f:
        data = f.read()
    args_data = {
        # 'top_num': 5
    }
    args_data['image'] = base64.b64encode(data).decode('utf8')
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # print(args_data)
    resp = requests.post(speed_url, data=args_data, headers=header)
    info = resp.text
    print(info)


get_text_fromsound(get_token())