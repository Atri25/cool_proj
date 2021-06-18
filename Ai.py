import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes 
import smtplib
import requests
import json
import subprocess
import winshell
import random
from googlesearch import search
from pywhatkit import *
import ctypes
import time
import wolframalpha
from pyttsx3 import voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 178)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    
    else:
        speak("Good Evening Sir")

    assname =("jarvis")
    speak("I am your Assistant jarvis")
    # speak(assname) 
    speak("How can i help sir")

    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n") 

        except Exception as e:
            speak("Say that again")
            print("Say that again please")
            return "None"
        return query

def sendEmail(to, content): 
    
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    server.login('gmail', 'pass') 
    server.sendmail('gmail', to, content) 
    server.close() 

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(*results)
            speak(results)
        elif 'hi' in query:
            speak("hello")
        elif 'wow' in query:
            speak("woww")
        elif 'change name' in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
        elif 'what do I tell you bro' in query:
            print("You can tell me the anything")
            speak("You can tell me the anything")
        elif "hello" in query:
            lis = ["Hi", "Hello", "what is up"]
            sel = random.choice(lis)
            speak (sel)
            print (sel)
        elif 'open youtube' in query:
            # webbrowser.open("youtube.com")
            url = "https://www.youtube.com/"

            new = 2  # open in a new tab, if possible
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            # open a public URL, in this case, the webbrowser docs
            # url = "http://docs.python.org/library/webbrowser.html"
            webbrowser.get().open(url, new=new)
        elif 'open google' in query:
            #  webbrowser.open("google.com")
            url = "https://www.google.com/"

            new = 2  # open in a new tab, if possible
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            # open a public URL, in this case, the webbrowser docs
            # url = "http://docs.python.org/library/webbrowser.html"
            webbrowser.get().open(url, new=new)
        elif 'weather' in query:
            api_key = "edffd1bf975a74d5d10e58c5ac8be2d3"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city_name, 'units':'metric'}
            response = requests.get(base_url, params=params)
            # print(response.json())
            weather_json = response.json()
            city = weather_json['name']
            conditions = weather_json['weather'][0]['description']
            temp = weather_json['main']['temp']
            speak(f"city name is {city} and the temperature is {temp} degree celsius. The conditions are{conditions}")
            print(f"city name is {city} and the temperature is {temp} degree celsius. The conditions are{conditions}")
        elif 'open stack overflow' in query:
            url = "stackoverflow.com"

            new = 2  # open in a new tab, if possible
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.get().open(url, new=new)
            #  webbrowser.open("stackoverflow.com")
        elif 'whatsapp' in query:
            # webbrowser.open("web.whatsapp.com") 
            url = "web.whatsapp.com"

            new = 2  # open in a new tab, if possible
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            # open a public URL, in this case, the webbrowser docs
            # url = "http://docs.python.org/library/webbrowser.html"
            webbrowser.get().open(url, new=new)
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")          
        elif 'play music' in query:
             music_dir = 'D:\songs'
             music = os.listdir(music_dir) 
             print (music)
             os.startfile(os.path.join(music_dir, music[0]))   
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is :{strTime}")
            speak(f"Sir, the time is{strTime}")   
        elif 'very good' in query:
            speak("Thank you sir")
            print("Thank you sir")
        elif 'who are you' in query:
            speak("I am jarvis")
        elif 'news' in query:
            url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=c4d7760756b846b7a7709a4264ae6a00"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news, Listen Carefully")

            speak("Thanks for listening...")
        elif 'open cmd' in query:
            path = "d:\\Desktop\\cmd.exe"
            os.startfile(path)    
        elif 'open code' in query:
            code = "C:\\Users\\Atri\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif 'you are right' in query:
            print("you are right, i am right and everyone else is right")
            speak("you are right, i am right and everyone else is right")
        elif 'do you love steve jobs' in query:
            speak("Ya, I love him here is somrthing about him,Steven Paul Jobs  (February 24, 1955 – October 5, 2011) was an American business magnate, industrial designer, investor, and media proprietor. He was the chairman, chief executive officer (CEO), and co-founder of Apple Inc., the chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. ")
            print("Ya, I love him here is somrthing about him,Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American business magnate, industrial designer, investor, and media proprietor. He was the chairman, chief executive officer (CEO), and co-founder of Apple Inc., the chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. ")
        elif 'email to me' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "reviever"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")     
        elif 'send a mail' in query: 
            try: 
                speak("what should I say?") 
                content = takeCommand() 
                speak("whom should i send")   
                to = takeCommand() 
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
        elif 'joke' in query: 
            speak(pyjokes.get_joke())  
            print(pyjokes.get_joke())  
        elif 'search' in query:
            query = query.replace("search", "")
            pywhatkit.search(query)
            print("Searching...")
        elif 'fine' in query:
            speak("Glad to know") 
            print("Glad to know")  
        elif 'yes' in query:
            speak("We have same Ideas") 
            print("We have same Ideas") 
        elif 'no i' in query:
            speak("As you say sir") 
            print("As you say sir")            
        elif "who am i" in query: 
            speak("If you talk then definately your human.") 
            print("If you talk then definately your human.")         
        elif "i like your work" in query: 
            speak("i will improve")       
        elif "why you came to world" in query: 
            speak("Thanks to Atri. further It's a secret")
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Atri")    
        elif 'shutdown system' in query: 
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call('shutdown / p /f')
        elif 'game 2' in query:
            speak("I will help you bro, Let us play snake game")   
            print("I will help you bro, Let us play snake game")
            gamee = "D:\\Desktop\\game\\game 2.py"      
            os.startfile(gamee) 
            exit()  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note)    
        elif "show note" in query: 
                speak("Showing Notes") 
                file = open("jarvis.txt", "r")  
                print(file.read()) 
                speak(file.read(6))
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit()
        elif 'game' in query:
            speak("I will help you bro, Let us play don't touch me")   
            print("I will help you bro, Let us play don't touch me")
            gamee = "D:\\Desktop\\game\\game.py"      
            os.startfile(gamee)
            exit()
        elif 'show voice' in query:
            print(voices)
        elif 'are you sure' in query:
            print("I am always sure")
# D:\\background\\kalam sir.jpg, D:\Arti-oppo-130720\Whatsapp\IMG_20191002_202127.jpg 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "D:\\background\\kalam sir.jpg",
                                                       0)
            speak("Background changed succesfully")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            speak("started listening")
            print("STARTED LISTENING")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            exit()
