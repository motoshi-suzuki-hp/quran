from huggingface_hub import login
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import os

class HuggingFaceModel:
    @staticmethod
    def load_model(model_path: str):
        """
        事前にダウンロード済みのモデルディレクトリからプロセッサとモデルを読み込む。
        例: model_path = "./models/wav2vec2-large-xlsr-53-arabic"
        """
        processor = Wav2Vec2Processor.from_pretrained(model_path)
        model = Wav2Vec2ForCTC.from_pretrained(model_path)
        return processor, model
    