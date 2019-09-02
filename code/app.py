from flask import Flask, make_response, render_template
from flask_restful import Api
from util.csrfprotect import csrf
from flask_wtf.csrf import CSRFError
from util.templatefilters import templatefilters
from config import Config

from resources.main.home import Home
from resources.user.login import Login
from resources.user.register import Register
from resources.user.account import Account
from resources.user.logout import Logout
from resources.main.about import About
from resources.main.contact import Contact
from resources.bnb.bnblistings import BnbListings
from resources.main.disclaimer import Disclaimer
from resources.bnb.bnbdashboard import BnbDashboard
from resources.bnb.addbnblisting import AddBnbListing
from resources.bnb.editbnblisting import EditBnbListing
from resources.main.privacypolicy import PrivacyPolicy
from resources.bnb.bnbdetail import BnbDetail
from resources.maidplan.maiddashboard import MaidDashboard
from resources.maidplan.addmaidplan import AddMaidPlan
from resources.maidplan.editmaidplan import EditMaidPlan
from resources.schedule.scheduledashboard import ScheduleDashboard, CopySchedule
from resources.schedule.addschedule import AddSchedule
from resources.schedule.editschedule import EditSchedule
from resources.schedule.maidschedule import MaidSchedule

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(templatefilters)

handle_exceptions = app.handle_exception
handle_user_exception = app.handle_user_exception
api = Api(app)
app.handle_user_exception = handle_exceptions
app.handle_user_exception = handle_user_exception

csrf.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(CSRFError)
def handle_csrf_error(reason):
    return make_response(
        render_template('error/csrf_error.html', reason=reason, title="CSRF Validation"), 400,
        {"Content-Type": "text/html"}
    )


@app.errorhandler(404)
def handle_404_error(reason):
    return make_response(
        render_template('error/fourohfour.html', title="404 Error"), 404,
        {"Content-Type": "text/html"}
    )


api.add_resource(Home, "/", "/home")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(Account, "/account")
api.add_resource(Logout, "/logout")
api.add_resource(About, "/about")
api.add_resource(Contact, "/contact")
api.add_resource(BnbListings, "/bnblistings")
api.add_resource(Disclaimer, "/disclaimer")
api.add_resource(BnbDashboard, "/bnbdashboard")
api.add_resource(AddBnbListing, "/addbnblisting")
api.add_resource(EditBnbListing, "/editbnblisting/<int:id>")
api.add_resource(PrivacyPolicy, "/privacypolicy")
api.add_resource(BnbDetail, "/bnbdetail/<int:id>")
api.add_resource(MaidDashboard, "/maiddashboard")
api.add_resource(AddMaidPlan, "/addmaidplan")
api.add_resource(EditMaidPlan, "/editmaidplan/<int:id>")
api.add_resource(ScheduleDashboard, "/scheduledashboard")
api.add_resource(AddSchedule, "/addschedule")
api.add_resource(EditSchedule, "/editschedule/<int:id>")
api.add_resource(CopySchedule, "/copyschedule")
api.add_resource(MaidSchedule, "/maidschedule")

if __name__ == "__main__":
    from db import db

    # init db
    db.init_app(app)
    app.run(port=5000, debug=True)
