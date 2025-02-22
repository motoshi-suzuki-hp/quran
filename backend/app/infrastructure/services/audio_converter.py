from pydub import AudioSegment
import os
import datetime

class AudioConverter:
    @staticmethod
    def generate_unique_filename(user_id: int, surah_id: int, ayah_id: int) -> str:
        """
        現在の日時、ユーザーID、Surah、Ayahを組み合わせたユニークなファイル名を生成します。
        例: 200101101010_2_1_1.wav
        """
        now = datetime.datetime.now()
        formatted_date = now.strftime("%y%m%d%H%M%S")
        return f"{formatted_date}_{user_id}_{surah_id}_{ayah_id}.wav"
    
    @staticmethod
    def generate_temporal_filename(user_id: int) -> str:

        return f"temp_audio_{user_id}.wav"

    def convert_to_wav(audio_file, user_id: int, surah_id: int, ayah_id: int) -> str:
        """
        アップロードされた音声ファイルをwebmからwavに変換し、ユニークな名前で保存します。
        保存先は永続的なディレクトリ（例: ./media/yours）とします。
        """
        temp_webm_path = "temp_audio.webm"
        # 一時的なwebmファイルとして保存
        audio_file.save(temp_webm_path)
        
        # ユニークなファイル名を生成
        unique_filename = AudioConverter.generate_unique_filename(user_id, surah_id, ayah_id)
        temporal_filename = AudioConverter.generate_temporal_filename(user_id)
        # 永続的に保存するディレクトリ
        output_dir = "/app/media/yours"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        temporal_output_path = os.path.join(output_dir, temporal_filename)
        output_path = os.path.join(output_dir, unique_filename)
        
        try:
            sound = AudioSegment.from_file(temp_webm_path, format="webm")
            sound.export(temporal_output_path, format="wav")
            sound.export(output_path, format="wav")
            return temporal_output_path
        finally:
            if os.path.exists(temp_webm_path):
                os.remove(temp_webm_path)
