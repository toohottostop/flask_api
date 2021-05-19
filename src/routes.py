import datetime
from typing import List

from flask_restful import Resource
from flask import request
from src import api, db
from src.models import Bike


class BikesListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            bikes = db.session.query(Bike).all()
            return [bike.to_dict() for bike in bikes], 200
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        return bike.to_dict(), 200

    def post(self):
        bike_json = request.json
        if not bike_json:
            return {"message": "Wrong data"}, 400
        try:
            bike = Bike(
                model=bike_json["model"],
                riding_style=bike_json.get("riding_style"),
                description=bike_json.get("description"),
                release_date=datetime.datetime.strptime(bike_json["release_date"], "%Y-%m-%d"),
                price=bike_json.get("price"),
                rating=bike_json.get("rating"),
            )
            db.session.add(bike)
            db.session.commit()
        except (ValueError, KeyError):
            return {"message": "Wrong data"}, 400
        return {"message": "Resource created successfully"}, 201

    def put(self, uuid):
        bike_json = request.json
        if not bike_json:
            return {"message": "Wrong data"}, 400
        try:
            db.session.query(Bike).filter_by(uuid=uuid).update(
                dict(
                    model=bike_json["model"],
                    riding_style=bike_json.get("riding_style"),
                    description=bike_json.get("description"),
                    release_date=datetime.datetime.strptime(bike_json["release_date"], "%Y-%m-%d"),
                    price=bike_json.get("price"),
                    rating=bike_json.get("rating"),
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {"message": "Wrong data"}, 400
        return {"message": "Resource updated successfully"}, 200

    def patch(self, uuid):
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        bike_json = request.json
        model = bike_json.get("model")
        riding_style = bike_json.get("riding_style")
        description = bike_json.get("description")
        release_date = datetime.datetime.strptime(bike_json.get("release_date"), "%Y %m %d") if bike_json.get(
            "release_date") else None
        price = bike_json.get("price")
        rating = bike_json.get("rating")
        if model:
            bike.model = model
        elif riding_style:
            bike.riding_style = riding_style
        elif description:
            bike.description = description
        elif release_date:
            bike.release_date = release_date
        elif price:
            bike.price = price
        elif rating:
            bike.rating = rating

        db.session.add(bike)
        db.session.commit()
        return {"message": "Resource patched successfully"}, 200

    def delete(self, uuid):
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        db.session.delete(bike)
        db.session.commit()
        return "", 204


api.add_resource(BikesListApi, '/bikes', "/bikes/<string:uuid>", strict_slashes=False)
