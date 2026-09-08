import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# Initialize speech engine
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said.")
        return ""

    except sr.RequestError:
        speak("Sorry, there is a problem with the speech recognition service.")
        return ""


def main():

    speak("Hello! I am your voice assistant.")
    speak("How can I help you?")

    while True:

        command = listen()

        # Greeting
        if "hello" in command or "hi" in command:
            speak("Hello! Nice to talk to you.")

        # Time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Date
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        # Search
        elif "search" in command:

            search_query = command.replace("search", "")
            search_query = search_query.replace("for", "")
            search_query = search_query.strip()

            if search_query:
                speak("Searching for " + search_query)

                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    search_query.replace(" ", "+")
                )

                # Give time to view and close Google
                time.sleep(8)

            else:
                speak("Please tell me what you want to search.")

        # Exit
        elif "bye" in command or "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        # Unknown command
        else:
            speak("Sorry, I don't know that command yet.")


if __name__ == "__main__":
    main()
