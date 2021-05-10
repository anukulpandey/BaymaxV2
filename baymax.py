# Importing all Modules
import pyttsx3 as ps
import speech_recognition as sr
import time
import os
import wolframalpha
import webbrowser
import wikipedia
from datetime import datetime,date
import json

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

def timeNow():
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
    print("Enter your username here:",end="")
    username=input()
    if username in parsedCred:
        speak(f'Hello {username} ! Enter your password')
        print("Enter your password here:",end="")
        password=input()
        if password==parsedCred[f"{username}"]:
            speak(f"Welcome back!{username}")
        else:
            print("---INCORRECT PASSWORD---")
            speak("sorry the password you entered is incorrect!please try again")
            i=0
            for i in range(0,2):
                print("Enter your password here:",end="")
                password=input()
                if password==parsedCred[f"{username}"]:
                    speak(f"Welcome back!{username}")
                    break
                elif i==1:
                    speak("Intruder Detected!Making a log of intruder login")
                    print(f"Log made at {timeNow()}")
                else:
                    print("---INCORRECT PASSWORD---")
                    speak("sorry the password you entered is incorrect!please try again")
    elif username=="leave":
        return 0
    else:
        speak("Sorry you are not in our data base,To continue using assistant,Create an account")
        speak("by logging in as admin")
        userLogin()

        
# Paths 
pathDict={
    "chrome":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "edge":"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "word":"C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE",
    "code":"C:/Users/anuku/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    }

# Credentials
credentials='{"anukul":"333","admin":"1234"}'
parsedCred=json.loads(credentials)
loopCounter=0

# Constants and Variables
intro='Hey Beymax here!\n To use me as your assistant you have to login first.'
wdym="sorry sir I did not get you,can you please repeat"
wdywmtd="What do you want me to do?"

# Main function here
def mainFunc():
    if "open chrome" in query.lower():
        openApp(pathDict['chrome'])
        speak("Opened chrome successfully!")
        time.sleep(10)
    elif "open code editor" in query.lower():
        openApp(pathDict['code'])
        speak("Opened VS Code successfully!")
        time.sleep(10)
    elif "turn off" in query.lower():
        speak("Turning off my brain,Take care Sir")
        exit()
    elif "open microsoft word" in query.lower():
        openApp(pathDict['word'])
        speak("Opened Microsoft word Successfully!")
        time.sleep(10)
    elif "open microsoft edge" in query.lower():
        openApp(pathDict['edge'])
        speak("Opened Microsoft edge Successfully!")
        time.sleep(10)
    elif "answer me" in query.lower():
        speak("what do you want to ask me sir?")
        question=listen()

# Logic Starts Here
if __name__=="__main__":
    # speak(intro)
    # if userLogin()!=0:
    #     speak(wdywmtd)
        while True:
            try:
                query=listen()
                print(query)
                break
            except Exception as e:
                speak("Sir please repeat")
        while True:
            if loopCounter!=0:
                speak("Is there anything more I can do for you?")
                while True:
                    try:
                        listened_word=listen()
                        print(listened_word)
                        break
                    except Exception as e:
                        speak("Sir please repeat")
                if listened_word.lower()=="yes":
                    speak(wdywmtd)
                    while True:
                        try:
                            query=listen()
                            print(query)
                            break
                        except Exception as e:
                            speak("Sir please repeat")
                    mainFunc()
                    loopCounter+=1
                elif listened_word.lower()=="no":
                    speak("Ok Sir May I sleep till then?")
                    while True:
                        try:
                            query=listen()
                            print(query)
                            break
                        except Exception as e:
                            speak("Can you please repeat sir if i can sleep or not?")
                    if "yes" in query.lower():
                        speak("For how many seconds sir?")
                        print("Enter the number of seconds you want me to sleep:")
                        secs=int(input())
                        speak(f"Ok sir sleeping for {secs} secondss")
                        time.sleep(secs)
                    elif listened_word.lower()=="no":
                        speak("Ok sir")
                    else:
                        speak("Sorry I did not get you sir")
                else:
                        speak("Sorry I did not get you sir")
            else:
                mainFunc()
                loopCounter+=1

