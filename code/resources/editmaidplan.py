from flask import make_response, render_template, request, escape, flash, redirect, url_for
from flask_restful import Resource
from util.session import is_admin_logged_in
from util.modelvalidators import validate_maidplan

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

            error = validate_maidplan(data)

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
