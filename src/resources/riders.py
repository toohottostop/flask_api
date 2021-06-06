from flask_restful import Resource
from src.schemas.riders import RiderSchema


class RidersListApi(Resource):
    rider_schema = RiderSchema()

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
