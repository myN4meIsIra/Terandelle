# speech recog
"""
speech recognition implementations
"""
import speech_recognition as sr
from tts import TTS
from gptChat import GPTChat
from logHandler import Logger

log = Logger(True, "speechRecog")

class SpeechRecog:
    def __init__(self):
        pass

    # Function to recognize speech
    def recognize_speech(self):
        tts = TTS()
        log.log("recognizing speech")
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                try:
                    query = recognizer.recognize_google(audio, language='en-US')
                    log.log(f"You said: {query}")
                    return query
                except sr.UnknownValueError:
                    gptChat = GPTChat()
                    tts.speak(gptChat.chat_with_gpt("you didn't quite understand the last thing I said, could you ask me to repeat it?"))
                    return None
                except sr.RequestError:
                    tts.speak("There was an error with the speech recognition service.")
                    return None
        except AttributeError:
            # Handle the case where PyAudio is missing
            log.log("Microphone input requires the 'PyAudio' library, which is missing. Please install it to enable this feature.")
            tts.speak("Sorry, I am unable to access the microphone. Please check your audio configuration.")
            return None

