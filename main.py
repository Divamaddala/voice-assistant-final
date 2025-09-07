"""
GPT-Based Smart Voice Assistant
Interactive voice-controlled assistant using OpenAI's GPT model
"""

from openai import OpenAI
from apikey import api_data 
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import requests
import json

# Configuration
MODEL = "gpt-4o"
client = OpenAI(api_key=api_data)

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant with TTS engine"""
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        
        # Set voice properties
        if voices:
            self.engine.setProperty('voice', voices[0].id)  # Use first available voice
        self.engine.setProperty('rate', 180)  # Speech rate
        self.engine.setProperty('volume', 0.9)  # Volume level
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice commands and convert to text"""
        with self.microphone as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio, language='en-US')
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                print("Could not understand audio")
                return "none"
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return "none"
            except sr.WaitTimeoutError:
                print("Listening timeout")
                return "none"
    
    def get_gpt_response(self, question):
        """Get response from OpenAI GPT model"""
        try:
            completion = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system", 
                        "content": """You are a helpful voice assistant. Provide concise, 
                        conversational responses. Keep answers brief but informative. 
                        Be friendly and natural."""
                    },
                    {"role": "user", "content": question}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def get_weather(self, city="your location"):
        """Get weather information (placeholder - would need weather API)"""
        return f"I'd need a weather API to get current weather for {city}. This is a placeholder response."
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"
    
    def get_date(self):
        """Get current date"""
        today = datetime.date.today()
        return f"Today is {today.strftime('%A, %B %d, %Y')}"
    
    def search_wikipedia(self, query):
        """Search Wikipedia for information"""
        try:
            # Remove common words
            search_query = query.replace("wikipedia", "").replace("search", "").strip()
            result = wikipedia.summary(search_query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple results found. Please be more specific. Options include: {', '.join(e.options[:3])}"
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{search_query}'"
        except Exception as e:
            return f"Sorry, I couldn't search Wikipedia right now."
    
    def process_command(self, command):
        """Process voice commands and execute appropriate actions"""
        if command == "none":
            return None
        
        # Browser commands
        if "open youtube" in command:
            self.speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            return "Opened YouTube"
        
        elif "open google" in command:
            self.speak("Opening Google")
            webbrowser.open("https://www.google.com")
            return "Opened Google"
        
        elif "open github" in command:
            self.speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
            return "Opened GitHub"
        
        # Time and date commands
        elif "time" in command:
            response = self.get_time()
            self.speak(response)
            return response
        
        elif "date" in command:
            response = self.get_date()
            self.speak(response)
            return response
        
        # Weather command (placeholder)
        elif "weather" in command:
            response = self.get_weather()
            self.speak(response)
            return response
        
        # Wikipedia search
        elif "wikipedia" in command or "search wikipedia" in command:
            response = self.search_wikipedia(command)
            self.speak(response)
            return response
        
        # Exit commands
        elif any(word in command for word in ["bye", "goodbye", "exit", "quit", "stop"]):
            response = "Goodbye! Have a great day!"
            self.speak(response)
            return "EXIT"
        
        # Default: Use GPT for general queries
        else:
            response = self.get_gpt_response(command)
            self.speak(response)
            return response
    
    def run(self):
        """Main execution loop"""
        self.speak("Hello! I'm your voice assistant. How can I help you today?")
        
        while True:
            try:
                command = self.listen()
                result = self.process_command(command)
                
                if result == "EXIT":
                    break
                elif result is None:
                    continue
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.speak("Sorry, I encountered an error. Please try again.")

def main():
    """Main function to start the voice assistant"""
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as e:
        print(f"Failed to start assistant: {e}")

if __name__ == "__main__":
    main()