from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from models import PasswordRules, PasswordVerification
from password import Password


server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Validate Password")
spec.register(server)
CORS(server)


@server.post("/verify")
@spec.validate(body=Request(PasswordRules), resp=Response(HTTP_200=PasswordVerification))
def verify_password():
    verify, no_match = Password(request.context.body.dict()).verify()
    response = PasswordVerification(verify=verify, noMatch=no_match)
    return jsonify(response.dict())
