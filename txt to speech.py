#from text_to_speech import speak 

#speak("hello", lang="en", save=True, file="hello.mp3")
from gtts import gTTS
import playsound
import os
tts = gTTS(text='hi i am saad দর্শকেরা আমি তানভীর ইসলাম ইস্ত্রিম । চাইতেছি বাংলা  সহকারি বানাতে ? আর সেটা উন্মুক্ত করে দিতে । আপনারা কি এই প্রোজেক্ট এ কাজ করবেন ? ', lang='bn')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
playsound.playsound('good.mp3', True)
 
