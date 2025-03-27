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
from wikipediaHandler import WikipediaClass

import datetime

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
            tts.speak(gptChat.chat_with_gpt("Goodbye Terandelle!"))
            break

        # Weather information
        elif "weather" in query:
            tts.speak(gptChat.chat_with_gpt("Could you please ask me which city i would like to know the weather for?"))
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

        elif "wikipedia" in query:
            wikipedia = WikipediaClass()
            tts.speak(gptChat.chat_with_gpt("Ask me what I would like to know about from Wikipedia."))
            request_topic = speechRecog.recognize_speech()
            wiki = wikipedia.wikipediaDefine(request_topic)
            if wiki is not None:
                defineTextList = wiki.split(".")
                # loop through input:lines, or fewer lines in the return if there are fewer than input:lines lines in it
                for i in range(0, min(len(defineTextList) + 1, 4)):
                    print("line: " + str(i))
                    tts.speak(defineTextList[i])

        elif "time" in query:
            tts.speak(gptChat.chat_with_gpt(f"Could you please tell me that the time is {str(datetime.datetime.now().strftime("%H:%M"))}, though say it differently?"))

        # Calendar and Todo list management
        elif "calendar" in query or "to-do" in query:
            todo = Todo()
            response = todo.manage_calendar_and_todo(query)
            tts.speak(response)

        elif "thank you" in query or "thanks" in query:
            tts.speak(gptChat.chat_with_gpt(query))

        elif "what can you do" in query:
            tts.speak(gptChat.chat_with_gpt("please explain to me that you can pull weather information, "
                                            "the news, "
                                            "wikipedia articles, "
                                            "tell the time, "
                                            "manage me to-do list, "
                                            "and chat using chat gpt, briefly explaining that you can."))

        # Interactive conversation
        elif "chat" in query or "talk" in query:
            tts.speak(gptChat.chat_with_gpt(query))
            while True:
                user_input = speechRecog.recognize_speech()
                if user_input is not None and (
                        "exit" in user_input.lower() or "quit" in user_input.lower() or "stop" in user_input.lower()):
                    tts.speak(gptChat.chat_with_gpt("Goodbye!"))
                    break

                if user_input:
                    response = gptChat.chat_with_gpt(user_input)
                    tts.speak(response)

        # Fallback for unclear commands
        else:
            tts.speak(gptChat.chat_with_gpt("Respond as if you didn't quite understand the last thing I said, it's not a command you understand."))


if __name__ == "__main__":
    main()
    log.log("done\n\n")
