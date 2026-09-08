# Voice Assistant

## Project Description

The Voice Assistant is a Python-based program that accepts voice commands from the user and responds using speech. It can greet the user, tell the current time and date, and perform web searches.

## Features

- Voice input using microphone
- Speech recognition
- Voice responses using text-to-speech
- Greeting commands
- Tells the current time
- Tells the current date
- Searches the web using Google
- Handles speech recognition errors
- Exit command to stop the assistant

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- datetime
- webbrowser
- time
- PyAudio

## Commands

The following voice commands can be used:

- "Hello" or "Hi" – Gives a greeting
- "What is the time?" – Tells the current time
- "What is the date?" – Tells today's date
- "Search for data science" – Opens Google and searches for data science
- "Bye" – Stops the assistant
- "Exit" – Stops the assistant
- "Stop" – Stops the assistant

## How to Run

1. Install Python.
2. Install the required Python libraries.
3. Open Python IDLE.
4. Open `voice_assistant.py`.
5. Press F5 or select Run → Run Module.
6. Allow microphone access if requested.
7. Speak a supported command when the program displays "Listening...".

## Example

```text
Assistant: Hello! I am your voice assistant.
Assistant: How can I help you?

Listening...
You: hello
Assistant: Hello! Nice to talk to you.

Listening...
You: what is the time?
Assistant: The current time is ...

Listening...
You: what is the date?
Assistant: Today's date is ...

Listening...
You: search for data science
Assistant: Searching for data science
## Error Handling
Handles unclear or unrecognized speech.
Handles speech recognition service errors.
Handles unsupported commands.
Provides helpful responses when the assistant cannot understand the user.
##Learning Outcome

This project helped me understand speech recognition, text-to-speech, Python modules, functions, loops, conditional statements, exception handling, and web browser integration.

##Internship Details

Track: Python Programming
Task: Voice Assistant
Level: Beginner
Organization: Oasis Infobyte