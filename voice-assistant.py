import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wolframalpha
from datetime import date
import screen_brightness_control as sbc
from ecapture import ecapture as ec
import pyjokes
import pyautogui
import psutil
from googletrans import Translator
import sys
import randfacts
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *


app = wolframalpha.Client("9PKWL8-W6HYQV9E55")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)


def speak(audio):  # fuction for converting text to audio
    engine.say(audio)
    engine.runAndWait()

try:
    import pywhatkit

except:
    speak("terminal x is unable to connect... please check your internet connection")
    exit(0)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said {query}\n")

    except Exception as e:
        print("Sorry I didn't understand say that again please...")

        return ""
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

def sendEmail(to, message):

    contact = {
        "arqham": "ell9481489750@gmail.com",
        "abdul": "abdgaming4714@gmail.com",
        "ismail": "ismailzabi2003@gmail.com",
        "mohan": "mohanksmohan02@gmail.com",
        "chirag": "chiruchirag9900@gmail.com",
        "samir": "null",
        "kirti": "null"
    }
    for i in contact:
        if i in to:
            receiver = contact.get(i,"null")
            break

    
    if receiver == "null":
        print("no email found\n")
        return -1

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('terminalx824@gmail.com', 'terminalx824!!')
    print("message is delivered to " + receiver)
    print("as " + message)
    speak("message is delivered to " + receiver)
    speak("as " + message)
    mail.sendmail('terminalx824@gmail.com', receiver, message)
    
    mail.close()
    return 1


def whatsapp(to, message):
    driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
    driver.get('https://web.whatsapp.com/')
    speak("login quick..")
    time.sleep(20)
    search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_bar.click()

    search_bar.send_keys(to)
    search_bar.send_keys(Keys.ENTER)

    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    speak("message successfully sent..")


def google(key):
    driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
    driver.get('https://www.google.com')
    time.sleep(3)
    search_bar = driver.find_element_by_name('q')
    search_bar.send_keys(key)
    search_bar.send_keys(Keys.ENTER)

    query = takeCommand()
    if "exit" in query or "quit" in query or "close" in query:
        speak("closing browser")
        driver.close()

    else:
        speak("i am sorry, please say that again")

def findint(string):
    letters = ""
    number = ""
    for i in string:
        try:
            int(i)
            number = number + i
        except:
            letters = letters + i
    return int(number)

def my_name(query):
    speak("please tell me your name")
    print("please tell me your name")

    myname = takeCommand().lower()
    if "i am" in query:
        myname = myname.replace("i am", "")
    if "my name is" in query:
        myname = myname.replace("my name is", "")

    fil3 = open("E:\\name.txt", "wr+")
    fil3.write(myname)

    speak(f"tell me how can i serve you master{fil3.read()}")
    print(f"tell me how can i serve you master{fil3.read()}")
    fil3.close()

def comparison():
    myname = open("E:\\name.txt", "r+").read()
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        if "search for" in query:
            query = query.replace("search for", "")
        if "on" in query or "in" in query:
            try:
                query = query.replace("in", "")
            except:
                query = query.replace("on", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak("wikipedia says...")
        speak(results)


    elif "youtube" in query:
        speak("what would you like to play")
        pywhatkit.playonyt((takeCommand()))
        speak("Give me a minute")
        time.sleep(2)


    elif "music" in query or "play music" in query:
        link = "D:\\New folder"
        array = os.listdir(link)
        index = random.randint(0, len(array))
        speak("playing music \n hope you will enjoy")
        os.startfile(os.path.join(link, array[index]))


    elif "video" in query or "play video" in query:
        path = "F:\movies"
        array = os.listdir(path)
        index = random.randint(0, len(array))
        speak("check out this one.")
        os.startfile(os.path.join(path, array[index]))


    elif "email" in query:
        print("sending email")

        try:
            speak("to whom do you want to send")
            to = takeCommand().lower()
            print(f"to:- {to}")
            speak(f"to:- {to}")

            if "to" in to:
                to = to.replace("to", "")
            speak("what should I send")
            message = takeCommand()

            if sendEmail(to, message) == 1:
                speak("email has been sent successfully")
            else:
                speak(f"no contact in name of {to} is found")

        except Exception as e:
            print(e)
            speak("sorry I couldn't send",e)

    elif "my name" in query:
        if "change" in query:
            my_name(query)
        elif myname == "":
            speak("i dont know your name")
            my_name(query)
        else:
            name = open("E:\\name.txt", "r+").read()
            speak(f"your name is master {name} right")
            print(f"your name is master {name} right")

    elif "open" in query:
        if "youtube" in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(3)

        elif "google" in query:
                webbrowser.open_new_tab("https://www.google.com")
                speak("google is open now")
                time.sleep(3)

        elif "news" in query:
            webbrowser.open_new_tab("https://www.ndtv.com")
            speak("Here are some news from NDTV,Enjoy Reading")
            time.sleep(3)

        elif "photos" in query or "images" in query:
            path = "D:\\photos"
            os.startfile(path)
            time.sleep(3)

        elif "gmail" in query:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("gmail is open now")
            time.sleep(3)
        else:
            try:
                link = "C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\New folder"
                wr = query.replace("open ", "_")
                os.startfile(os.path.join(link, wr))
            except:
                speak("sorry,no such file found")

    elif "youtube" in query:
        if "search" in query:
            query = query.replace("search for", "")
        if "on" in query:
            query = query.replace("on youtube", "")

        else:
            query = query.replace("in youtube", "")

        speak("searching in youtube")
        driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
        driver.get('https://www.youtube.com')
        time.sleep(3)
        search_bar = driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
        search_bar.send_keys(query)
        search_bar = driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button")
        search_bar.send_keys(query)
        time.sleep(2)
        speak("hear you go")

    elif "calculate" in query:
        speak("give me a second")
        app_id = "9PKWL8-W6HYQV9E55"
        client = wolframalpha.Client(app_id)
        index = query.lower().split().index('calculate')
        query = query.split()[index + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print(answer)
        speak("The answer is" + answer)

    elif "timer" in query or "countdown" in query or "stop watch" in query:
        speak('specify the time in seconds')
        seconds = findint((takeCommand()))
        try:
            speak("time starts now")
            pyautogui.countdown(seconds)
            speak("Time up")
            pyautogui.alert("Time up")
        except:
            speak("I was unable to understand please say that again")

    elif "time" in query:
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(t)
        speak(f"its {t}")

    elif "your name" in query:
        speak("my name is Terminal-x")

    elif "today" in query or "date" in query:
        today = date.today()
        d = today.strftime("%A %B %d %Y")
        print(d)
        speak(f"Today's date is:{d}\n")

    elif "what is" in query or "who is" in query:
        if "what is" in query:
            query = query.replace("what is","")

        elif "who is" in query:
            query = query.replace("who is", "")

        try:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        except:
            results = wikipedia.summary(query, sentences=2)
            print("wikipedia says")
            print(results)
            speak(results)

    elif "google maps" in query:
        if "search" in query:
            query = query.replace("search for", "")
        if "on" in query:
            query = query.replace("on google maps", "")
        else:
            query = query.replace("in google maps", "")

        speak("searching in google maps")
        driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
        driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
        time.sleep(2)
        search_bar = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]")
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        speak("here you go")

    elif "amazon" in query:
        if "search" in query:
            query = query.replace("search for", "")
        if "on" in query:
            query = query.replace("on amazon", "")
        else:
            query = query.replace("in amazon", "")

        speak("searching in amazon")
        speak("give me a second")
        driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
        driver.get('https://www.amazon.in')
        time.sleep(2)
        search_bar = driver.find_element_by_xpath(
            '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        speak("this is what i got")

    elif "flipkart" in query:
        if "search" in query:
            query = query.replace("search for", "")
        if "on" in query:
            query = query.replace("on flipkart", "")

        else:
            query = query.replace("in flipkart", "")

        speak("searching in flipkart")
        speak("give me a second")
        driver = webdriver.Chrome(executable_path='C:\\Users\\ABDUL MUEED SOUDAGAR\\PycharmProjects\\pythonProject1\\venv\\chromedriver.exe')
        driver.get('https://www.flipkart.com')
        time.sleep(3)
        search_bar = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        speak("this is what i got")

    elif "search" in query or "google" in query:
        if "search for" in query:
            query = query.replace("search for", "")
        if "google" in query:
            query = query.replace("google", "")

        speak("searching in chrome driver..")
        google(query)

    elif "what can you do" in query or "can you do" in query or "about you" in query:
        speak("I can send email")
        speak("i can browse for you on google, youtube, amazon or flipkart")
        speak("i can take notes and reminders")
        speak("i can tell you date and time")
        speak("and much more")

    elif "whatsapp" in query:
        speak("initiating whatsapp")
        speak("to whom do you want to send")
        print("to whom do you want to send")
        try:
            to = takeCommand()
            print(to)
            speak("what do you want to send")
            message = takeCommand()
            print(message)
            whatsapp(to, message)
        except:
            speak("sorry i was unable to send your message")

    elif "brightness" in query:
        query = findint(query)

        try:
            sbc.set_brightness(query)
        except:
            print("try saying:-  set brightness to 20")
            speak("unable to set brightness")
            speak("try saying  set brightness to 20. this will work")

    elif "read note" in query or "read the note" in query:
        try:
            file = open("E:\\note.txt", "r+")
            speak(file.read())

        except:
            speak("may be file does not existes or there is no content")

    elif "note" in query:
        speak("what should i take as note")
        text3 = takeCommand()
        file = open("E:\\note.txt", "r+")
        speak("should i include date in the note")
        condition = takeCommand()

        if "yes" in condition or "sure" in condition or "absolutely" in condition:
            today = datetime.datetime.today()
            dte = today.strftime("%B %d %Y")
            file.write(dte)

        file.write(text3)
        speak("note saved")

    elif "set a reminder" in query:
        speak("what should I remind you about?")
        txt = takeCommand()
        speak("In how many minutes")
        my_time = int(takeCommand())
        my_time = my_time * 60
        time.sleep(my_time)
        speak(txt)
        pyautogui.alert(txt)

    elif "volume" in query:
        if "up" in query or "increase" in query:
            pyautogui.press("volumeup", findint(query))
            speak(f"volume incresed by {findint()} percent")

        elif "down" in query or "decrease" in query:
            pyautogui.press("volumedown", findint(query))
            speak(f"volume decresed by {findint()} percent")

        elif "mute" in query:
            pyautogui.press("volumemute")

    elif "power" in query or "battery" in query:
        try:
            power = psutil.sensors_battery()
            percentage = power.percent
            speak(f"Sir its{percentage}percent")

            if percentage >= 75:
                speak("we have enough power to continue our work")

            elif percentage >= 40 and percentage <= 75:
                speak("we need to charge the system to continue our work")

            elif percentage >= 15 and percentage <= 40:
                speak("there is not enough power to continue our work")

            elif percentage <= 15:
                speak("the system needs to be charged immediately it may shutdown any minute")

        except:
            speak("i think you are working on desktop \n no need to worry about power")

    elif "joke" in query:
        y = pyjokes.pyjokes.get_joke()
        print(y)
        speak(y)

    elif "fact" in query or "tell me a facts" in query:
        x = randfacts.getFact()
        print(x)
        speak(x)

    elif "screenshot" in query or "snapshot" in query:
        speak("please specify the filename")
        file_name = takeCommand()
        pyautogui.screenshot(f"D:\\photos\\{file_name}.jpg")
        speak(f"image saved in name of {file_name}")

    elif "exit" in query or "quit" in query or "close" in query:
        speak("Terminating application")
        speak("have a nice day")
        exit(0)

    elif "translate" in query:
        translater = Translator()
        speak("what should i translate")
        trans = takeCommand()
        speak("to")
        to = takeCommand()
        try:
            output = translater.translate(text=trans, dest=to)
            print(output)
            speak(output)
            pyautogui.alert(output)
        except:
            speak("sorry say that again please")

    elif "photo" in query or "picture" in query or "selfi" in query or "image" in query:
        speak("please specify the filename")
        file_name2 = takeCommand()
        speak("Smile please")
        ec.capture(0, False, f"D:\\photos{file_name2}.jpg")
        speak(f"image saved in name of {file_name2}")

    elif "product" in query or "buy" in query or "online store" in query:
        speak("if you want to check out or buy a product on online store")
        speak("try saying search for this product on amazon or flipkart")
        speak("for example search for headphones on amazon")

    elif "location" in query:
        speak("if you want to find any location or place")
        speak("try saying search for this location")
        speak("for example search for tokyo")

    elif "how are you created" in query or "how are you made" in query:
        speak("fifth semester computer science students put their heads together and came up with me")

    elif "how are you" in query:
        speak("i am always fine,tell me about you")

    elif "good" in query:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12 and "morning" in query:
            speak(f"good morning {myname}")
        elif hour >= 12 and hour < 18 and "afternoon" in query:
            speak(f"good afternoon {myname}")
        elif hour >= 18 and "evening" in query:
            speak(f"good evening {myname}")
        else:
            speak("it's")
            wishMe()
            speak("actually")

    elif "who are you" in query or "who created you" in query or "who made you" in query:
        speak("i am a virtual assistant designed by fifth sem CSE students")

    elif "stop listening" in query or "wait" in query or "one minute" in query:
        speak("for how long would you want me to hold")
        wait = int(takeCommand())
        speak(f"holding {wait} seconds")
        time.sleep(wait)

    elif "have food" in query or "had food" in query:
        speak("No thank you, I am already full of information ")
        speak("but if you want I can search for near by restaurants for you")

    elif "shut up" in query or "get lost" in query or "silence" in query:
        speak("did i say anything wrong")
        speak("I apologize for that")

    elif "who am i" in query:
        speak(f"you are {myname} ,am i right")


    else:
        speak("unable to recognize, please say that again")

if __name__ == '__main__':

    App = QApplication(sys.argv)
    root = QMainWindow()
    root.setWindowTitle("Voice Based PC Commander")
    root.setFixedWidth(1280)
    root.setFixedHeight(800)
    root.setStyleSheet("background-color : #181818;")



    label = QLabel(root)
    label.setGeometry(0, 0, 800, 600)
    label.move(240, 80)
    label.setPixmap(QtGui.QPixmap("D:\\gif22.gif"))
    label.show()


    btn = QPushButton(root)
    btn.setGeometry(0, 0, 100, 100)
    btn.clicked.connect(comparison)
    btn.setStyleSheet("border-radius : 50; background-color : #181818;")
    btn.setIcon(QIcon("D:\\mic343.png"))
    btn.setIconSize(QSize(150, 150))
    btn.move(580, 625)
    btn.show()

    movie = QtGui.QMovie("D:\\gif22.gif")
    label.setMovie(movie)
    movie.start()

    root.show()
    wishMe()
    speak("i am terminal x at your service. how can i help you")
    sys.exit(App.exec_())



