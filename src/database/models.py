import uuid
from src import db

bike_riders = db.Table(
    "bike_riders",
    db.Column("rider_id", db.Integer, db.ForeignKey("riders.id"), primary_key=True),
    db.Column("bike_id", db.Integer, db.ForeignKey("bikes.id"), primary_key=True)
)


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
    riders = db.relationship("Rider", secondary=bike_riders, lazy="subquery", backref=db.backref("bikes", lazy=True))

    def __init__(self, model, riding_style, description, release_date, price, rating, riders=None):
        self.model = model
        self.uuid = str(uuid.uuid4())
        self.riding_style = riding_style
        self.description = description
        self.release_date = release_date
        self.price = price
        self.rating = rating
        if not riders:
            self.riders = []
        else:
            self.riders = riders

    def __repr__(self):
        return f"Bike({self.model}, {self.uuid}, {self.release_date}, {self.price})"


class Rider(db.Model):
    __tablename__ = "riders"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Rider - {self.first_name} {self.last_name}"
