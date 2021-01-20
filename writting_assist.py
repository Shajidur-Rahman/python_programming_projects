
import speech_recognition as sr
import pyttsx3
import time
import pyautogui
r = sr.Recognizer()


try:
    with sr.Microphone() as mic:
        print("speak anything")
        listen = r.listen(mic)
        text = r.recognize_google(listen)
        print("you said: ", format(text))
        time.sleep(3)
        pyautogui.typewrite(text)
except:
    print("sorry cant get this")
        

