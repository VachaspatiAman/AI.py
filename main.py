import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)


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
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how May I help you")

def takeCommand():
    # It takes microphone input form the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizinng...")
        quary = r.recognize_google(audio, language='en-in')
        print(f"Uesr said:{quary}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return quary

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('vachaspatiaman@gmail.com','Aman@2005')
    server.sendmail('amanvachaspati@gmail.com', to, content)
    server.close()


if __name__=="__main__":
        wishMe()
        while True:
            quary = takeCommand().lower()
            if 'wikipedia' in quary:
                speak('Searching Wikipedia...')
                quary = quary.replace("wikipedia", "")
                result = wikipedia.summary(quary, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)

            elif 'open youtube' in quary:
                webbrowser.open("youtube.com")


            elif 'open google' in quary:
                webbrowser.open("google.com")


            elif 'open stakoverflow' in quary:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in quary:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))


            elif 'open code' in quary:
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.3\\bin\\pycharm64.exe"
                os.startfile(codePath)


            elif 'the time' in quary:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'email to aman' in quary:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "shristipandey1812@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend aman bhai. I am not able to send this email")

            elif 'open spotify' in quary:
                webbrowser.open("spotify.com")

            elif 'open mail' in quary:
                webbrowser.open("gmail.com")
