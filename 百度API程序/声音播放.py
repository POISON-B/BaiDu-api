# date： 18-2-19
from pyaudio import PyAudio
import wave

CHUNK = 1024

wf = wave.open('8k.wav', 'rb')
# print(wf)
p = PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
data = wf.readframes(CHUNK)
# for i in data:
    # print(len(data))

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()