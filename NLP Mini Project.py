import os
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

recommendations = {
    "movie": ["Inception", "Interstellar", "The Matrix"],
    "book": ["1984", "Brave New World", "Fahrenheit 451"],
    "music": ["Bohemian Rhapsody", "Imagine", "Hotel California"]
}

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said", text)
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Google Speech service is unavailable.")
        return ""

def recommend_based_on_input(user_input):
    for category in recommendations:
        if category in user_input:
            items = recommendations[category]
            return f"I recommend these {category}s {','.join(items)}", items

    return "Sorry, I don't have recommendations for that."

while True:
    user_text = get_voice_input()
    if "exit" in user_text or "quit" in user_text:
        speak("Goodbye!")
        break
    response, suggestion = recommend_based_on_input(user_text)
    print(suggestion)
    speak(response)
    #
    # for thing in suggestion:
    #     print(thing)
    #     tts_engine.say(thing)
    #     tts_engine.runAndWait()

