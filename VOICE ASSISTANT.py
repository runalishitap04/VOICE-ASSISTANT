import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi, I am your personal assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that. Can you repeat?")
        return ""
    return query.lower()

def run_assistant():
    greet_user()
    while True:
        command = take_command()

        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {current_time}")

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'play music' in command:
            music_dir = 'C:\\Users\\Public\\Music'  # Change path as needed
            songs = os.listdir(music_dir)
            if songs:
                speak("Playing music")
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        else:
            speak("I can search that for you")
            webbrowser.open(f"https://www.google.com/search?q={command}")

# Start the assistant
run_assistant()
