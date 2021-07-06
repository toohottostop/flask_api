import datetime
from functools import wraps

from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from werkzeug.security import check_password_hash
import jwt

from src.database.models import User
from src.schemas.users import UserSchema
from src import db, app
from sqlalchemy.exc import IntegrityError


class AuthRegister(Resource):
    user_schema = UserSchema()

    def post(self):
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as exc:
            return {"message": str(exc)}
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as exc:
            db.session.rollback()
            return {"message": "User already exists"}, 409
        return self.user_schema.dump(user), 201


class AuthLogin(Resource):

    def get(self):
        auth = request.authorization
        if not auth:
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required', charset='UTF-8'"}
        user = db.session.query(User).filter_by(username=auth.get("username", "")).first()
        if not user or not check_password_hash(user.password, auth.get("password", "")):
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required', charset='UTF-8'"}
        token = jwt.encode(
            {
                "user_id": user.uuid,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=2)
            }, app.config["SECRET_KEY"]
        )
        return jsonify(
            {
                "token": token
            }
        )


def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        token = request.headers.get("X-API-KEY", "")
        if not token:
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required', charset='UTF-8'"}
        try:
            uuid = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])["user_id"]
        except (KeyError, jwt.ExpiredSignatureError):
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required', charset='UTF-8'"}
        user = db.session.query(User).filter_by(uuid=uuid).first()
        if not user:
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required', charset='UTF-8'"}
        return func(self, *args, **kwargs)

    return wrapper
