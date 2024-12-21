from flask import Flask, request, jsonify, Response
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
from phonemizer import phonemize
import soundfile as sf
import librosa
import os
import json
from flask_cors import CORS
from pydub import AudioSegment
import difflib

app = Flask(__name__)
CORS(app)

# Hugging Faceにログイン
from huggingface_hub import login

huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
if huggingface_token:
    login(huggingface_token)
else:
    raise EnvironmentError("HUGGINGFACE_TOKEN is not set")

# 音素解析用のWav2Vec 2.0と音素変換関数の設定
# model = "facebook/wav2vec2-large-960h"

model = "jonatasgrosman/wav2vec2-large-xlsr-53-arabic"
processor = Wav2Vec2Processor.from_pretrained(model)
model = Wav2Vec2ForCTC.from_pretrained(model)

def text_to_phonemes(text):
    phonemes = phonemize(text, language="ar", backend="espeak")
    return phonemes

def evaluate_pronunciation(audio_file, expected_text):
    audio_data, sample_rate = sf.read(audio_file)
    
    if sample_rate != 16000:
        audio_data = librosa.resample(audio_data, orig_sr=sample_rate, target_sr=16000)

    input_values = processor(audio_data, sampling_rate=16000, return_tensors="pt").input_values

    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    if transcription == "":
        predicted_phonemes = []
        expected_phonemes = text_to_phonemes(expected_text).split()
        feedback = []
        feedback.append({
                "position": 0,
                "expected_text": expected_text,
                "expected_phoneme": text_to_phonemes(expected_text),
                "predicted_text": "",
                "predicted_phoneme": "",
                "similarity": 0,
                "message": "音声が認識できませんでした。もう一度お試しください。"
            })
        
        result = {
            "recognized_text": transcription.lower(),
            "phoneme_transcription": predicted_phonemes,
            "expected_text": expected_text,
            "expected_phonemes": expected_phonemes,
            "feedback": feedback,
        }

        return Response(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")


    # 音素のリストを位置ごとに保持する
    predicted_phonemes = text_to_phonemes(transcription).split()
    expected_phonemes = text_to_phonemes(expected_text).split()

    # フィードバックの生成部分を更新
    feedback = []
    for idx, (p_pred, p_exp) in enumerate(zip(predicted_phonemes, expected_phonemes)):
        if p_pred != p_exp:
            message = f"位置 {idx+1} の音素 '{p_pred}' を '{p_exp}' に修正してください。"

            feedback.append({
                "position": idx,
                "expected_text": expected_text.split()[idx],
                "expected_phoneme": p_exp,
                "predicted_text": transcription.split()[idx],
                "predicted_phoneme": p_pred,
                "similarity": grab_gestalt(p_exp, p_pred),
                "message": message
            })

        else:
            feedback.append({
                "position": idx,
                "expected_text": expected_text.split()[idx],
                "expected_phoneme": p_exp,
                "predicted_text": transcription.split()[idx],
                "predicted_phoneme": p_pred,
                "similarity": 100,
                "message": "発音が良好です！"
            })

    if feedback == []:
        feedback.append({
                "position": 0,
                "expected_text": expected_text,
                "expected_phoneme": text_to_phonemes(expected_text),
                "predicted_text": transcription,
                "predicted_phoneme": text_to_phonemes(transcription),
                "similarity": 100,
                "message": "発音が良好です！"
            })

    result = {
        "recognized_text": transcription.lower(),
        "phoneme_transcription": predicted_phonemes,
        "expected_text": expected_text,
        "expected_phonemes": expected_phonemes,
        "feedback": feedback,
    }

    return Response(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")

def grab_gestalt(word1: str, word2: str) -> float:
    distance_float = difflib.SequenceMatcher(None, word1, word2).ratio()*100
    return round(distance_float)

@app.route('/analyze', methods=['POST'])
def analyze():
    print("Request received")
    print("Files:", request.files)
    print("Form data:", request.form)
    
    audio_file = request.files['audio']

    # 一時的にアップロードファイルを保存
    temp_webm_path = "temp_audio.webm"
    audio_file.save(temp_webm_path)

    # 必要に応じてwebmをwav形式に変換
    try:
        sound = AudioSegment.from_file(temp_webm_path, format="webm")
        temp_wav_path = "temp_audio.wav"
        sound.export(temp_wav_path, format="wav")
        print(f"Converted audio saved to {temp_wav_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        return jsonify({"error": "File conversion failed."}), 400
    finally:
        # 一時ファイルを削除（必要に応じて）
        if os.path.exists(temp_webm_path):
            os.remove(temp_webm_path)

    # 変換されたwavファイルで処理を実行
    expected_text = request.form['text']

    result = evaluate_pronunciation(temp_wav_path, expected_text)

    # wavファイルも削除
    if os.path.exists(temp_wav_path):
        os.remove(temp_wav_path)

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)