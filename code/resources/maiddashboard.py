from flask import make_response, render_template
from flask_restful import Resource

from util.session import is_admin_logged_in
from models.maidplan import MaidPlanModel


class MaidDashboard(Resource):
    title = "Maid Plan Dashboard"
    headers = {"Content-Type": "text/html"}

    @is_admin_logged_in
    def get(self):
        maidplans = MaidPlanModel.query.all()

        return make_response(
            render_template("maiddashboard.html", title=self.title, maidplans=maidplans),200,self.headers
        )
