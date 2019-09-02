import datetime
import calendar
from flask_restful import Resource
from flask import make_response, render_template
from models.maidplanschedule import MaidPlanSchedule


class MaidSchedule(Resource):
    title = "Cleaning Schedule"
    headings = {"Content-Type": "text/html"}

    def get(self):
        current_month_last_day = calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]
        current_month_year = datetime.date.today().strftime("%B, %Y")
        schedule = MaidPlanSchedule.query.filter(
            datetime.date.today().replace(day=1) <= MaidPlanSchedule.schedule_date).filter(
            MaidPlanSchedule.schedule_date <= datetime.date.today().replace(
                day=current_month_last_day)).order_by(MaidPlanSchedule.schedule_date).all()
        return make_response(
            render_template("maidschedule.html", title=self.title, current_month_year=current_month_year,
                            schedule=schedule), 200, self.headings
        )
