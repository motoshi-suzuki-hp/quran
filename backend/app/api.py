import json
from flask import Blueprint, request, jsonify, Response, send_from_directory
from app.application import PronunciationAnalyzer
from app.infrastructure import HuggingFaceModel
from app.repository import DatabaseRepository
from app.repository.user_repository import UserRepository

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

@api.route("/<int:surah_id>/<int:ayah_id>", methods=["GET"])
def get_pronunciation_record(surah_id, ayah_id):

    try:
        database_repository = DatabaseRepository()
        # レコードの取得
        record = database_repository.get_record_by_surah_ayah(surah_id, ayah_id)
        if not record:
            return jsonify({"error": "Not Found", "message": f"Record with Surah ID {surah_id} and Ayah ID {ayah_id} not found"}), 404
        # レスポンスを構築
        
        result = {
            "id": record["id"],
            "text": record["text"],
            "phoneme": record["phoneme"],
            "audio_path": record["audio_path"]
        }

        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
    
@api.route("/<int:surah_id>", methods=["GET"])
def get_pronunciation_records(surah_id):

    try:
        database_repository = DatabaseRepository()
        # レコードの取得
        records = database_repository.get_records_by_surah(surah_id)
        if not records:
            return jsonify({"error": "Not Found", "message": f"Record with Surah ID {surah_id} not found"}), 404
        # レスポンスを構築
        
        result = [
            {
                "id": record["id"],
                "ayah_id": record["ayah_id"],
                "text": record["text"],
                "phoneme": record["phoneme"]
            }
            for record in records
        ]

        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
    
@api.route("/", methods=["GET"])
def get_all_pronunciation_records():

    try:
        database_repository = DatabaseRepository()
        # レコードの取得
        records = database_repository.get_records()
        if not records:
            return jsonify({"error": "Not Found", "message": "Records not found"}), 404
        # レスポンスを構築
        result = [
            {
                "id": record["id"],
                "surah_id": record["surah_id"],
                "ayah_id": record["ayah_id"],
                "text": record["text"],
                "phoneme": record["phoneme"]
            }
            for record in records
        ]

        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
    
@api.route("/<int:audio_id>", methods=["GET"])
def get_audio_metadata(audio_id):
    db = DatabaseRepository()
    metadata = db.get_audio_metadata_by_id(audio_id)

    if not metadata:
        return jsonify({"error": "Audio not found"}), 404

    return jsonify(metadata), 200

@api.route('/media/audio/<path:filename>', methods=["GET"])
def serve_audio(filename):
    return send_from_directory('media/audio', filename)
