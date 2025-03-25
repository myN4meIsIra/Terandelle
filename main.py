# main
"""
main file
"""

from speechRecog import SpeechRecog
from tts import TTS
from weather import Weather
from todo import Todo
from gptChat import GPTChat
from news import News


# Main function to handle voice input and interaction
def main():
    tts = TTS()
    gptChat = GPTChat()

    tts.speak(gptChat.chat_with_gpt("Hello Terrandelle!"))

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
                response = gptChat.chat_with_gpt(user_input)
                tts.speak(response)

        # Weather information
        elif "weather" in query:
            tts.speak("Which city's weather would you like to know?")
            city = speechRecog.recognize_speech()
            if city:
                weather = Weather()
                weather_info = weather.get_weather(city)
                tts.speak(weather_info)

        # News update
        elif "news" in query:
            news = News()
            theNews = news.get_news()
            tts.speak(theNews)

        # Calendar and Todo list management
        elif "calendar" in query or "to-do" in query:
            todo = Todo()
            response = todo.manage_calendar_and_todo(query)
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
