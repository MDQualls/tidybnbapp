from flask_restful import Resource
from flask import make_response, render_template, flash, redirect, url_for, escape, request

from models.bnb import BnbModel
from util.session import is_admin_logged_in
from util.validators import in_length, min_length, is_int, max_length


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

            error = ""

            if not in_length(data["title"], 3, 80):
                error = "Invalid title.  Title must be from 3 to 80 characters."
            if not in_length(data["summary"], 3, 240):
                error = "Invalid summary.  Summary must be from 3 to 240 characters."
            if not min_length(data["content"].strip(), 10):
                error = "Invalid content.  Content must be at least 10 characters."
            if "active" in data and not is_int(data['active']):
                error = "Invalid active entry.  'Active' entry must be an integer."
            if "archived" in data and not is_int(data['archived']):
                error = "Invalid archived entry.  'Archived' entry must be an integer."
            if not is_int(data['bedrooms']):
                error = "Invalid bedrooms entry.  'Bedrooms' entry must be an integer."
            if not is_int(data['bathrooms']):
                error = "Invalid bathrooms entry.  'Bathrooms' entry must be an integer."
            if not in_length(data["street_address_1"], 3, 80):
                error = "Invalid street address 1.  'Street address 1' must be from 3 to 80 characters."
            if data['street_address_2'] and not max_length(data["street_address_2"], 80):
                error = "Invalid street address 2.  'Street address 2' must be 80 characters or less."
            if not in_length(data["city"], 3, 80):
                error = "Invalid city entry.  'City' must be from 3 to 80 characters."
            if not in_length(data["state"], 2, 80):
                error = "Invalid state entry.  'State' must be from 2 to 80 characters."
            if not in_length(data["zip_code"], 5, 20):
                error = "Invalid zip code entry.  'Zip code' must be from 5 to 20 characters."
            if not in_length(data["square_footage"], 2, 20):
                error = "Invalid data footage entry.  'Square footage' must be from 2 to 20 characters."

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
