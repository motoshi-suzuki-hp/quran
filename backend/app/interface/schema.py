from marshmallow import Schema, fields

class AnalyzeRequestSchema(Schema):
    audio = fields.Raw(required=True, description="音声ファイル")
    text = fields.String(required=True, description="期待されるテキスト")

class AnalyzeResponseSchema(Schema):
    recognized_text = fields.String(required=True)
    predicted_phonemes = fields.List(fields.String, required=True)
    expected_text = fields.String(required=True)
    expected_phonemes = fields.List(fields.String, required=True)
    feedback = fields.List(fields.Dict, required=True)
