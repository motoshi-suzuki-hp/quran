import json
from flask import Blueprint, request, jsonify, Response
from app.application import PronunciationAnalyzer
from app.infrastructure import HuggingFaceModel
from app.repository import DatabaseRepository

api = Blueprint("api", __name__)

# ユースケースの初期化
analyzer = PronunciationAnalyzer(
    model_name="jonatasgrosman/wav2vec2-large-xlsr-53-arabic"
)

@api.route("/analyze", methods=["POST"])
def analyze():
    audio_file = request.files.get("audio")
    expected_text = request.form.get("text")

    if not audio_file or not expected_text:
        return jsonify({"error": "Invalid request", "message": "音声ファイルとテキストを提供してください。"}), 400

    return analyzer.evaluate_pronunciation(audio_file, expected_text)

@api.route("/<int:id>", methods=["GET"])
def get_pronunciation_record(id):

    try:
        database_repository = DatabaseRepository()
        # レコードの取得
        record = database_repository.get_record_by_id(id)
        if not record:
            return jsonify({"error": "Not Found", "message": f"Record with ID {id} not found"}), 404
        # レスポンスを構築
        
        result = {
            "text": record["text"],
            "phoneme": record["phoneme"]
        }

        # return Response(
        #     response=json.dumps(result, ensure_ascii=False),
        #     status=200,
        #     mimetype="application/json"
        # )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500