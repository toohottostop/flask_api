from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from src.database.models import Rider


class RiderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rider
        load_instance = True
        include_fk = True
    bikes = Nested("BikeSchema", many=True, exclude=("riders",))
