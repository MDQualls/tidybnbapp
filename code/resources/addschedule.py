from flask import make_response, render_template, request, redirect, flash, escape, url_for
from flask_restful import Resource
from models.maidplanschedule import MaidPlanSchedule
from util.session import is_admin_logged_in
from util.modelvalidators import validate_schedule


class AddSchedule(Resource):
    title = "Admin Maid Schedule"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        cleandata = {}

        return make_response(
            render_template("adminscheduleform.html", title=self.title, cleandata=cleandata, schedule_date=""), 200,
            self.headers
        )

    @is_admin_logged_in
    def post(self):

        cleandata = {}

        try:
            data = request.form

            error = validate_schedule(data)

            if len(error) > 0:
                return make_response(
                    render_template("adminscheduleform.html", title=self.title, error=error, cleandata=data),
                    200,
                    self.headers,
                )
        except Exception as e:
            error = (
                "An internal error occurred.  Please try this operation again later."
            )
            return make_response(
                render_template("scheduledashboard.html", title=self.title, error=error),
                200,
                self.headers,
            )

        for item in data:
            cleandata[item] = escape(data[item])

        schedule = MaidPlanSchedule(
            schedule_name=cleandata["schedule_name"],
            schedule_date=cleandata["schedule_date"],
            start_time=cleandata["start_time"],
            end_time=cleandata["end_time"],
            post_clean_buffer=cleandata["post_clean_buffer"],
        )

        schedule.save_to_db()

        flash("Your new maid schedule listing has been successfully saved.", "success")

        return redirect(url_for("scheduledashboard"))
