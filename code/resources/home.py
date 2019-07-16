from flask import render_template, make_response
from flask_restful import Resource


class Home(Resource):
    title = "Welcome"

    def get(self):
        headers = {'Content-Type': 'text/html'}

        return make_response(render_template("home.html", title=self.title), 200, headers)
