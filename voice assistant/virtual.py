import speech_recognition as sr
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import spacy
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
openweather_api_key = os.getenv('OPENWEATHER_API_KEY')

# Initialize spacy model
nlp = spacy.load('en_core_web_sm')

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I could not understand. Please try again.")
        return None

    return query

# Function to respond to greeting
def respond_to_greeting(query):
    if 'hello' in query.lower():
        return "Hello! How can I help you today?"

# Function to tell time or date
def tell_time_or_date(query):
    if 'time' in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    elif 'date' in query.lower():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}"

# Function for basic web search using Google Custom Search API
def basic_web_search(query):
    if 'search for' in query.lower():
        search_term = query.split("search for")[-1].strip()
        print(f"Searching the web for {search_term}...")

        # Google Custom Search API
        api_key = google_api_key
        cx = '73ec56484f22d4423'
        endpoint = "https://www.googleapis.com/customsearch/v1"
        params = {"q": search_term, "key": api_key, "cx": cx}

        response = requests.get(endpoint, params=params)
        results = response.json()

        # Extracting and displaying top 3 results
        items = results.get("items", [])
        if items:
            response = ""
            for i, item in enumerate(items[:3]):
                response += f"Result {i+1}:\nTitle: {item['title']}\nURL: {item['link']}\nSnippet: {item['snippet']}\n\n"
            return response
        else:
            return "No results found."

# Function to process natural language queries
def process_query(query):
    doc = nlp(query)
    return doc

# Function to send email
def send_email(to_address, subject, body):
    from_address = "your_email@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

    return "Email has been sent!"

# Function to get weather information
def get_weather(city):
    api_key = openweather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    print("API Response:", json.dumps(data, indent=4))  # Print the response for debugging

    # Check for error codes or unexpected responses
    if 'cod' in data:
        if data['cod'] == 200:
            main = data.get('main', {})
            weather = data.get('weather', [{}])[0]
            temperature = main.get('temp', 'N/A')
            weather_description = weather.get('description', 'No description available')
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        elif data['cod'] == '404':
            return "City not found."
        else:
            return f"Error {data['cod']}: {data.get('message', 'Unknown error occurred.')}"
    else:
        return "Unexpected response format from the weather API."


# Main function for advanced voice assistant
def advanced_voice_assistant():
    while True:
        query = recognize_speech()
        if query:
            doc = process_query(query)
            response = None
            
            if 'hello' in query.lower():
                response = "Hello! How can I assist you today?"
            elif 'time' in query.lower():
                response = tell_time_or_date(query)
            elif 'date' in query.lower():
                response = tell_time_or_date(query)
            elif 'search for' in query.lower():
                response = basic_web_search(query)
            elif 'send email' in query.lower():
                # Example: "Send email to example@example.com about Meeting with body Let's meet at 5 PM"
                parts = query.split(" ")
                to_address = parts[3]
                subject = parts[5]
                body = " ".join(parts[7:])
                response = send_email(to_address, subject, body)
            elif 'weather in' in query.lower() or 'weather for' in query.lower():
                # Extract city name from the query
                city = query.split("in")[-1].strip() if 'in' in query.lower() else query.split("for")[-1].strip()
                response = get_weather(city)
            
            if response:
                print(response)
            else:
                print("Sorry, I didn't understand that.")
            
            if 'exit' in query.lower():
                break

if __name__ == "__main__":
    advanced_voice_assistant()
