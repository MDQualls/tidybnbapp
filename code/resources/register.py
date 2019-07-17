from flask_restful import Resource
from flask import make_response, render_template


class Register(Resource):
    title = "Register"
    headers = {"Content/Type": "text/html"}

    def get(self):
        return make_response(render_template("register.html", title=self.title), 200, self.headers)
