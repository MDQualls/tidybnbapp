from flask_restful import Resource
from flask import make_response, render_template

from util.session import is_admin_logged_in


class ScheduleDashboard(Resource):
    title = "Maid Schedule Dashboard"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        return make_response(
            render_template("scheduledashboard.html", title=self.title), 200, self.headers
        )
