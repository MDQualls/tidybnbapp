from flask import make_response, render_template, request, escape, flash, redirect, url_for
from flask_restful import Resource
from util.session import is_admin_logged_in
from util.modelvalidators import validate_maidplan

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

        cleandata = {}

        try:
            data = request.form

            error = validate_maidplan(data)

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

        for item in data:
            cleandata[item] = escape(data[item])

        plan = MaidPlanModel(
            title=cleandata["title"],
            summary=cleandata["summary"],
            description=cleandata["description"].strip(),
            deleted=False,
        )

        plan.save_to_db()

        flash("Your new maid plan has been successfully save.", "success")

        return redirect(url_for("maiddashboard"))
