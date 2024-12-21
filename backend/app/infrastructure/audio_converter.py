from pydub import AudioSegment
import os

class AudioConverter:
    @staticmethod
    def convert_to_wav(audio_file) -> str:
        temp_webm_path = "temp_audio.webm"
        temp_wav_path = "temp_audio.wav"
        
        audio_file.save(temp_webm_path)

        try:
            sound = AudioSegment.from_file(temp_webm_path, format="webm")
            sound.export(temp_wav_path, format="wav")
            return temp_wav_path
        finally:
            if os.path.exists(temp_webm_path):
                os.remove(temp_webm_path)
