from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from src.database.models import Bike


class BikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bike
        exclude = ["id"]
        load_instance = True
        include_fk = True
    riders = Nested("RiderSchema", many=True, exclude=("bikes",))
