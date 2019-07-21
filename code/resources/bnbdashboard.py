from flask import make_response, render_template
from flask_restful import Resource

from util.session import is_admin_logged_in
from models.bnb import BnbModel


class BnbDashboard(Resource):
    title = "BnB Dashboard"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):

        bnbs = BnbModel.query.all()

        return make_response(
            render_template("dashboard.html", title=self.title, bnbs=bnbs), 200, self.headers
        )
