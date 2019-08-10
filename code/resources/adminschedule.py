from flask import make_response, render_template, request, redirect, flash, escape, url_for
from flask_restful import Resource
from models.maidplanschedule import MaidPlanSchedule
from util.session import is_admin_logged_in
from util.validators import in_length, is_date, is_time, is_int, verify_time_diff_positive


class AdminSchedule(Resource):
    title = "Admin Maid Schedule"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        cleandata = {}

        return make_response(
            render_template("adminscheduleform.html", title=self.title, cleandata=cleandata), 200, self.headers
        )

    @is_admin_logged_in
    def post(self):

        cleandata = {}

        try:
            data = request.form

            error = ""

            if not in_length(data["schedule_name"], 3, 80):
                error = "Invalid schedule name.  Name must be from 3 to 80 characters."
            if not is_date(data["schedule_date"]):
                error = "Invalid schedule date.  Schedule date must be valid datetime."
            if not is_time(data["start_time"]):
                error = "Invalid schedule start time.  Schedule start time must be valid time."
            if not is_time(data["end_time"]):
                error = "Invalid schedule end time.  Schedule end time must be valid time."
            if not is_int(data["post_clean_buffer"]):
                error = "Invalid schedule post clean time.  Schedule post clean time must be valid number of minutes."
            if not verify_time_diff_positive(data["start_time"], data["end_time"]):
                error = "Invalid start and end time entry.  Start time must be before end time."

            if len(error) > 0:
                return make_response(
                    render_template("scheduledashboard.html", title=self.title, error=error, cleandata=cleandata),
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
