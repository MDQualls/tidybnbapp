from flask import make_response, render_template
from flask_restful import Resource


class Disclaimer(Resource):
    title = "Disclaimer"
    headers = {"Context-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("disclaimer.html", title=self.title), 200, self.headers
        )
