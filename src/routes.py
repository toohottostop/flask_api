from src import api
from src.resources.bikes import BikesListApi
from src.resources.riders import RidersListApi
from src.resources.auth import AuthRegister, AuthLogin

api.add_resource(BikesListApi, "/bikes", "/bikes/<string:uuid>", strict_slashes=False)
api.add_resource(RidersListApi, "/riders", strict_slashes=False)
api.add_resource(AuthRegister, "/register", strict_slashes=False)
api.add_resource(AuthLogin, "/login", strict_slashes=False)
