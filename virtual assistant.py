import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("How may I help you?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        print("Please say that again")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")  
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("The time is",Time) 
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "quit" in query:
            exit()
        else:
            print("No query matched")