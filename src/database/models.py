import uuid
from src import db


class Bike(db.Model):
    __tablename__ = "bikes"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    riding_style = db.Column(db.String(50))
    description = db.Column(db.Text)
    release_date = db.Column(db.Date, index=True, nullable=False)
    price = db.Column(db.Float)
    rating = db.Column(db.Float)

    def __init__(self, model, riding_style, description, release_date, price, rating):
        self.model = model
        self.uuid = str(uuid.uuid4())
        self.riding_style = riding_style
        self.description = description
        self.release_date = release_date
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"Bike({self.model}, {self.uuid}, {self.release_date}, {self.price})"

    def to_dict(self):
        return {
            "model": self.model,
            "uuid": self.uuid,
            "riding_style": self.riding_style,
            "description": self.description,
            "release_date": self.release_date.strftime("%Y-%m-%d"),
            "price": self.price,
            "rating": self.rating,
        }


class Rider(db.Model):
    __tablename__ = "riders"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Rider - {self.first_name} {self.last_name}"
