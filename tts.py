# tts
"""
implementations for text to speech
"""

from gtts import gTTS
from audioplayer import AudioPlayer

from logHandler import Logger

log = Logger(True, "tts")

class TTS:
    def __init__(self):
        pass

    # Function to speak text
    def speak(self, text):
        log.log(f"starting tts of {text}")
        tts = gTTS(text=text, lang='en', slow=False, tld='ru')
        log.log("saving tts file")
        tts.save("voice.mp3")
        log.log("playing tts file")
        AudioPlayer("voice.mp3").play(block=True)

