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
from logHandler import Logger

log = Logger(True, "main")
import sys

# Main function to handle voice input and interaction
def main():
    tts = TTS()
    gptChat = GPTChat()

    tts.speak(gptChat.chat_with_gpt("Hello Terandelle!"))

    speechRecog = SpeechRecog()
    while True:
        query = speechRecog.recognize_speech()
        if query is None:
            continue

        query = query.lower()


        # Exit the assistant
        if "exit" in query or "quit" in query or "stop" in query:
            tts.speak(gptChat.chat_with_gpt("Goodbye!"))
            sys.exit()
            break

        # Interactive conversation
        elif "chat" in query or "talk" in query:
            tts.speak(gptChat.chat_with_gpt(query))
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



        # Fallback for unclear commands
        else:
            tts.speak(gptChat.chat_with_gpt("You didn't quite understand the last thing I said, could you ask me to repeat it?"))


if __name__ == "__main__":
    main()
    log.log("done\n\n")
