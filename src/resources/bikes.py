from flask_restful import Resource
from flask import request
from src.schemas.bikes import BikeSchema
from src import db
from src.database.models import Bike
from marshmallow import ValidationError
from .auth import token_required


class BikesListApi(Resource):
    bike_schema = BikeSchema()

    @token_required
    def get(self, uuid=None):
        if not uuid:
            bikes = db.session.query(Bike).all()
            return self.bike_schema.dump(bikes, many=True), 200
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        return self.bike_schema.dump(bike), 200

    def post(self):
        try:
            bike = self.bike_schema.load(request.json, session=db.session)
        except ValidationError as exc:
            return {"message": str(exc)}, 400
        db.session.add(bike)
        db.session.commit()
        return self.bike_schema.dump(bike), 201

    def put(self, uuid):
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        try:
            bike = self.bike_schema.load(request.json, instance=bike, session=db.session)
        except ValidationError as exc:
            return {"message": str(exc)}, 400
        db.session.add(bike)
        db.session.commit()
        return self.bike_schema.dump(bike), 200

    def patch(self, uuid):
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        try:
            bike = self.bike_schema.load(request.json, instance=bike, session=db.session)
        except ValidationError as exc:
            return {"message": str(exc)}, 400

        model = bike.model
        riding_style = bike.riding_style
        description = bike.description
        release_date = bike.release_date.strftime("%Y-%m-%d") if bike.release_date else None
        price = bike.price
        rating = bike.rating

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
        return self.bike_schema.dump(bike), 200

    def delete(self, uuid):
        bike = db.session.query(Bike).filter_by(uuid=uuid).first()
        if not bike:
            return "", 404
        db.session.delete(bike)
        db.session.commit()
        return "", 204
