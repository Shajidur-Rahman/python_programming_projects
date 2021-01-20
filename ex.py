
import speech_recognition as sr
import pyttsx3
import pyautogui
r = sr.Recognizer()


while True:
    try:
        with sr.Microphone() as mic:
            print("speak anything")
            listen = r.listen(mic)
            text = r.recognize_google(listen)
            print("you said: ", format(text))
            pyautogui.typewrite(text)
    except:
        print("sorry cant get this")
        
