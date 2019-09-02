from flask import render_template, make_response
from flask_restful import Resource


class Home(Resource):
    title = "Welcome"
    headers = {'Content-Type': 'text/html'}

    def get(self):
        return make_response(render_template("home.html", title=self.title), 200, self.headers)
