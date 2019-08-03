from flask import make_response, render_template, request, escape, flash, redirect, url_for
from flask_restful import Resource
from util.session import is_admin_logged_in
from util.validators import in_length, min_length

from models.maidplan import MaidPlanModel


class EditMaidPlan(Resource):
    title = "Edit Maid Plan"
    headers = {"Content-Type": "Text/html"}

    @is_admin_logged_in
    def get(self, id):
        plan = MaidPlanModel.find_by_id(id)

        if plan is None:
            flash("The plan you attempted to edit was not found")
            return redirect(url_for("maiddashboard"))

        return make_response(
            render_template("maidplanform.html", title=self.title, cleandata=plan), 200, self.headers
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
            if not min_length(data["description"].strip(), 10):
                error = "Invalid description.  Description must be at least 10 characters."

            if len(error) > 0:
                return make_response(
                    render_template("maidplanform.html", title=self.title, error=error, cleandata=data),
                    200,
                    self.headers,
                )

        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("maidplanform.html", title=self.title, error=error),
                200,
                self.headers,
            )

        cleandata = {}
        for item in data:
            cleandata[item] = escape(data[item])

        plan = MaidPlanModel.find_by_id(id)

        if plan is None:
            flash("The plan you attempted to edit was not found.", "info")
            return redirect(url_for("maiddashboard"))

        plan.title = cleandata["title"]
        plan.summary = cleandata["summary"]
        plan.description = cleandata["description"].strip()

        plan.save_to_db()

        flash("Your maid plan update has been successfully saved.", "success")

        return redirect(url_for("maiddashboard"))
