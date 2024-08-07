# Voice Assistant Project

This is a basic voice assistant project that can perform simple tasks based on voice commands. It includes features such as responding to greetings, telling the time and date, searching the web, and providing weather updates.

## Features

### For Beginners
- Responds to commands like "Hello" with predefined responses.
- Tells the current time or date.
- Searches the web for information based on user queries.

### For Advanced
- Sends emails.
- Sets reminders.
- Provides weather updates.
- Controls smart home devices.
- Answers general knowledge questions.
- Integrates with third-party APIs for additional functionality.

## Requirements

- Python 3.7 or higher
- `speech_recognition` library
- `pyttsx3` library
- `requests` library
- `python-dotenv` library
- `spacy` library and `en_core_web_sm` model

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/voice-assistant-project.git
   cd voice-assistant-project

## Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```bash
   pip install -r requirements.txt

## Create and Configure .env File:


Create a .env file in the root directory.

Add your API keys in the .env file:
```bash
GOOGLE_API_KEY=your_google_api_key
OPENWEATHER_API_KEY=your_openweathermap_api_key


3. download spacy model
```bash
python -m spacy download en_core_web_sm

## Usage
```bash
python main.py

Voice Commands:

Greet the Assistant: Say "Hello" to get a greeting response.
Get Time or Date: Say "What time is it?" or "What's the date today?"
Search the Web: Say "Search for Python language."
Get Weather: Say "Weather for mumbai."

License
This project is licensed under the MIT License. See the LICENSE file for details.
