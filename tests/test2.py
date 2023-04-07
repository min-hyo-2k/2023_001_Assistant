import os
from playsound import playsound
from gtts import gTTS
import threading
import time
import random
import multiprocessing

def speak(text):
    tts = gTTS(text)
    # max 6 speaker speak at same time
    try:
        for i in range(5):
            time.sleep(random.random()) # avoid playsound start at same time and raise error
            if os.path.isfile(f"temp{i}.mp3"):
                continue
            else:
                tts.save(f"temp{i}.mp3")
                playsound(f"temp{i}.mp3")
                os.remove(f"temp{i}.mp3")
                break
    except Exception as e:
        print(e)

def txt(text):
    print(text)

def speak_thread(text):
    # t = threading.Thread(target=speak, args=[text])
    t = multiprocessing.Process(target=speak, args=[text])
    t.start()

if __name__ == '__main__':
    speak_thread('Have a good day')
    speak_thread('How can i help you')
    speak_thread('I can not help you')
    speak_thread('Minh Hieu')
    speak_thread('I can')
    speak_thread('I can not')