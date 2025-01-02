from marshmallow import Schema, fields

class SignupRequestSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=False)  # デフォルト 'user'、管理者登録の場合 'admin'

class LoginRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

class RefreshRequestSchema(Schema):
    refresh_token = fields.String(required=True)

class SignupResponseSchema(Schema):
    message = fields.String()
    user_id = fields.Integer()

class LoginResponseSchema(Schema):
    access_token = fields.String()
    refresh_token = fields.String()
    user = fields.Dict()

class MeResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.Email()
    role = fields.String()
