from flask_restful import Resource
from flask import make_response, render_template, flash, redirect, url_for, escape, request

from util.session import is_admin_logged_in
from models.maidplanschedule import MaidPlanSchedule


class EditSchedule(Resource):
    title = "Edit Maid Schedule"
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
