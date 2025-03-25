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
    def speak(self, text):
        tts = gTTS(text=text, lang='en', slow=False, tld="ru")
        tts.save("voice.mp3")
        AudioPlayer("voice.mp3").play(block=True)

