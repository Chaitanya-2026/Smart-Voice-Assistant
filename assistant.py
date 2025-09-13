import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from datetime import datetime


class AssistantController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.client = OpenAI()
        self.chat_history = []  # conversation memory

    def listen(self):
        """Capture audio and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=6)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

    def process(self, user_text):
        """Decide whether to answer locally or ask GPT"""
        # ✅ Built-in commands
        if "time" in user_text.lower():
            now = datetime.now().strftime("%I:%M %p")
            return f"The current time is {now}."
        elif "date" in user_text.lower():
            today = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today's date is {today}."

        # ✅ Otherwise use GPT
        self.chat_history.append({"role": "user", "content": user_text})

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.chat_history
            )
            reply = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Error: {str(e)}"

    def speak(self, text):
        """Convert text to speech"""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
