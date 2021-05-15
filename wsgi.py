from src import app
from src import api
from src.routes import BikesListApi

api.add_resource(BikesListApi, '/bikes', "/bikes/<string:uuid>", strict_slashes=False)

if __name__ == '__main__':
    app.run()
