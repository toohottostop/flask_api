from flask import Flask

try:
    from flask_restful import Api
except ImportError:
    import flask.scaffold
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
    from flask_restful import Api

app = Flask(__name__)
api = Api(app)
