from flask import make_response, render_template
from flask_restful import Resource

from models.bnb import BnbModel


class BnbListings(Resource):
    title = "BnB Listings"
    headers = {"Content-Type": "text/html"}

    def get(self):

        bnbs = BnbModel.query.all()

        return make_response(
            render_template("bnblistings.html", title=self.title, bnbs=bnbs), 200, self.headers
        )
