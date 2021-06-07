import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import pyautogui
import wikipedia
import webbrowser as wb
from time import sleep
import pywhatkit
import os
import psutil
from nltk.tokenize import word_tokenize
import subprocess
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is jarvis")
    
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello this is Friday")    

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizning...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query
   
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# hour = I minutes = M seconds =S
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good Night sir!")

def wishme():
    greeting()
    speak("jarvis at your service , please tell me how can i help you?")

def sendwhatsmsg():
    wb.open(' ')#your link to redirect 
    sleep(10)
    pyautogui.press('enter')

def sendmail():
    wb.open(' ')#your link to redirect 
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    wb.open(' '+search)#your link to redirect 
    sleep(10)

def climate():
    speak("the climate pictorial representation is shown sir ")
    wb.open('')#your link to redirect 
    sleep(10)

def news():
    speak('opening news ')
    wb.open(' ')#your link to redirect 
    sleep(10)

def drive():
    speak('opening your google drive')
    wb.open(' ')#your link to redirect 
    sleep(3)

def instagram():
    speak('opening your instagram account')
    wb.open(' ')#your link to redirect 
    sleep(3)

def facebook():
    speak('opening your facebook account')
    wb.open(' ')#your link to redirect 
    sleep(3)    

def shoping():
    speak('opening amazon')
    wb.open(' ')#your link to redirect 
    sleep(3)

def calender():
    speak('opening your calender to find your task scheduled')
    wb.open(' '))#your link to redirect 
    sleep(3)


def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query
 
def cpustatus():
     usage = str(psutil.cpu_percent())
     speak('currently the CPU status is.. ')
     battery = psutil.sensors_battery()
     speak("the battery is at")
     speak(battery.percent)
     speak("percentage")
     speak("the temprature of cpu is forty degree celsius ")
     speak("our cooling system is now activated sir")

def introduction():
     speak("allow me to introduce myself")
     speak("I am jarvis 2.0")
     speak("A virtual artificial intelligence")
     speak("created by joel")
     speak("I am here to help you in any task as I can")
     speak("twenty four hours a day and seven days a week")
     speak("how can I help you sir...")

def private():
    speak('opening your private server sir ')
    wb.open(' ')#your link to redirect 
    sleep(3)

def college():
    speak('opening your college website ')
    wb.open(' ')#your link to redirect 
    sleep(3)


def academics():
    speak('opening your moodle account from the college website  ')
    wb.open(' ') #your link to redirect 
    sleep(3)

def exit():
    speak('closing the currently opened window ')
    browserExe = "msedge.exe"
    os. system("taskkill /f /im "+browserExe)

def stop():
    speak('closing the currently opened window ')
    browserExe = "Code.exe"
    os. system("taskkill /f /im "+browserExe)


if __name__ == "__main__":
   introduction()


while True:
  query = takeCommandMic().lower()
  wakeword = "jarvis"
  while True:
   query = takeCommandMic().lower()
   query = word_tokenize(query)
   print(query)
   if wakeword in query: 
    print(query)

   if 'time' in query:
    time()

   elif 'day' in query:
     date()

   elif 'good' in query:
     greeting()

   elif 'offline' in query:
      speak("OK sir ")
      speak("JARVIS is going to the offline mode ")
      speak("have a nice day")
      quit()

   elif 'whatsapp' in query:
    speak("openning whatsap......")
    sendwhatsmsg()

   elif 'gmail' in query:
    speak("openning gmail......")
    sendmail()
 
   elif 'google' in query:
    searchgoogle()
   
   elif 'buy' in query:
    shoping()

   elif 'instagram' in query:
    instagram()

   elif 'facebook' in query:
    facebook()

   elif 'calender' in query:
     calender()     
  
   elif 'who ' in query:
    introduction()
 
   elif 'youtube' in query:
     speak("what should i search for on youtube?")
     topic = takeCommandMic()
     pywhatkit.playonyt(topic)
     sleep(3)
   
   elif 'drive' in query:
    drive()
   
   elif 'server' in query:
    private()

   elif 'news' in query:
    news()
 
   elif 'weather' in query:
     climate()

   elif 'moodle' in query:
     academics()

   elif 'college' in query:
     college()
   
   elif 'download' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(3)

   elif 'code' in query:
     speak("opeming visual code")
     codepath = ' ' #your directory name
     os.startfile(codepath)
     sleep(3)

   elif ' D' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(3)

   elif ' E' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(3)

   elif ' C' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(3) 
 
   elif 'maths' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(3)

   elif 'OS' in query:
     codepath = ' '#your directory name
     os.startfile(codepath)
     sleep(10)
 
   elif 'status' in query:
     speak(" the CPU status is ")
     cpustatus()
  
   elif 'close' in query:
       exit()

   elif 'wake ' in query:
       speak("I am up and online sir") 
    
   