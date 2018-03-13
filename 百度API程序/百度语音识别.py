
# date： 18-2-18

# from aip import AipSpeech
from pyaudio import PyAudio, paInt16
import requests
import base64
import json
import os
import wave



# 声音数据操作缓存
CHUNK = 1024
# 采样声音通道数
CHANNELS = 1
# 采样率：每秒使用多少bit对采样数据进行保存
RATE = 8000
# 默认录制时间
RECORD_SECONDS = 5
# 默认的采样点编码位数
FORMAT_BITS = paInt16
#声音文件
WAVE_OUTPUT_FILENAME = "1.wav"

#
# # 从麦克风里输入音频数据
# def get_data_mic():
#     p = PyAudio()
#     print('开始录音')
#     # 初始化麦克风设备参数，并开始采样
#     stream = p.open(format=FORMAT_BITS,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)
#     # 声音采集数据缓存
#     frames = []
#     for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     print('*/ 录音结束')
#     # 关闭设备
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     # 返回采集数据位二进制流字符
#     # return b''.join(frames)
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT_BITS))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#
# get_data_mic()
#


def get_token():
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'

    data = {
        'grant_type': 'client_credentials',
        'client_id': 'WPkt4n6yv1sLlXbGqTeZcHuF',
        'client_secret': '78ka4t8mbWbGEodvawNyPX86ZCKXN3y2',
    }

    # header = {'Content-Type': 'application/json; charset=UTF-8'}

    request = requests.post(token_url, data=data)
    return request.json()['refresh_token']
    # print(request.json())
    # print(type(request.json()))
# get_token()


def get_text_fromsound(atoken):
    speed_url = 'http://vop.baidu.com/server_api'
    args_data = {'format': 'pcm',
                 'rate': RATE,
                 'channel': CHANNELS,
                 'cuid': 'rocky_shop',
                 'token': atoken,
                 }

    with open('0841.wav', 'rb') as f:
        data = f.read()

    args_data['len'] = len(data)
    args_data['speech'] = base64.b64encode(data).decode('utf8')
    header = {'Content-Type': 'application/json'}
    resp = requests.post(speed_url, data=json.dumps(args_data), headers=header)
    info = resp.json()
    if info['err_no'] == 0:
        print(info['result'][0])
    else:
        print([info['err_msg']])
    # print(info)
    # print(args_data)
get_text_fromsound(get_token())