from flask import render_template, make_response
from flask_restful import Resource
from util.session import is_logged_in


class Account(Resource):
    title = "Account"
    headers = {"Content-Type": "text/html"}

    @is_logged_in
    def get(self):
        return make_response(
            render_template("account.html", title=self.title), 200, self.headers
        )
