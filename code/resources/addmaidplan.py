from flask import make_response, render_template, request, escape, flash, redirect, url_for
from flask_restful import Resource
from util.session import is_admin_logged_in
from util.validators import in_length, min_length

from models.maidplan import MaidPlanModel


class AddMaidPlan(Resource):
    title = "Add New Maid Plan"
    headers = {"Content-Type": "Text/html"}

    @is_admin_logged_in
    def get(self):
        return make_response(
            render_template("maidplanform.html", title=self.title, cleandata={}), 200, self.headers
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
            if not min_length(cleandata["description"].strip(), 10):
                error = "Invalid content.  Content must be at least 10 characters."

            if len(error) > 0:
                return make_response(
                    render_template("maidplanform.html", title=self.title, error=error, cleandata=cleandata),
                    200,
                    self.headers,
                )
        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("maiddashboard.html", title=self.title, error=error),
                200,
                self.headers,
            )

        plan = MaidPlanModel(
            title=cleandata["title"],
            summary=cleandata["summary"],
            description=cleandata["description"].strip(),
            deleted=False,
        )

        plan.save_to_db()

        flash("Your new maid plan has been successfully save.", "success")

        return redirect(url_for("maiddashboard"))
