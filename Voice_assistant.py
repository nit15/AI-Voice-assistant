import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import googlesearch
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

engine= pyttsx3.init('sapi5')

task=['Search youtube for playing any video','open for google,youtube,spotify or any other platform','search for google anything']
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour= int(datetime.datetime.now().hour)
    if hour<12:
        speak("good morning")
    elif hour>=12 and hour<=16:
        speak("Good afternoon")
    elif hour>16 and hour<=22:
        speak("Good evening")
    else:
        speak("It's a night. Go and get some sleep")

    speak("hello! I am smart assistant, How may I help you?")

def input():
    i= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        i.pause_threshold = 0.8
        i.energy_threshold = 1000
        audio = i.listen(source)

    try:
        print("Recognizing.....")
        query = i.recognize_google(audio,language='en-in')
        print("user said:"+query)

    except Exception as e:
        print("Sorry, Please Say that again and clear...")
        return "None"

    return query.lower()


if __name__ == '__main__':
    greet()
    while True:

        query = str(input().lower())

        if "wikipedia" in query:
            query=query.replace("wikipedia","")
            try:
                result= wikipedia.summary(query,sentences=3)
                speak("According to wikipedia..")
                print(result)
                speak(result)
            except Exception as e:
                print("Sorry not found")
                speak("Sorry..!! not found")


        elif ("your name" in query or "who are you" in query):
            print("Hello!, my name is Neet, I am your smart assistant and the name of my creater is, Mr. nitya parikh ")
            speak("Hello!, my name is Neet, I am your smart assistant and the name of my creater is, Mister nitya parikh ")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is:"+time)

        elif ("search" in query or "google" in query):
            query=query.replace("search","")
            url=""
            url+=str()
            for i in googlesearch.search(query,tld="com", num=1, stop=1, pause=2):
                 list=[]
                 webbrowser.open(i)
                # print(list[0])

        elif "how are you" in query:
            speak("Thanks for asking...I am fine master. What about you?")

        elif ("not fine" in query or "not good" in query or "not well" in query or "sad" in query):
            speak("Let's listen some of your favourite music, what you say,master?")
            input()
           #spotify.Album()

            from time import sleep

        elif "search" and "youtube" in query:
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

        elif "datasheet" in query:

            speak()




