import requests
import base64



def get_token():
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'

    data = {
        'grant_type': 'client_credentials',
        'client_id': 'pVrlMmls5upvZzFe16ccHzb3',
        'client_secret': 'Rcidwst7mPyKDC1h38UUe2crbdKUeAqY',
    }


    request = requests.post(token_url, data=data)
    return request.json()['access_token']
    # print(request.json())
    # print(request.text)
    # print(type(request.json()))
    #
# get_token()


def get_text_fromsound(atoken):
    speed_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + atoken


    with open('1.jpg', 'rb') as f:
        data = f.read()
    args_data = {}
    args_data['image'] = base64.b64encode(data).decode('utf8')
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # print(args_data)
    resp = requests.post(speed_url, data=args_data, headers=header)
    info = resp.text
    print(info)


get_text_fromsound(get_token())