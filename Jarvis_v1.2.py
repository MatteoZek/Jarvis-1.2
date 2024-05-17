import speech_recognition as sr    # pip install SpeechRecognition and PyAudio
import pyttsx3                     # pip install pyttsx3
import datetime                    # pip install datetime
import webbrowser
import subprocess
import os
import pywhatkit
import wikipedia                   # pip install wikipedia

r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
cont = "yes"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def time1():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
def startup():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12 :
        speak("Good morning sir!")
    elif hour >= 12 and hour<18 :
        speak("Good afternoon sir!")
    elif hour >= 18 and hour<=24:
        speak("Good evening sir!")
    elif hour >= 0 and hour<6:
        speak("Good evening sir!")
    speak("The current time in your location is:")
    time1()
    speak("The current date is:")
    date()
    speak("Jarvis at your service sir.")


def take_command():
        with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                voice_data = ''
                try:
                        voice_data = r.recognize_google(audio)
                        voice_data = voice_data.lower()
                        print(voice_data)
                except Exception as e:
                        return "None"

                return voice_data


def run_jarvis():
    command = take_command()
    if "hello jarvis" in command:
            speak("hello sir")
    elif "rest" in command:
            speak("going into sleep mode, if you need anything you now what to do")
            input("Press Enter to continue...")
    elif "sleep" in command:
            speak("going into sleep mode, if you need anything you now what to do")
            input("Press Enter to continue...")
    elif "time" in command:
             speak("The current time is:")
             time1()
    elif "hour" in command:
             speak("The current time is:")
             time1()
    elif "date" in command:
             speak("Todays date is:")
             date()
    elif "shut down" in command:
            speak("jarvis shutting down sir")
            quit()
    elif "shutdown" in command:
            speak("jarvis shutting down sir")
            quit()
    elif "deactivate" in command:
            speak("jarvis shutting down sir")
            quit()
    elif "turn off" in command:
            speak("jarvis shutting down sir")
            quit()
    elif "power off" in command:
            speak("jarvis shutting down sir")
            quit()
    elif "open youtube" in command:
            speak("opening youtube from brave browser")
            webbrowser.open("http://youtube.com")
    elif "open google" in command:
            speak("opening google from brave browser")
            webbrowser.open("http://google.com")
    elif "let me check my emails" in command:
            speak("i'll open gmail in a moment sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif "open gmail" in command:
            speak("i'll open gmail in a moment sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif "open my class register" in command:
            speak("opening the class register")
            webbrowser.open("https://web.spaggiari.eu/home/app/default/menu_webinfoschool_studenti.php")
    elif "let me see my marks" in command:
            speak("opening the class register")
            webbrowser.open("https://web.spaggiari.eu/home/app/default/menu_webinfoschool_studenti.php")
    elif "open discord" in command:
            speak("opening discord sir")
            subprocess.call('C://Users//matte//AppData//Local//Discord//app-1.0.9003//Discord')
    elif "open minecraft" in command:
            speak("opening minecraft")
            subprocess.call('C://Users//matte//AppData//Local//Programs//lunarclient//Lunar Client')
    elif "open teams" in command:
            speak("opening microsoft teams")
            subprocess.call('C://Users//matte//AppData//Local//Microsoft//Teams//current//Teams')
    elif "open themes" in command:
            speak("opening microsoft teams")
            subprocess.call('C://Users//matte//AppData//Local//Microsoft//Teams//current//Teams')
    elif "news" in command:
            speak("here is the last news report that went on air")
            webbrowser.open("https://www.rainews.it/notiziari/tg1")
    elif "open word" in command:
            speak("opening microsoft word")
            subprocess.call('C://Program Files//Microsoft Office//root//Office16//WINWORD')
    elif "shop" in command:
            product = command.replace('shop', '')
            webbrowser.open("https://www.amazon.it/s?k=" + product)
    elif "search on google" in command:
            object = command.replace('search on google', '')
            webbrowser.open("https://www.google.com/search?q=" + object)
    elif "open school folder" in command:
            os.startfile('C://Users//matte//Documents//school')
    elif "open documents" in command:
            os.startfile("C://Users//matte//Documents")
    elif "open messages" in command:
            speak("opening whatsapp web and connecting to phone")
            subprocess.call('C://Users//matte//AppData//Local//Whatsapp//Whatsapp')
    elif "open music" in command:
            speak("opening spotify")
            subprocess.call('C://Users//matte//AppData//Roaming//Spotify//Spotify')
    elif "play" in command:
            song = command.replace('play', '')
            pywhatkit.playonyt(song)
    elif "send a message" in command:
            speak("Write message text here")
            text = input("Write message text here:")
            speak("Write the phone number here")
            number= input("Write the phone number here: (remember to add a prefix like +39)")
            pywhatkit.sendwhatmsg_instantly(number, text , 15)
    elif "send message" in command:
            speak("Write message text here")
            text = input("Write message text here:")
            speak("Write the phone number here")
            number= input("Write the phone number here: (remember to add a prefix like +39)")
            pywhatkit.sendwhatmsg_instantly(number, text , 15)
    elif "search information on" in command:
             thing = command.replace('search information on', '')
             info = wikipedia.summary(thing, 1)
             speak(info)


startup()
while cont == "yes":
        run_jarvis()
#        cont = input("Insert another instruction yes/no? ")

