from openai import OpenAI
import requests
from datetime import datetime

from speechRecog import SpeechRecog
from tts import TTS

# OpenAI API Key (set your API key here)
OPENAI_API_KEY = "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"

# Weather API Key (OpenWeatherMap)
weather_api_key = "75f6c15e22433ed3e7406b24691a0706"

# News API Key (NewsAPI)
news_api_key = "8f0d56d54b4640339d5884c7ebabc166"



# Function to interact with ChatGPT using gpt-3.5-turbo
def chat_with_gpt(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = completion.choices[0].message.content
        return answer
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return "I'm sorry, I couldn't fetch a response right now."


# Function to get weather details
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"The current weather in {city} is {weather_description} with a temperature of {temp}°C."
        else:
            return "I couldn't find the weather for that location. Please try another city."
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return "Unable to get the weather right now."


# Function to get the latest news
def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok" and data["totalResults"] > 0:
            articles = data["articles"][:5]
            news_summary = "Here are the top 5 news headlines: "
            for idx, article in enumerate(articles):
                news_summary += f"\n{idx + 1}. {article['title']}"
            return news_summary
        else:
            return "I couldn't fetch the news at the moment."
    except Exception as e:
        print(f"Error fetching news: {e}")
        return "Unable to get the news right now."


# Placeholder function for calendar and todo integration
def manage_calendar_and_todo(query):
    # You can integrate Google Calendar API or any other service here
    # This is a placeholder for demonstration purposes
    if "add event" in query:
        return "Sure, I can add an event to your calendar. Please provide the details."
    elif "show my events" in query:
        return "Here are your upcoming events: [Placeholder data]"
    elif "add task" in query:
        return "Sure, I can add a task to your to-do list. Please provide the details."
    elif "show my tasks" in query:
        return "Here are your current tasks: [Placeholder data]"
    else:
        return "I'm sorry, I couldn't understand your calendar or to-do request."


# Main function to handle voice input and interaction
def main():
    tts = TTS()
    tts.speak("Good morning")

    speechRecog = SpeechRecog()
    while True:
        query = speechRecog.recognize_speech()
        if query is None:
            continue

        query = query.lower()

        # Exit the assistant
        if "exit" in query or "quit" in query or "stop" in query:
            tts.speak("Goodbye! Have a great day!")
            break

        # Interactive conversation
        elif "chat" in query or "talk" in query:
            tts.speak("What would you like to talk about?")
            user_input = speechRecog.recognize_speech()
            if user_input:
                response = chat_with_gpt(user_input)
                tts.speak(response)

        # Weather information
        elif "weather" in query:
            tts.speak("Which city's weather would you like to know?")
            city = speechRecog.recognize_speech()
            if city:
                weather_info = get_weather(city)
                tts.speak(weather_info)

        # News update
        elif "news" in query:
            news = get_news()
            tts.speak(news)

        # Calendar and Todo list management
        elif "calendar" in query or "to-do" in query:
            response = manage_calendar_and_todo(query)
            tts.speak(response)

            # Exit the assistant
        elif "exit" in query or "quit" in query or "stop" in query:
            tts.speak("Goodbye! Have a great day!")
            break

        # Fallback for unclear commands
        else:
            tts.speak("I'm sorry, I didn't understand that. Can you please repeat?")


if __name__ == "__main__":
    main()
