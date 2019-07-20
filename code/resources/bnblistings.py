from flask import make_response, render_template
from flask_restful import Resource


class BnbListings(Resource):
    title = "BnB Listings"
    headers = {"Contenct-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("bnblistings.html", title=self.title), 200, self.headers
        )
