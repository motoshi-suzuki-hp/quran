from flask import Blueprint, request, jsonify, send_from_directory, g
from interface.http.decorators import token_required
from application.analysis_service import AnalysisService
from infrastructure.persistence.database import DatabaseRepository

api_blueprint = Blueprint("api", __name__)

# 事前ダウンロードしたモデルディレクトリからモデルをロードする
analysis_service = AnalysisService(model_path="./models/wav2vec2-large-xlsr-53-arabic")

@api_blueprint.route("/analyze", methods=["POST"])
@token_required
def analyze():
    # token_required で認証チェック済み、g.user_payload にデコード済み情報が格納されている前提
    user_id = g.user_payload["sub"]

    audio_file = request.files.get("audio")
    expected_text = request.form.get("text")
    surah_id = request.form.get("surah_id")
    ayah_id = request.form.get("ayah_id")

    if not audio_file or not expected_text or not surah_id or not ayah_id:
        return jsonify({
            "error": "Invalid request", 
            "message": "音声ファイルとテキスト、surah_id、ayah_idを提供してください。"
        }), 400

    # analysis_service 内でファイル変換時にユニークなファイル名生成等の処理を実施
    return analysis_service.evaluate_pronunciation(audio_file, expected_text, user_id, surah_id, ayah_id)

@api_blueprint.route("/<int:surah_id>/<int:ayah_id>", methods=["GET"])
@token_required
def get_pronunciation_record(surah_id, ayah_id):
    try:
        db = DatabaseRepository()
        record = db.get_record_by_surah_ayah(surah_id, ayah_id)
        if not record:
            return jsonify({
                "error": "Not Found", 
                "message": f"Record with Surah ID {surah_id} and Ayah ID {ayah_id} not found"
            }), 404
        result = {
            "id": record["id"],
            "text": record["text"],
            "phoneme": record["phoneme"],
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500

@api_blueprint.route("/<int:surah_id>", methods=["GET"])
def get_pronunciation_records(surah_id):
    try:
        db = DatabaseRepository()
        records = db.get_records_by_surah(surah_id)
        if not records:
            return jsonify({
                "error": "Not Found", 
                "message": f"Record with Surah ID {surah_id} not found"
            }), 404
        result = [{
            "id": record["id"],
            "ayah_id": record["ayah_id"],
            "text": record["text"],
            "phoneme": record["phoneme"]
        } for record in records]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500

@api_blueprint.route("/", methods=["GET"])
def get_all_pronunciation_records():
    try:
        db = DatabaseRepository()
        records = db.get_records()
        if not records:
            return jsonify({"error": "Not Found", "message": "Records not found"}), 404
        result = [{
            "id": record["id"],
            "surah_id": record["surah_id"],
            "ayah_id": record["ayah_id"],
            "text": record["text"],
            "phoneme": record["phoneme"]
        } for record in records]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500

@api_blueprint.route('/media/audio/<path:filename>', methods=["GET"])
def serve_audio(filename):
    return send_from_directory('/app/media/audio', filename)

@api_blueprint.route('/media/yours/<path:filename>', methods=["GET"])
def serve_your_audio(filename):
    return send_from_directory('/app/media/yours', filename)
