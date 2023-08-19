import requests
import pywhatkit as kit
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am Jarvis boss. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your email id", "your password")
    server.sendmail("your email id", to, content)
    server.close()


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"{number}", message)


def play_on_youtube(video):
    kit.playonyt(video)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res["slip"]["advice"]


def get_random_joke():
    headers = {"Accept": "application/json"}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
