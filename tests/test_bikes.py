import http
import json

import jwt
import datetime
import pytest
from unittest.mock import patch

from src import app, db
from src.database.models import User, Bike
from src.resources.bikes import BikesListApi


class TestBikesResource:
    uuid = []

    @pytest.fixture(name='token_and_bike_uuid')
    def set_test_user_and_create_token(self):
        user = User(
            username="test_user",
            password="test_pass",
            email="test@test1.com"
        )
        bike = Bike(
            model="test_model",
            riding_style="test_style",
            description="test_description",
            release_date=datetime.datetime.strptime("2021-11-08", "%Y-%m-%d"),
            price=10000.0,
            rating=5.0,
        )
        db.session.add(user)
        db.session.add(bike)
        user_id = db.session.query(User).filter_by(username='test_user').first()
        token = jwt.encode({"user_id": user_id.uuid,
                            "exp": datetime.datetime.now() + datetime.timedelta(hours=2)}, app.config["SECRET_KEY"])
        yield token, bike.uuid
        db.session.rollback()

    def test_get_bikes_list(self, token_and_bike_uuid):
        token = token_and_bike_uuid[0]
        client = app.test_client()
        response_bikes = client.get('/bikes', headers={"X-API-KEY": token})

        assert response_bikes.status_code == http.HTTPStatus.OK
        assert response_bikes.headers['Content-Type'] == 'application/json'
        assert b'test_model' in response_bikes.data

    def test_get_one_bike(self, token_and_bike_uuid):
        token, uuid = token_and_bike_uuid[0], token_and_bike_uuid[1]
        client = app.test_client()
        response_bike = client.get(f'/bikes/{uuid}', headers={"X-API-KEY": token})

        assert response_bike.status_code == http.HTTPStatus.OK

    def test_create_bike(self):
        client = app.test_client()
        data = {
            'model': 'Test Model',
            'riding_style': 'Test Style',
            'description': 'Some description',
            'release_date': '2021-01-01',
            'price': 100000.0,
            'rating': 5.0
        }
        response = client.post('/bikes', data=json.dumps(data), content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED
        assert response.json['model'] == 'Test Model'
        self.uuid.append(response.json['uuid'])

    def test_update_bike(self):
        client = app.test_client()
        data = {
            'model': 'Update Test Model',
            'riding_style': 'Update Test Style',
            'description': 'Update Some description',
            'release_date': '2021-01-02',
            'price': 200000.0,
            'rating': 4.95
        }
        response = client.put(f'/bikes/{self.uuid[0]}', data=json.dumps(data), content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        assert response.json['model'] == 'Update Test Model'

    def test_patch_bike(self):
        client = app.test_client()
        url = f'/bikes/{self.uuid[0]}'
        data = {
            'model': 'Patch Test Model',
            'riding_style': 'Patch Test Style',
            'release_date': '2021-03-03',
        }
        response = client.patch(url, data=json.dumps(data), content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        assert response.json['model'] == 'Patch Test Model'

    def test_delete_bike(self):
        client = app.test_client()
        url = f'/bikes/{self.uuid[0]}'
        response = client.delete(url)
        assert response.status_code == http.HTTPStatus.NO_CONTENT
