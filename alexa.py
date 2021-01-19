import speech_recognition as sr
import pyttsx3
import time
import pyautogui
listener = sr.Recognizer()
try:
    with sr.Microphone() as mic:
        print("listening")
        voice = listener.listen(mic)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'siri' in command:
            pyautogui.hotkey('winleft', 'l')
            print(command)
except:
    print("sorry cant get it. please try again")
        
