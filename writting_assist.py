import speech_recognition as sr
import pyttsx3
import time
import pyautogui
r = sr.Recognizer()
with sr.Microphone() as mic:
    print("speak anything")
    listen = r.listen(mic)

    try:
        text = r.recognize_google(listen)
        print("you said: ", format(text))
        time.sleep(3)
        pyautogui.typewrite(text)
        friend = pyttsx3.init()
        friend.say("hey stop speaking. i am writting this first")
        friend.runAndWait()
    except:
        print("sorry cant get this")
        
