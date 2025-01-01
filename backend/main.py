from flask import Flask
from flask_cors import CORS
from app.api import api
from app.auth_api import auth
from app.infrastructure import HuggingFaceModel

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/auth")
    # app.config["JSON_AS_ASCII"] = False
    CORS(app)

    # Hugging Faceへのログイン
    HuggingFaceModel.login_to_huggingface()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001)
