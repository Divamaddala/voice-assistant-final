🎤 GPT-Based Smart Voice Assistant
An intelligent voice-controlled assistant leveraging OpenAI's GPT model to understand and respond to user queries in natural language. This assistant provides seamless interaction through advanced speech recognition and text-to-speech conversion capabilities.
🌟 Features

🎙️ Voice Recognition - Converts speech to text using Google Speech Recognition
🤖 AI-Powered Responses - Integrates with OpenAI GPT-4 for intelligent conversations
🔊 Text-to-Speech - Natural voice output using pyttsx3
🌐 Web Automation - Opens websites (YouTube, Google, GitHub) via voice commands
📅 Information Queries - Get current time, date, and Wikipedia searches
💬 Natural Conversation - Handles general questions and casual chat
🔒 Secure - API keys properly managed and excluded from version control

🎥 Demo
User: "Hello, how are you?"
Assistant: "Hello! I'm your voice assistant. How can I help you today?"

User: "Open YouTube"
Assistant: "Opening YouTube" [Opens YouTube in browser]

User: "What time is it?"
Assistant: "The current time is 3:45 PM"

User: "Tell me about artificial intelligence"
Assistant: [Provides detailed AI explanation from GPT-4]
📋 Prerequisites
Before running this application, make sure you have:

Python 3.7+ installed
OpenAI API key from OpenAI Platform
Microphone and speakers/headphones
Stable internet connection

🚀 Quick Start
1. Clone the Repository
bashgit clone https://github.com/Divamaddala/voice-assistant-final.git
cd voice-assistant-final
2. Install Dependencies
bashpip install -r requirements.txt
Note for Windows users: If you encounter PyAudio installation issues:
bashpip install pipwin
pipwin install pyaudio
Note for macOS users: You might need to install PortAudio first:
bashbrew install portaudio
pip install pyaudio
3. Setup OpenAI API Key

Get your API key from OpenAI Platform
Create a file named apikey.py in the project root
Add your API key:

pythonapi_data = "sk-your-actual-api-key-here"
4. Run the Assistant
bashpython main.py
Wait for the greeting message, then start speaking your commands!
🎯 Available Commands
CommandDescriptionExampleBrowser ControlOpen websites"Open YouTube", "Open Google"Time & DateGet current information"What time is it?", "What's the date?"Wikipedia SearchSearch Wikipedia"Wikipedia artificial intelligence"General QuestionsAsk anything"Tell me a joke", "Explain quantum physics"ExitClose the assistant"Bye", "Goodbye", "Exit"
🏗️ Project Structure
voice-assistant-final/
├── main.py              # Main application with voice assistant logic
├── app.py              # Web version for deployment (Flask)
├── requirements.txt    # Python dependencies
├── .gitignore         # Files to ignore in version control
└── README.md          # Project documentation
🔧 Technical Details
Core Technologies

OpenAI GPT-4 - Natural language understanding and generation
SpeechRecognition - Converting speech to text
pyttsx3 - Text-to-speech conversion
webbrowser - Web automation capabilities

Architecture

Audio Input → Speech Recognition → Text
Text Processing → OpenAI GPT-4 → Response
Response → Text-to-Speech → Audio Output

Key Classes and Functions

VoiceAssistant - Main assistant class
listen() - Captures and processes audio input
get_gpt_response() - Interfaces with OpenAI API
speak() - Converts text to speech
process_command() - Handles specific commands

🛠️ Configuration
Voice Settings
Modify TTS properties in the __init__ method:
pythonself.engine.setProperty('rate', 180)    # Speech speed
self.engine.setProperty('volume', 0.9)  # Volume level
Recognition Settings
Adjust speech recognition parameters:
pythonself.recognizer.pause_threshold = 1     # Pause detection
# Timeout and phrase limits in listen() method
GPT Model Configuration
Change the model or parameters in get_gpt_response():
pythonmodel = "gpt-4o"  # or "gpt-3.5-turbo" for cost efficiency
max_tokens = 150  # Response length limit
temperature = 0.7 # Response creativity (0.0-1.0)
🔍 Troubleshooting
Common Issues and Solutions
Microphone Not Detected

Check system microphone permissions
Ensure microphone is not muted
Try python -m speech_recognition to test

OpenAI API Errors

Verify your API key is correct
Check your OpenAI account has sufficient credits
Ensure stable internet connection

Audio Output Issues

Check speaker/headphone connections
Verify system audio settings
Try different TTS voices in the code

Import/Installation Errors

Reinstall packages: pip install -r requirements.txt --force-reinstall
For PyAudio issues, see installation notes above
Check Python version compatibility (3.7+)

Speech Recognition Problems

Speak clearly and at moderate pace
Reduce background noise
Adjust microphone positioning
Check pause_threshold setting

🌐 Deployment Options
Option 1: Local Desktop Application

Run directly with python main.py
Create executable with PyInstaller:

bashpip install pyinstaller
pyinstaller --onefile --windowed main.py
Option 2: Web Application

Deploy app.py using Flask to platforms like:

Heroku
Railway
Render
PythonAnywhere



Option 3: Container Deployment
dockerfile# Basic Dockerfile structure
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
🔒 Security Considerations

API Key Protection: Never commit apikey.py to version control
Environment Variables: Use .env files for production deployment
Rate Limiting: Monitor OpenAI API usage to avoid unexpected charges
Input Validation: The assistant processes all voice input through OpenAI

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository
Create a feature branch: git checkout -b feature/amazing-feature
Commit your changes: git commit -m 'Add amazing feature'
Push to the branch: git push origin feature/amazing-feature
Open a Pull Request

Ideas for Contributions

Add support for multiple languages
Implement weather API integration
Add calendar/scheduling features
Improve error handling
Add unit tests
Create GUI interface

📈 Performance & Optimization
Tips for Better Performance

Use gpt-3.5-turbo instead of gpt-4 for faster responses
Implement response caching for common queries
Adjust max_tokens based on your needs
Use environment variables for configuration

Cost Optimization

Monitor token usage in OpenAI dashboard
Set spending limits on your OpenAI account
Cache responses for repeated queries
Use shorter system prompts

📚 Learning Resources

OpenAI API Documentation
SpeechRecognition Library Guide
pyttsx3 Documentation
Python Speech Recognition Tutorial

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

OpenAI for providing the GPT API
Google for Speech Recognition services
Python Speech Recognition community
pyttsx3 developers for text-to-speech capabilities

📧 Contact & Support

GitHub Issues: Report bugs or request features
Project Repository: voice-assistant-final


🚀 Quick Commands Reference
bash# Setup
git clone https://github.com/Divamaddala/voice-assistant-final.git
cd voice-assistant-final
pip install -r requirements.txt

# Create API key file
echo 'api_data = "your-api-key-here"' > apikey.py

# Run
python main.py
Made with ❤️ by Divamaddala
