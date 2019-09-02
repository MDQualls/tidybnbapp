from flask_restful import Resource
from sqlalchemy import extract
from flask import make_response, render_template, request, escape, flash, redirect, url_for
from datetime import datetime

from util.session import is_admin_logged_in
from models.maidplanschedule import MaidPlanSchedule
from util.dateutil import year_month_list
from util.validators import is_date


class ScheduleDashboard(Resource):
    title = "Maid MaidSchedule Dashboard"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        # default query is current month
        schedules = MaidPlanSchedule.query.filter(
            extract('year', MaidPlanSchedule.schedule_date) == datetime.today().year).filter(
            extract('month', MaidPlanSchedule.schedule_date) == datetime.today().month).all()

        timePeriod = datetime.today().strftime("%B, %Y")
        scheduleFilterList = year_month_list(1)

        return make_response(
            render_template("scheduledashboard.html", title=self.title, schedules=schedules, timePeriod=timePeriod,
                            scheduleFilterList=scheduleFilterList),
            200, self.headers
        )

    @is_admin_logged_in
    def post(self):
        data = request.form

        cleandata = {}
        for item in data:
            cleandata[item] = escape(data[item])

        year = datetime.strptime(cleandata['scheduleFilterList'], "%B, %Y").year
        month = datetime.strptime(cleandata['scheduleFilterList'], "%B, %Y").month

        schedules = MaidPlanSchedule.query.filter(
            extract('year', MaidPlanSchedule.schedule_date) == year).filter(
            extract('month', MaidPlanSchedule.schedule_date) == month).all()

        timePeriod = datetime(year=year, month=month, day=1).strftime("%B, %Y")
        scheduleFilterList = year_month_list(1)

        return make_response(
            render_template("scheduledashboard.html", title=self.title, schedules=schedules, timePeriod=timePeriod,
                            scheduleFilterList=scheduleFilterList),
            200, self.headers
        )


class CopySchedule(Resource):
    title = "Maid MaidSchedule Dashboard"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def post(self):
        data = request.form

        schedule_id = None
        schedule_date = None
        for item in data:
            if item.startswith("schedule_date_copy_to_"):
                schedule_date = data[item]
                continue
            if item.startswith("sched_id_"):
                schedule_id = data[item]
                continue

        error = ""
        if not is_date(schedule_date):
            error = "Invalid schedule date.  MaidSchedule date must be valid datetime."

        if len(error) > 0:
            return make_response(
                render_template("scheduledashboard.html", title=self.title, error=error, cleandata=data,
                                schedule_date=datetime.strptime(schedule_date, '%Y-%m-%d')),
                200,
                self.headers,
            )

        clean_schedule_date = escape(schedule_date)
        clean_schedule_id = escape(schedule_id)

        sched_to_copy = MaidPlanSchedule.find_by_id(clean_schedule_id)

        if sched_to_copy is None:
            flash("The maid schedule you attempted to copy was not found", "info")
            return redirect(url_for("scheduledashboard"))

        schedule = MaidPlanSchedule(
            schedule_name=sched_to_copy.schedule_name,
            schedule_date=clean_schedule_date,
            start_time=sched_to_copy.start_time,
            end_time=sched_to_copy.end_time,
            post_clean_buffer=sched_to_copy.post_clean_buffer,
        )

        schedule.save_to_db()

        flash("Your new maid schedule listing has been successfully saved.", "success")

        return redirect(url_for("scheduledashboard"))
