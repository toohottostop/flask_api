from typing import List

from flask_restful import Resource
from flask import request


def get_all_bikes():
    return [
        {
            "id": "1",
            "model": "Norco Rampage",
            "riding_style": "Freeride",
            "price": "50000",
        },
        {
            "id": "2",
            "model": "Specialized Demo",
            "riding_style": "Downhill",
            "price": "100000",
        },
        {
            "id": "3",
            "model": "Norco 250",
            "riding_style": "Street",
            "price": "30000",
        },
        {
            "id": "4",
            "model": "NS Majesty",
            "riding_style": "Park",
            "price": "30000",
        },
        {
            "id": "5",
            "model": "NS Soda",
            "riding_style": "Slopestyle",
            "price": "80000",
        }
    ]


def get_bike_by_uuid(uuid: str) -> dict:
    bikes = get_all_bikes()
    bike = list(filter(lambda b: b["id"] == uuid, bikes))
    return bike[0] if bike else {}


def create_bike(bike_json: dict) -> List[dict]:
    bikes = get_all_bikes()
    bikes.append(bike_json)
    return bikes


class BikesListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            bikes = get_all_bikes()
            return bikes, 200
        bike = get_bike_by_uuid(uuid)
        if not bike:
            return "", 404
        return bike, 200

    def post(self):
        bike_json = request.json
        return create_bike(bike_json), 201

    def put(self):
        return get_all_bikes()

    def patch(self):
        return get_all_bikes()
