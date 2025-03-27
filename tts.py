from gtts import gTTS
import io
import vlc  # VLC Python library for audio streaming
from pydub import AudioSegment
import time

from logHandler import Logger
log = Logger(True, "tts")

class TTS:
    def __init__(self):
        pass

    def speak(self, text):
        log.log(f"pulling TTS: {text}")
        tts = gTTS(text=text, lang='en', slow=False, tld='ru')
        log.log("writing to buffer")
        # Save TTS output to a buffer
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)  # Reset buffer to the beginning

        # Save buffer to a temporary file
        log.log("saving to temp file")
        temp_file = "sounds/temp_audio.mp3"
        with open(temp_file, "wb") as temp:
            temp.write(audio_buffer.read())

        log.log("playing audio")
        # Play the temporary file using VLC
        player = vlc.MediaPlayer(temp_file)
        player.play()

        # Ensure playback starts before checking the state
        time.sleep(0.1)

        # Wait for playback to finish by checking the state
        while True:
            state = player.get_state()
            if state in [vlc.State.Ended, vlc.State.Stopped, vlc.State.Error]:
                break
            time.sleep(0.1)  # Poll every 100ms


