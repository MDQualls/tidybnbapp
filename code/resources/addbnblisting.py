from flask import make_response, render_template, flash, redirect, url_for, escape, request
from flask_restful import Resource
from util.session import is_admin_logged_in
from models.bnb import BnbModel
from util.validators import in_length, min_length, is_int, max_length


class AddBnbListing(Resource):
    title = "Add new BnB Listing"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        return make_response(
            render_template("addbnblisting.html", title=self.title, cleandata={}), 200, self.headers
        )

    @is_admin_logged_in
    def post(self):
        try:
            data = request.form

            cleandata = {}
            for item in data:
                cleandata[item] = escape(data[item])

            error = ""

            if not in_length(cleandata["title"], 3, 80):
                error = "Invalid title.  Title must be from 3 to 80 characters."
            if not in_length(cleandata["summary"], 3, 240):
                error = "Invalid summary.  Summary must be from 3 to 240 characters."
            if not min_length(cleandata["content"], 10):
                error = "Invalid content.  Content must be at least 10 characters."
            if "active" in cleandata and not is_int(cleandata['active']):
                error = "Invalid active entry.  'Active' entry must be an integer."
            if "archived" in cleandata and not is_int(cleandata['archived']):
                error = "Invalid archived entry.  'Archived' entry must be an integer."
            if not is_int(cleandata['bedrooms']):
                error = "Invalid bedrooms entry.  'Bedrooms' entry must be an integer."
            if not is_int(cleandata['bathrooms']):
                error = "Invalid bathrooms entry.  'Bathrooms' entry must be an integer."
            if not in_length(cleandata["street_address_1"], 3, 80):
                error = "Invalid street address 1.  'Street address 1' must be from 3 to 80 characters."
            if cleandata['street_address_2'] and not max_length(cleandata["street_address_2"], 80):
                error = "Invalid street address 2.  'Street address 2' must be 80 characters or less."
            if not in_length(cleandata["city"], 3, 80):
                error = "Invalid city entry.  'City' must be from 3 to 80 characters."
            if not in_length(cleandata["state"], 2, 80):
                error = "Invalid state entry.  'State' must be from 2 to 80 characters."
            if not in_length(cleandata["zip_code"], 5, 20):
                error = "Invalid zip code entry.  'Zip code' must be from 5 to 20 characters."
            if not in_length(cleandata["square_footage"], 2, 20):
                error = "Invalid square footage entry.  'Square footage' must be from 2 to 20 characters."

            if len(error) > 0:
                return make_response(
                    render_template("addbnblisting.html", title=self.title, error=error, cleandata=cleandata),
                    200,
                    self.headers,
                )

        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("addbnblisting.html", title=self.title, error=error),
                200,
                self.headers,
            )

        post = BnbModel(
            title=cleandata["title"],
            summary=cleandata["summary"],
            content=cleandata["content"],
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
