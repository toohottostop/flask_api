from flask_restful import Resource

from src.database.models import Rider
from src.schemas.riders import RiderSchema
from src import db


class RidersListApi(Resource):
    rider_schema = RiderSchema()

    def get(self):
        riders = db.session.query(Rider).all()
        if not riders:
            return "", 404
        return self.rider_schema.dump(riders, many=True), 200

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
