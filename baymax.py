# Importing all Modules
import pyttsx3 as ps
import speech_recognition as sr
import time
import os
import wolframalpha
import webbrowser
import wikipedia
from datetime import datetime,date

# Functions
def listen():
    """
    Listens to whatever the user says and return the same as string
    """
    hear=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        hear.pause_threshold = 1
        audio = hear.listen(source)
        query = hear.recognize_google(audio, language='en-in')
    return query

def speak(string):
    """
    Speaks the string given as Input
    """
    engine = ps.init()
    engine.setProperty('rate', 175)
    engine.say(string)
    engine.runAndWait()

def time():
    """
    Returns current time
    """
    now = datetime.now()
    cTime = now.strftime("%H:%M:%S")
    return cTime

def wQue(question):
    """
    Takes question as argument and returns answer
    """
    app_id ='3YP882-WUEKL7HEQ7'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    return answer

def openApp(path):
    """
    Takes path as input and opens software
    """
    os.startfile(path)

def searchPath(listenedWord):
    """
    Searches listenedWord in paths dictionary
    """
    for key in pathDict:
        if listenedWord == key:
            break
    return pathDict[f"{key}"]

def onChrome(listenedWord):
    """
    Searches the desired keyword on google chrome
    """
    theList=listenedWord.split(" ")
    finalWord=""
    for index,elem in enumerate(theList):
        if index==0:
            finalWord=f"{elem}"
        else:
            finalWord=f"{finalWord}+{elem}"
    edge=webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
    edge.open(f"google.com/search?q={finalWord}")

def userLogin():
    speak('Enter your Username below')
    username=input()
    for creds in credentials:
        for key,value in creds.items():
            print(key)
            if key == username:
                speak(f"Hello {key}.Please Enter your password")
                try:
                    password=int(input())
                    if password == value:
                        speak('Credentials matched successfully!You can continue')
                        return 1
                    else:
                        speak('Sorry! Credentials did not match')
                        return 0
                        break
                except Exception as e:
                    print('Password Can not be empty')
            else:
                speak("Sorry No username found")
                speak("If you want to create a new account please")
                while True:
                    userLogin()
                    break
        
# Paths 
pathDict={
    "chrome":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "edge":"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "word":"C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE",
    "code":"C:/Users/anuku/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    }

# Constants and Variables
intro='Hey Beymax here!\n To use me as your assistant you have to login first.'
credentials=[{'anukul':333},{'admin':123}]

# Logic Starts Here
if __name__=="__main__":
    # speak(intro)
    check = userLogin()
    while check:
        speak("Hello Sir What do you want me to do?")
        pass