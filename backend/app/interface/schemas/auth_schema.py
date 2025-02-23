from marshmallow import Schema, fields

class SignupRequestSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    first_language = fields.String(required=True)
    second_language = fields.String(required=False)
    third_language = fields.String(required=False)
    role = fields.String(required=False)

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
    first_language = fields.String()
    second_language = fields.String()
    third_language = fields.String()
    role = fields.String()
