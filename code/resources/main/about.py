from flask_restful import Resource
from flask import make_response, render_template


class About(Resource):
    title = "About"
    headers = {"Content-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("about.html", title=self.title), 200, self.headers
        )
