from flask import make_response, render_template, flash, redirect, url_for, escape, request
from flask_restful import Resource
from util.session import is_admin_logged_in
from models.bnb import BnbModel
from util.modelvalidators import validate_bnblisting


class AddBnbListing(Resource):
    title = "Add new BnB Listing"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        return make_response(
            render_template("bnblistingform.html", title=self.title, cleandata={}), 200, self.headers
        )

    @is_admin_logged_in
    def post(self):

        cleandata = {}

        try:
            data = request.form

            error = validate_bnblisting(data)

            if len(error) > 0:
                return make_response(
                    render_template("bnbdashboard.html", title=self.title, error=error, cleandata=cleandata),
                    200,
                    self.headers,
                )

        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("bnblistingform.html", title=self.title, error=error),
                200,
                self.headers,
            )

        for item in data:
            cleandata[item] = escape(data[item])

        post = BnbModel(
            title=cleandata["title"],
            summary=cleandata["summary"],
            content=cleandata["content"].strip(),
            thumbnail="",
            active=True,
            archived=False,
            deleted=False,
            bedrooms=cleandata["bedrooms"],
            bathrooms=cleandata["bathrooms"],
            street_address_1=cleandata["street_address_1"],
            street_address_2=cleandata["street_address_2"],
            city=cleandata["city"],
            state=cleandata["state"],
            zip_code=cleandata["zip_code"],
            square_footage=cleandata["square_footage"],
        )

        post.save_to_db()

        flash("Your new BnB listing has been successfully saved.", "success")

        return redirect(url_for("bnbdashboard"))
