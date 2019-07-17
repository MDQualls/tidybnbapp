from flask import render_template, make_response
from flask_restful import Resource


class Login(Resource):
    title = "Login"
    headers = {"Content/Type": "text/html"}

    def get(self):
        return make_response(render_template("login.html", title=self.title), 200, self.headers)
