import datetime
import wikipedia
import webbrowser
from pprint import pprint
import os
import sys
import requests
import json
import pyautogui
import functions
import decoration
import pywhatkit
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print(decoration.word)

password = input("Enter password : ")
mainpassword = "jarvis@0506"
whatsapppassword = "whatsapp@0506"

if password == mainpassword:
    print("right password")
else:
    print("wrong password!!")
    sys.exit()

if __name__ == "__main__":
    functions.wishMe()
    while True:
        query = functions.takeCommand().lower()
        if "wikipedia" in query:
            functions.speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            functions.speak("According to wikipedia")
            print(results)
            functions.speak(results)
        elif 'youtube' in query:
            functions.speak(f'What do you want me to play on Youtube?')
            video = functions.takeCommand().lower()
            functions.play_on_youtube(video)
        elif "open google" in query:
            functions.speak("boss, what should i search on google?")
            cm = functions.takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open rudra patel website" in query:
            webbrowser.open("rudrapatelyt.netlify.app")
        elif 'play music from youtube' in query:
            webbrowser.open(
                "https://www.youtube.com/watch?v=z8OdasLT_BM&list=RDz8OdasLT_BM")

        elif "play music" in query:
            music_dir = "C:\\Users\\Admin\\Desktop\\song"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            functions.speak(f"Boss, The time is {strTime}")
        elif "you are good" in query:
            print("Thank you boss!")
            functions.speak("Thank you boss!")
        elif "open code" in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open chrome" in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)

        elif "email" in query:
            a = input("Do you want to add attachments in mail : ")
            functions.speak(
                "Please write your subject body reciever email and file path to attach \n\n Please write in console.")
            if a == "Yes":
                subject = input('Subject for your email : ')
                body = input('Body for your email : ')
                sender_email = "rudylegendarygamer@gmail.com"
                receiver_email = input('Recipient email : ')
                password = "yxddsklwccmxahia"
                filename = input("Enter your file name : ")

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

                subject = input('Subject for your email : ')
                body = input('Body for your email : ')
                sender_email = "rudylegendarygamer@gmail.com"
                receiver_email = input('Recipient email : ')
                password = "yxddsklwccmxahia"

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

            print("Email successfully sent")
            functions.speak("Email successfully sent!!")

        elif "exit" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                print("Thanks for using me boss, have nice day.")
                functions.speak("Thanks for using me boss, have nice day.")
            else:
                print("Thanks for using me boss, have a good night.")
                functions.speak("Thanks for using me boss, have a good night.")
            sys.exit()
        elif "latest news" in query:
            question = input("What type of news are you interested in? ")
            url = f"https://newsapi.org/v2/everything?q={question}&from=2023-07-16&sortBy=publishedAt&apiKey=5190dbfb7e324e2295d236076c6bdc50"
            r = requests.get(url)
            news = json.loads(r.text)
            # print(news, type(news))
            for article in news["articles"]:
                print(article["title"])
                print(article["description"])
                print("-----------------------------------")
        elif "jarvis" in query:
            print("Yes boss!!")
            functions.speak("Yes boss!!")
        elif "open notepad" in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(codepath)
        elif "type" in query:
            print("What should I write boss?")
            functions.speak("What should I write boss?")
            type_text = functions.takeCommand().lower()
            pyautogui.write(type_text)
        elif "send a whatsapp message" in query:
            password = input("Enter your password : ")
            if password == whatsapppassword:
                print("right password")
                whatinput = input("Do you need to send image (Yes / No) : ")
                functions.speak(
                    "To which number should I send the message? Please enter in the console."
                )
                number = input("Enter the number: ")
                if whatinput == "No":
                    # Make sure whatsapp web is open and you're logged in with your account
                    functions.speak("Do you want type message?")
                    a = input("Do you want type message? (Yes / No)")
                    if a == "Yes":
                        functions.speak("What is the message?")
                        message = input("What is the message : ")
                        functions.send_whatsapp_message(number, message)
                        functions.speak("I've sent the message.")
                    else:
                        functions.speak("What is the message?")
                        message = functions.takeCommand().lower()
                        functions.send_whatsapp_message(number, message)
                        functions.speak("I've sent the message.")
                else:
                    caption = input("Caption : ")
                    imagePath = input("Image Path : ")
                    pywhatkit.sendwhats_image(number, imagePath, caption, 10)
                    functions.speak("I've sent the message.")
            else:
                print("Wrong password!!")
                functions.speak("Wrong password!!")

        elif "joke" in query:
            functions.speak(f"Hope you like this one")
            joke = functions.get_random_joke()
            functions.speak(joke)
            functions.speak(
                "For your convenience, I am printing it on the screen")
            pprint(joke)

        elif "advice" in query:
            functions.speak(f"Here's an advice for you")
            advice = functions.get_random_advice()
            functions.speak(advice)
            functions.speak(
                "For your convenience, I am printing it on the screen")
            pprint(advice)
        elif "thank you" in query:
            functions.speak("You're welcome.")

        elif "who are you" in query:
            functions.speak(
                "I was an assistant of Tony Stark. \n But now I am your assistant")

        elif "who am i" in query:
            functions.speak(
                "If you could talk, you're definetly a human. \n I guess.")

        elif "who is your boss" in query:
            functions.speak("You are my boss")
