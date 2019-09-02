from flask_restful import Resource
from flask import make_response, render_template, flash, request, escape, redirect, url_for
from util.validators import in_length, strings_match
from util.security import Security

from models.user import UserModel


class Register(Resource):
    title = "Register"
    headers = {"Content/Type": "text/html"}

    def get(self):
        return make_response(render_template("register.html", title=self.title), 200, self.headers)

    def post(self):

        try:

            error = ""

            data = request.form

            if not in_length(data["username"], 3, 80):
                error = "Invalid user name.  Limit is 3 to 80 characters."
            if not in_length(data["email_address"], 8, 80):
                error = "Invalid email address.  Limit is 8 to 80 characters."
            if not in_length(data["password"], 8, 80):
                error = "Invalid password.  Limit is 8 to 80 characters."
            if not strings_match(data["password"], data["confirm_password"]):
                error = "Password and confirm password must match."
            if UserModel.find_by_username(data["username"]):
                error = "Duplicate username found."
            if UserModel.find_by_email(data["email_address"]):
                error = "Duplicate email address found."

            if len(error) > 0:
                return make_response(
                    render_template("register.html", title=self.title, error=error),
                    200,
                    self.headers,
                )

        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("register.html", title=self.title, error=error),
                200,
                self.headers,
            )

        cleandata = {}
        for key in data:
            cleandata[key] = escape(data[key])

        password = Security.encrypt(data["password"])

        user = UserModel(
            username=data["username"],
            password=password,
            email_address=data["email_address"],

        )

        user.save_to_db()

        flash("Thank you for registering.  You can now login.", "success")

        return redirect(url_for("home"))
