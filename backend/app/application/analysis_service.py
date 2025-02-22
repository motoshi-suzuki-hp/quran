from flask import jsonify
import torch
import librosa
import soundfile as sf
from domain.exceptions import AudioRecognitionError
from domain.services.evaluation import EvaluationService
from infrastructure.services.audio_converter import AudioConverter
from infrastructure.services.huggingface_model import HuggingFaceModel

class AnalysisService:
    def __init__(self, model_path: str):
        # 事前ダウンロードしたモデルディレクトリからロードする
        self.processor, self.model = HuggingFaceModel.load_model(model_path)

    def evaluate_pronunciation(self, audio_file, expected_text, user_id, surah_id, ayah_id):
        try:
            # AudioConverterで変換・保存時にユニークなファイル名を付与する処理を利用
            audio_wave_file = AudioConverter.convert_to_wav(audio_file, user_id, surah_id, ayah_id)
            audio_data, sample_rate = sf.read(audio_wave_file)

            if sample_rate != 16000:
                audio_data = librosa.resample(audio_data, orig_sr=sample_rate, target_sr=16000)
            input_values = self.processor(audio_data, sampling_rate=16000, return_tensors="pt").input_values
            with torch.no_grad():
                logits = self.model(input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = self.processor.decode(predicted_ids[0])

            if transcription.strip() == "":
                raise AudioRecognitionError("音声認識に失敗しました。")

            predicted_phonemes = EvaluationService.text_to_phonemes(transcription)
            expected_phonemes = EvaluationService.text_to_phonemes(expected_text)

            feedback = EvaluationService.evaluate_pronunciation(
                predicted_phonemes, expected_phonemes, transcription, expected_text
            )

            result = {
                "user_id": user_id,
                "recognized_text": transcription.lower(),
                "predicted_phonemes": predicted_phonemes,
                "expected_text": expected_text,
                "expected_phonemes": expected_phonemes,
                "feedback": feedback,
            }
            return jsonify(result)
        except AudioRecognitionError as e:
            return jsonify({"error": "Audio Recognition Error", "message": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
