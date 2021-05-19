import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / "data" / "flask_api_db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
