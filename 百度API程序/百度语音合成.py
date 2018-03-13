import requests
import os


def get_token():    #获取token
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'

    data = {
        'grant_type': 'client_credentials',
        'client_id': 'WPkt4n6yv1sLlXbGqTeZcHuF',
        'client_secret': '78ka4t8mbWbGEodvawNyPX86ZCKXN3y2',
    }

    header = {'Content-Type': 'application/json; charset=UTF-8'}
    request = requests.post(token_url, data=data, headers=header)
    return request.json()['access_token']    #将结果转成字典容易提取token
#     print(request.json())
# get_token()

def get_text_fromsound(atoken):
    speed_url = 'http://tsn.baidu.com/text2audio'


    with open('1.txt', 'rb') as f:
        data = f.read().decode('utf8')
        # print(len(data))      #免费版只支持500字
    args_data = {         #百度官方写法
        'tex': data,    #需合成的文字信息 必须urlencode
        'tok': atoken,   #token
        'cuid': 'rocky_shop',   #随意写
        'ctp': 1,         #web端固定值
        'lan': 'zh',      #固定值
        'per': 0          #默认0 可选 1（男声）  3（情感男） 4（情感女）
    }

    resp = requests.get(speed_url, params=args_data)
    # print(resp.url)
    with open('1.mp3', 'wb') as f:
        f.write(resp.content)     #下载合成音频

if __name__ == '__main__':

    get_text_fromsound(get_token())


    os.system('1.mp3')     #调用系统播放器播放
