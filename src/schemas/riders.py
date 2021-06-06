from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Rider


class RiderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rider
        load_instance = True
