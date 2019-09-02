from flask_restful import Resource
from flask import make_response, render_template, flash, redirect, url_for, escape, request

from models.bnb import BnbModel
from util.session import is_admin_logged_in
from util.modelvalidators import validate_bnblisting


class EditBnbListing(Resource):
    title = "Edit BnB Listing"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self, id):
        bnb = BnbModel.find_by_id(id)

        if bnb is None:
            flash("The BnB you attempted to edit was not found")
            return redirect(url_for("bnbdashboard"))

        return make_response(
            render_template("bnblistingform.html", title=self.title, cleandata=bnb), 200, self.headers
        )

    @is_admin_logged_in
    def post(self, id):
        try:
            data = request.form

            error = validate_bnblisting(data)

            if len(error) > 0:
                return make_response(
                    render_template("bnblistingform.html", title=self.title, error=error, cleandata=data),
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

        cleandata = {}
        for item in data:
            cleandata[item] = escape(data[item])

        bnb = BnbModel.find_by_id(id)

        if bnb is None:
            flash("The BnB you attempted to edit was not found.", "info")
            return redirect(url_for("bnbdashboard"))

        bnb.title = cleandata["title"]
        bnb.summary = cleandata["summary"]
        bnb.content = cleandata["content"].strip()
        bnb.thumbnail = ""
        bnb.active = True
        bnb.archived = False
        bnb.deleted = False
        bnb.bedrooms = cleandata["bedrooms"]
        bnb.bathrooms = cleandata["bathrooms"]
        bnb.street_address_1 = cleandata["street_address_1"]
        bnb.street_address_2 = cleandata["street_address_2"]
        bnb.city = cleandata["city"]
        bnb.state = cleandata["state"]
        bnb.zip_code = cleandata["zip_code"]
        bnb.square_footage = cleandata["square_footage"]

        bnb.save_to_db()

        flash("Your BnB update has been successfully saved.", "success")

        return redirect(url_for("bnbdashboard"))
