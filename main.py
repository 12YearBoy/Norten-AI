from email.mime import audio
import PyPDF2
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import eel 
import os
import sys
import wikipedia
import webbrowser
import pywhatkit as kit
import time
from PyPDF2 import PdfReader
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sympy as sp
from gtts import gTTS















a = pyttsx3.init('sapi5')
voices = a.getProperty('voices')
a.setProperty('voices', voices[0].id)
a.setProperty("rate",150)

def speak(audio):
    a.say(audio)
    print(audio)
    a.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    
    try:
        print("Running....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Hecker Said: {query}")


    except Exception as e:
        speak("")
        return "none"
    return query

def wish():
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        time_msg = "Good Morning"
    elif 12 <= hour < 18:
        time_msg = "Good Afternoon"
    else:
        time_msg = "Good Evening"
    
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    speak(f"{time_msg}. It's {current_time}. Norten is now Activated")

def play_song_on_youtube():
    speak("Which song do you want to play on YouTube?")
    song_name = takecommand()
    if song_name:
        speak(f"Playing {song_name} on YouTube.")
        kit.playonyt(song_name)
    else:
        speak("Sorry, I couldn't understand your request.")

def search_on_youtube():
    speak("What do you want to play on YouTube?")
    song_name = takecommand()
    if song_name:
        speak(f"Playing {song_name} on YouTube.")
        kit.playonyt(song_name)
    else:
        speak("Sorry, I couldn't understand your request.")

def search_on_google():
    speak("What do you want to search on Google?")
    query = takecommand()
    if query:
        search_url = f"https://www.google.com/search?q={query}"
        speak(f"Searching on Google.")
        webbrowser.open(search_url)
    else:
        speak("Sorry, I couldn't understand your request.")

def parse_time(time_str):
    time_units = {"second": 1, "seconds": 1, "minute": 60, "minutes": 60, "hour": 3600, "hours": 3600}
    for unit, value in time_units.items():
        if unit in time_str:
            return int(time_str.split()[0]) * value
    return None

def set_alarm(duration):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    while datetime.datetime.now() < end_time:
        time.sleep(1)  # Check every second
    speak("Wake up! your alarm had been Finished")
   
def get_current_time():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%I:%M %p")  # Format time as "hour:minute AM/PM"
    return time_str

def process_query(query):
    if "what is the time" in query:
        current_time = get_current_time()
        speak(f"The current time is {current_time}.")
    else:
        speak("I'm sorry, I didn't understand that.")


recognizer = sr.Recognizer()

def answer_math_questions():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    speak("Sure, Tell me your Maths problem.. Say thankyou when your questions are done")

    while True:
        try:
            
            with sr.Microphone() as source:
                speak("whats your next question ?")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source)
                # Listen to the user's question
                audio = recognizer.listen(source)
            
            # Convert the audio to text
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            
            # Check if the user wants to exit
            if "thank" in user_input.lower():
                engine.say("You're welcome! Have a great day!")
                engine.runAndWait()
                break
            
            # Evaluate the math question
            solution = eval(user_input)

            # Speak the solution
            engine.say(f"The answer is {solution}")
            engine.runAndWait()
        
        except Exception as e:
            print("Error:", e)


def store_and_retrieve_data():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate (speed) of speech to a lower value
    engine.setProperty('rate', 150)  # You can adjust this value to your preference

    data = {}  # Dictionary to store user data

    while True:
        try:
            while True:
                with sr.Microphone() as source:
                    speak("Please provide a label for the data (or say 'exit' to stop providing labels):")
                    # Adjust for ambient noise
                    recognizer.adjust_for_ambient_noise(source)
                    # Listen to the user's input
                    audio = recognizer.listen(source)
                
                # Convert the audio to text
                label = recognizer.recognize_google(audio)
                print("Label:", label)

                if "exit" in label.lower():
                    break  # Exit the label input loop if the user says 'exit'

                with sr.Microphone() as source:
                    speak(f"Please provide the data for {label}:")
                    # Adjust for ambient noise
                    recognizer.adjust_for_ambient_noise(source)
                    # Listen to the user's input
                    audio = recognizer.listen(source)
                
                # Convert the audio to text
                data_text = recognizer.recognize_google(audio)
                print("Data:", data_text)
                
                # Try converting the data to a number
                try:
                    data_text = float(data_text)
                except ValueError:
                    pass  # If it's not a number, leave it as text
                
                # Store the data with the given label
                data[label] = data_text
                speak("Data stored successfully!")
            
            break  # Exit the main loop after storing data
        
        except Exception as e:
            print("Error:", e)

    # Now, let's implement the function to retrieve and speak the stored data
    def retrieve_data(label):
        if label in data:
            engine.say(f"The data for {label} is {data[label]}")
            engine.runAndWait()
        else:
            engine.say(f"Sorry, no data found for {label}")
            engine.runAndWait()

    # Return the function for later use
    return retrieve_data








# class MainThread(QThread):
#     def __init__():
#         super(MainThread,self)



    
# def pdf_reader():
#     book = open('D:\\Ash_\\JS Notes.pdf','rd')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     speak(f"Total numbers of pages in this book {pages}  ")
#     speak("Sir please enter the page number i have to read")
#     pg = int(input("Please Entre the page number: "))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     speak(text)

if __name__ == "__main__":
    
    # speak("This is Norten, the Advance A I Version 1.1 Created by Hecker. Enter password to activate")
    # userPassword = input("Enter the password: ")

    # if userPassword != "beluga":
    # # print("Wrong password. You are kicked out")
    #     speak("Wrong password. You are kicked out")
    #     exit()
    # else:
    # # print("Norten is Now Activated. How can I help you, Sir?")
    #     wish()
    #     speak("How can I help you Sir ?")




    
    while True:
        query = takecommand().lower()

    # Logic Building

        if "open my file" in query:
            fpath = "D:\\Hecker\\The Kind Stuff"
            os.startfile(fpath)

        elif "open cmd" in query:
            speak("done")
            dpath = "C:\Program Files\Google\Chrome\Application"
            os.system("start cmd")

        elif "play blinding lights" in query:
            speak("done")
            dpath = "C:\Program Files\Google\Chrome\Application"
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif "play under the influence" in query:
            speak("done")
            dpath = "C:\Program Files\Google\Chrome\Application"
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[6]))

        elif "open youtube" in query:
            speak("Opening Youtube Sir")
            search_on_youtube()
        
        elif "play songs on youtube" in query:
            play_song_on_youtube()
               
        elif "shutdown"  in query:
            speak("Have a Good Day. Norten is going offline")
            sys.exit()

        elif "search on google" in query:
            search_on_google()

        elif "set alarm" in query:
            if "set alarm" in query:
                speak("Sure, how long should I set the alarm for?")
                time_str = takecommand()
                duration = parse_time(time_str)
                if duration is not None:
                    speak(f"Alarm set for {duration} seconds.")
                    set_alarm(duration)
                    
                else:
                    speak("Sorry, I couldn't understand the duration.")
            elif "stop alarm" in query:
                speak("Alarm stopped.")
                break
          
        elif "what is the time" in query:
                process_query(query)
   
        elif "go to sleep" in query:
            speak("Norten is going to Sleep. Call me when you want Sir.")


        elif "wake up Norton" in query:
            speak("Norten is activated. How can I help you ?")

        elif "solve my maths problem" in query:
            answer_math_questions()

        elif "store my data" in query:
            
# Example usage:
            retrieve_data_func = store_and_retrieve_data()

            # Now, you can ask for the stored data
            while True:
                try:
                    with sr.Microphone() as source:
                        speak("Ask for data (or say 'exit' to stop):")
                        # Adjust for ambient noise
                        recognizer.adjust_for_ambient_noise(source)
                        # Listen to the user's input
                        audio = recognizer.listen(source)
                    
                    # Convert the audio to text
                    question = recognizer.recognize_google(audio)
                    print("You asked:", question)

                    if "exit" in question.lower():
                        speak("Done ")
                        break

                    retrieve_data_func(question)
                
                except Exception as e:
                    print("Error:", e)

        
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)
        

        
        


                
            
         
        
        




    
        
    















           

