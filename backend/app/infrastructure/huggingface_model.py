from huggingface_hub import login
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import os

class HuggingFaceModel:
    @staticmethod
    def login_to_huggingface():
        huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
        if not huggingface_token:
            raise EnvironmentError("HUGGINGFACE_TOKEN is not set")
        login(huggingface_token)

    @staticmethod
    def load_model(model_name: str):
        processor = Wav2Vec2Processor.from_pretrained(model_name)
        model = Wav2Vec2ForCTC.from_pretrained(model_name)
        return processor, model
