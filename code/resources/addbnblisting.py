from flask import make_response, render_template
from flask_restful import Resource

from util.session import is_admin_logged_in


class AddBnbListing(Resource):
    title = "Add new BnB Listing"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        return make_response(
            render_template("addbnblisting.html", title=self.title), 200, self.headers
        )
