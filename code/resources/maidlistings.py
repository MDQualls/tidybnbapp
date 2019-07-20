from flask import make_response, render_template
from flask_restful import Resource


class MaidListings(Resource):
    title = "Maid Listings"
    headings = {"Content-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("maidlistings.html", title=self.title), 200, self.headings
        )
