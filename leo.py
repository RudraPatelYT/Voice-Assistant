import datetime
import wikipedia
import webbrowser
from pprint import pprint
import os
import pywhatkit as kit
import sys
import speech_recognition as sr
import pyttsx3
import requests
import json
import pyautogui
import decoration
import pywhatkit
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from termcolor import cprint


cprint(decoration.image.center(768), decoration.color)

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
        # print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        # print("Good Afternoon!")

    else:
        speak("Good Evening!")
        # print("Good Evening!")

    speak("I am Leo boss. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        # print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        # print("Say that again please...")
        return "None"
    return query


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


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            # print(results)
            speak(results)
            speak("do you want me to print?")
            answer = takeCommand().lower()
            if answer == "yes" or answer == "yup":
                print(results)
            else:
                None
        elif 'open youtube' in query:
            speak(f'What do you want me to play on Youtube?')
            video = takeCommand().lower()
            play_on_youtube(video)
        elif "open google" in query:
            speak("boss, what should i search on google?")
            cm = takeCommand().lower()
            link = f"https://www.google.com/search?q={cm}"
            webbrowser.open(link)

        elif "open rudra patel website" in query:
            webbrowser.open("https://rudrapatelyt.netlify.app/")
        elif 'play music from youtube' in query:
            webbrowser.open(
                "https://www.youtube.com/watch?v=vtNJMAyeP0s&list=RDvtNJMAyeP0s&start_radio=1&rv=vtNJMAyeP0s&t=0")

        elif "play music" in query:
            music_dir = "C:\\Users\\Admin\\Desktop\\song"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # print(strTime)
            speak(f"Boss, The time is {strTime}")
        elif "you are good" in query:
            # print("Thank you boss!")
            speak("Thank you boss!")
        elif "open code" in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open chrome" in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)

        elif "email" in query:
            speak("Do you want to send attachments in email?")
            emailvoice = takeCommand().lower()
            if emailvoice == "yes" or emailvoice == "yup":
                speak("Please, enter recipient email in the console")
                receiver_email = input('Recipient email : ')
                speak("Please, tell me what is the subject?")
                subject = takeCommand().lower()
                speak("Please, tell me what is the body?")
                body = takeCommand().lower()
                filename = input("Enter your file name : ")
                sender_email = ""
                password = ""

                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email  # Recommended for mass emails
                message.attach(MIMEText(body, "plain"))

                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )

                message.attach(part)
                text = message.as_string()

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
            else:

                speak("Please enter recipient email in the console")
                receiver_email = input('Recipient email : ')
                speak("Please what is the subject?")
                subject = takeCommand().lower()
                speak("Please what is the body?")
                body = takeCommand().lower()
                sender_email = ""
                password = ""

                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email  # Recommended for mass emails
                message.attach(MIMEText(body, "plain"))
                text = message.as_string()

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email,
                                    receiver_email, text)

            # print("Email successfully sent")
            speak("Email successfully sent!!")

        elif "exit" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                # print("Thanks for using me boss, have nice day.")
                speak("Thanks for using me boss, have nice day.")
            else:
                # print("Thanks for using me boss, have a good night.")
                speak("Thanks for using me boss, have a good night.")
            sys.exit()
        # elif "latest news" in query:
        #     question = input("What type of news are you interested in? ")
        #     url = f""
        #     r = requests.get(url)
        #     news = json.loads(r.text)
        #     print(news, type(news))
        #     for article in news["articles"]:
        #         print(article["title"])
        #         print(article["description"])
        #         print("-----------------------------------")
        elif "leo" in query:
            # print("Yes boss!!")
            speak("Yes boss!!")
        elif "open notepad" in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(codepath)
        elif "open game" in query:
            codepath = "D:\\Users\\Rudra\\Desktop\\builds\\3dgame\\builds\\Car Game (Patel).exe"
            os.startfile(codepath)
        elif "type" in query:
            # print("What should I write boss?")
            speak("What should I write boss?")
            type_text = takeCommand().lower()
            pyautogui.write(type_text)
        elif "send a whatsapp message" in query:
            speak("Do you need to send image?")
            whatvoice = takeCommand().lower()
            speak(
                "To which number should I send the message? Please enter in the console."
            )
            number = input("Enter the number: ")
            if whatvoice == "no" or whatvoice == "nope":
                speak("Do you want type message?")
                speak("What is the message?")
                message = input("What is the message : ")
                send_whatsapp_message(number, message)
                speak("I've sent the message.")
            else:
                caption = input("Caption : ")
                imagePath = input("Image Path : ")
                pywhatkit.sendwhats_image(number, imagePath, caption, 10)
                speak("I've sent the message.")

        elif "joke" in query:
            speak(f"Hope you like this one")
            joke = get_random_joke()
            speak(joke)
            speak("do you want me to print it?")
            jokevoice = takeCommand().lower
            if jokevoice == "yes" or jokevoice == "yup":
                pprint(joke)
            else:
                None

        elif "excel" in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(codepath)

        elif "advice" in query:
            speak(f"Here's an advice for you")
            advice = get_random_advice()
            speak(advice)
            speak(
                "For your convenience, I am printing it on the screen")
            speak("do you want me to print it?")
            advicevoice = takeCommand().lower
            if advicevoice == "yes" or advicevoice == "yup":
                pprint(advice)
            else:
                None
        elif "thank you" in query:
            speak("You're welcome.")

        elif "who are you" in query:
            speak(
                "I was an assistant of Tony Stark. \n But now I am your assistant")

        elif "who am i" in query:
            speak(
                "If you could talk, you're definetly a human. \n I guess.")

        elif "who is your boss" in query:
            speak("You are my boss")
