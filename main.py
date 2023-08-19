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

print(decoration.word)

password = input("Enter password : ")
mainpassword = "0506"

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
            try:
                functions.speak("What should I say?")
                content = functions.takeCommand().lower()
                tomail = input("Enter email id: ")
                to = tomail
                functions.sendEmail(to, content)
                functions.speak("Email has been sent!")
            except Exception as e:
                print(e)
                functions.speak(
                    "Sorry boss, I was not able to send this email")

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
            if password == mainpassword:
                print("right password")
                # Make sure whatsapp web is open and you're logged in with your account
                functions.speak(
                    "To which number should I send the message? Please enter in the console."
                )
                number = input("Enter the number: ")
                functions.speak("What is the message?")
                message = functions.takeCommand().lower()
                functions.send_whatsapp_message(number, message)
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
