import speech_recognition as sr
import pyttsx3
import time
import pyautogui
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as mic:
            print("speak anything")
            listen = r.listen(mic)
            text = r.recognize_google(listen)
            text = text.lower()
            print("you said: ", format(text))
            if 'siri' in text:
                pyautogui.keyDown("winleft")
                pyautogui.press("2")
                pyautogui.keyUp("winleft")
            if 'terminal' in text:
                pyautogui.keyDown("winleft")
                pyautogui.press("1")
                pyautogui.keyUp("winleft") 
    except:
        print("sorry cant get this")
        pass
        
