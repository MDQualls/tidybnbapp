from flask_restful import Resource
from sqlalchemy import extract
from flask import make_response, render_template, request, escape
from datetime import datetime

from util.session import is_admin_logged_in
from models.maidplanschedule import MaidPlanSchedule
from util.dateutil import year_month_list


class ScheduleDashboard(Resource):
    title = "Maid Schedule Dashboard"
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
