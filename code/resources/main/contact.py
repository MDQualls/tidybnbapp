from flask import make_response, render_template
from flask_restful import Resource


class Contact(Resource):
    title = "Contact"
    headers = {"Content-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("contact.html", title=self.title), 200, self.headers
        )
