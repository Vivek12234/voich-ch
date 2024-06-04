import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("User said:", command)
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        command = None

    return command

def process_command(command):
    if command:
        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "search" in command:
            query = command.split("search", 1)[1].strip()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}.")
        elif "exit" in command:
            speak("Goodbye!")
            exit()
        else:
            speak("I'm sorry, I don't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! How can I help you?")
    while True:
        command = get_command()
        if command:
            command = command.lower()
            process_command(command)
