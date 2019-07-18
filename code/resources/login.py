from flask import render_template, make_response, redirect, url_for, flash, request
from flask_restful import Resource

from util.security import Security
from util.session import begin_session
from util.validators import in_length


class Login(Resource):
    title = "Login"
    headers = {"Content/Type": "text/html"}

    def get(self):
        return make_response(render_template("login.html", title=self.title), 200, self.headers)

    def post(self):
        try:
            error = ""
            data = request.form

            if not in_length(data["email_address"], 8, 80):
                error = "Invalid email address.  Limit is 8 to 80 characters."
            if not in_length(data["password"], 8, 80):
                error = "Invalid password.  Limit is 8 to 80 characters."
            if len(error) > 0:
                return make_response(
                    render_template("login.html", title=self.title, error=error),
                    200,
                    self.headers,
                )

        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("login.html", title=self.title, error=error),
                200,
                self.headers,
            )

        # Get form fields

        email_address = data["email_address"]
        password_candidate = data["password"]

        security = Security()
        result = security.authenticate(email_address, password_candidate)

        if not result["success"]:
            error = result["message"]
            return make_response(
                render_template("login.html", title=self.title, error=error),
                200,
                self.headers,
            )

        begin_session(
            result["user"].username, result["user"].email_address, True, False
        )

        flash(result["message"], "success")

        return redirect(url_for("home"))
