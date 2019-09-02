from flask import make_response, render_template
from flask_restful import Resource


class PrivacyPolicy(Resource):
    title = "Privacy Policy"
    headers = {"Content-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("privacypolicy.html", title=self.title), 200, self.headers
        )
