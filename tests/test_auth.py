import base64
import http
import json

from src import db, app
from src.database.models import User


class TestAuthResource:
    CLIENT = app.test_client()
    URL_REGISTER = '/register'
    URL_LOGIN = '/login'
    USER_REGISTER = {
        'username': 'test_username',
        'password': 'password12345',
        'email': 'test@email.com',

    }
    USER_LOGIN = {
        'username': 'test_username',
        'password': 'password12345'
    }
    VALIDATION_ERROR_DATA = {
        'email': 'test@email.com',
    }

    def test_register(self):
        response = self.CLIENT.post(self.URL_REGISTER,
                                    data=json.dumps(self.USER_REGISTER),
                                    content_type='application/json'
                                    )

        assert response.status_code == http.HTTPStatus.CREATED

    def test_user_already_exists(self):
        response = self.CLIENT.post(self.URL_REGISTER,
                                    data=json.dumps(self.USER_REGISTER),
                                    content_type='application/json'
                                    )

        assert response.status_code == http.HTTPStatus.CONFLICT

    def test_validation(self):
        response = self.CLIENT.post(self.URL_REGISTER,
                                    data=json.dumps(self.VALIDATION_ERROR_DATA),
                                    content_type='application/json'
                                    )

        assert response.status_code == http.HTTPStatus.BAD_REQUEST
        assert b'Missing data for required field.' in response.data

    def test_user_login(self):
        message = "test_username:password12345"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)

        auth_headers = {
            'Authorization': f'Basic ' + base64_bytes.decode("UTF-8"),
        }
        response = self.CLIENT.get(self.URL_LOGIN, headers=auth_headers)

        assert response.status_code == http.HTTPStatus.OK
        assert 'token' in response.json
        db.session.query(User).filter_by(username='test_username').delete()
        db.session.commit()
