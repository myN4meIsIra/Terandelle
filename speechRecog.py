# speech recog
"""
speech recognition implementations
"""
import speech_recognition as sr
from tts import TTS

class SpeechRecog:
    def __init__(self):
        pass

    # Function to recognize speech
    def recognize_speech(self):
        tts = TTS()
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                try:
                    query = recognizer.recognize_google(audio, language='en-US')
                    print(f"You said: {query}")
                    return query
                except sr.UnknownValueError:
                    tts.speak("Sorry, I didn't catch that. Could you repeat?")
                    return None
                except sr.RequestError:
                    tts.speak("There was an error with the speech recognition service.")
                    return None
        except AttributeError:
            # Handle the case where PyAudio is missing
            print("Microphone input requires the 'PyAudio' library, which is missing. Please install it to enable this feature.")
            tts.speak("Sorry, I am unable to access the microphone. Please check your audio configuration.")
            return None

