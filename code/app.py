from flask import Flask
from flask_restful import Api

from resources.home import Home
from resources.login import Login
from resources.register import Register

app = Flask(__name__)

api = Api(app)

api.add_resource(Home, "/", "/home")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")

app.run(port=5000, debug=True)
