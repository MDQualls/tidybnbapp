from flask import make_response, render_template, request, redirect, flash
from flask_restful import Resource
from models.maidplanschedule import MaidPlanSchedule
from util.session import is_admin_logged_in
from util.validators import in_length


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
        data = request.data

        error = ""

        if not in_length(data["schedule_name"], 3, 80):
            error = "Invalid schedule name.  Name must be from 3 to 80 characters."




