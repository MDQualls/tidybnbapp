from flask_restful import Resource
from flask import make_response, render_template

from models.bnb import BnbModel


class BnbDetail(Resource):
    title = "BnB Detail"
    headers = {"Content-Type": "text/html"}

    def get(self, id):
        bnb = BnbModel.find_by_id(id)

        return make_response(
            render_template("bnbdetail.html", title=self.title, bnb=bnb), 200, self.headers
        )
