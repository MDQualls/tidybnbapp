from flask_restful import Resource
from flask import make_response, render_template, flash, redirect, url_for, escape, request

from util.session import is_admin_logged_in
from models.maidplanschedule import MaidPlanSchedule
from util.modelvalidators import validate_schedule
from datetime import datetime


class EditSchedule(Resource):
    title = "Edit Maid MaidSchedule"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self, id):
        schedule = MaidPlanSchedule.find_by_id(id)

        if schedule is None:
            flash("The maid schedule you attempted to edit was not found")
            return redirect(url_for("scheduledashboard"))

        return make_response(
            render_template("adminscheduleform.html", title=self.title, cleandata=schedule,
                            schedule_date=schedule.schedule_date), 200, self.headers
        )

    @is_admin_logged_in
    def post(self, id):

        cleandata = {}

        data = request.form

        error = validate_schedule(data)

        if len(error) > 0:
            return make_response(
                render_template("adminscheduleform.html", title=self.title, error=error, cleandata=data,
                                schedule_date=datetime.strptime(data['schedule_date'], '%Y-%m-%d')), 200, self.headers
            )

        for item in data:
            cleandata[item] = escape(data[item])

        schedule = MaidPlanSchedule.find_by_id(id)

        if schedule is None:
            flash("The maid schedule you attempted to edit was not found", "info")
            return redirect(url_for("scheduledashboard"))

        schedule.schedule_name = cleandata["schedule_name"]
        schedule.schedule_date = cleandata["schedule_date"]
        schedule.start_time = cleandata["start_time"]
        schedule.end_time = cleandata["end_time"]
        schedule.post_clean_buffer = cleandata["post_clean_buffer"]

        schedule.save_to_db()

        flash("Your maid schedule update has been successfully saved.", "success")

        return redirect(url_for("scheduledashboard"))
