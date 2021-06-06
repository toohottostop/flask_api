from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Bike


class BikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bike
        exclude = ["id"]
        load_instance = True
