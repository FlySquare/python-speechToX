import speech_recognition as sr
import os
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import datetime

r = sr.Recognizer()

def commands(data):
    print(data)
    if data == "saat kaç" or data == "şuan saat kaç" or data == "saati söyle":
        textToSpeech("saat şuan "+datetime.datetime.now().strftime("%H:%M"))

def speechToText():
    with sr.Microphone() as source:
         print("Dinleniyor...")
         audio = r.listen(source)

    data = ""
    try:
       data = r.recognize_google(audio, language='tr-tr')
       data = data.lower()
       return data
    except sr.UnknownValueError:
           return "error"


def textToSpeech(data):
    tts = gTTS(text=data, lang='tr')
    clip_name = "gunes_voice"+datetime.datetime.now().strftime("%d%m%Y%H%M%S")+".mp3"
    tts.save(clip_name)
    audio = MP3(clip_name)
    os.system("gunes_voice"+datetime.datetime.now().strftime("%d%m%Y%H%M%S")+".mp3")
    time.sleep(audio.info.length+0.2)

textToSpeech("Günaydın Umut, bugün nasılsın? Saat şuan "+datetime.datetime.now().strftime("%H:%M"))


while 1:
    text = speechToText()
    if text != "error":
        commands(text)
