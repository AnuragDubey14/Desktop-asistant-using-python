import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from AppOpener import open
import os 





def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
        return query.lower()
    except Exception as e:
        print("Some error occurred. Sorry.")
        return ""



if __name__ == '__main__':
    say('Hello, I am Jarvis')
    say("Enter your password First.")
    password=input()
    if password=='Anurag1@':
        while True:
            query = takeCommand()
            if query:
                if "open youtube" in query:
                    say("Opening YouTube...")
                    webbrowser.open("https://www.youtube.com")
                elif "open wikipedia" in query:
                    say("Opening Wikipedia...")
                    webbrowser.open("https://www.wikipedia.org")
                elif "open google" in query:
                    say("Opening Google...")
                    webbrowser.open("https://www.google.com")
                elif "sleep" in query:
                    say("Thankyou I am going to sleep!")
                    break
                elif 'jarvis please say what is the timing' in query:
                    hour=datetime.datetime.now().strftime("%H")
                    min=datetime.datetime.now().strftime("%M")
                    say(f'sir the time is {hour} bajke {min} minutes sir')
                elif 'spotify' in query:
                    open(query)
    else:
        say("You Entered Wrong Password I am going to sleep again")

