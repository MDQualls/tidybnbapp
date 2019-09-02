from flask_restful import Resource
from flask import make_response, render_template


class MaidSchedule(Resource):
    title = "Cleaning MaidSchedule"
    headings = {"Content-Type": "text/html"}

    def get(self):
        return make_response(
            render_template("maidschedule.html", title=self.title), 200, self.headings
        )
