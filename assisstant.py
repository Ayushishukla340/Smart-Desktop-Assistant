import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

print("🤖 Assistant started")

while True:
    command = input("👉 Enter command: ").lower()

    # 🔹 BASIC COMMANDS
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Abhi time hai " + time)

    elif "day" in command:
        day = datetime.datetime.now().strftime("%A")
        speak("Aaj din hai " + day)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Aaj ki date hai " + date)

    elif "hello" in command:
        speak("Hello! main tumhari assistant hoon")

    elif "your name" in command:
        speak("Mera naam Python Assistant hai")

    # 🔹 WEB COMMANDS
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("YouTube open kar raha hoon")

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Google open kar raha hoon")

    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Instagram open kar raha hoon")

    elif "maps" in command or "gumna" in command or "travel" in command:
        webbrowser.open("https://www.google.com/maps")
        speak("Google Maps open kar raha hoon, ghoomne chalo ")

    # 🔹 SYSTEM COMMANDS
    elif "open notepad" in command:
        os.system("notepad")
        speak("Notepad open kar raha hoon")

    elif "open calculator" in command:
        os.system("calc")
        speak("Calculator open kar raha hoon")

    # 🔹 EXIT
    elif "exit" in command:
        speak("Bye bye, take care!")
        break

    else:
        speak("Mujhe ye command samajh nahi aayi") 