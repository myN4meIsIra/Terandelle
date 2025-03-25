# tts
"""
implementations for text to speech
"""

from gtts import gTTS
from audioplayer import AudioPlayer

class TTS:
    def __init__(self):
        pass

    # Function to speak text
    def speak(text):
        """# Get all voices available in your system
        voices = engine.getProperty('voices')

        print("Available voices:")
        for index, voice in enumerate(voices):
            print(f"Voice {index}:")
            print(f"  - ID: {voice.id}")
            print(f"  - Name: {voice.name}")
            print(f"  - Languages: {voice.languages}")
            print(f"  - Gender: {voice.gender}")
            print(f"  - Age: {voice.age}")


        engine.say(text)
        engine.runAndWait()"""
        tts = gTTS(text=text, lang='en', slow=False, tld="ru")
        tts.save("voice.mp3")
        AudioPlayer("voice.mp3").play(block=True)

