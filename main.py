import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import time
import pyjokes
import pyautogui
import os
import cv2
from requests import get
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak(" Say that again please")
            return "none"
        query = query.lower()
        return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning sir, its {tt}")
        speak("I am Jarvis, please tell me how may i help you")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon sir, its {tt}")
        speak("I am Jarvis, please tell me how may i help you")
    else:
        speak(f"good evening sir, its {tt}")
        speak("I am Jarvis, please tell me how may i help you")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")


        elif "open camera" in query:
            cap = cv2.VideoCapture(0)

            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)

            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")


        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")




        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()



        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
def TaskExecution():
    wish()
    while True:
        query = takecommand()
