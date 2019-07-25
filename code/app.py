from flask import Flask, make_response, render_template
from flask_restful import Api
import secrets
from util.csrfprotect import csrf
from flask_wtf.csrf import CSRFError

from resources.home import Home
from resources.login import Login
from resources.register import Register
from resources.account import Account
from resources.logout import Logout
from resources.about import About
from resources.contact import Contact
from resources.bnblistings import BnbListings
from resources.maidlistings import MaidListings
from resources.disclaimer import Disclaimer
from resources.bnbdashboard import BnbDashboard
from resources.addbnblisting import AddBnbListing
from resources.editbnblisting import EditBnbListing
from resources.privacypolicy import PrivacyPolicy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://tidyuser:\G''ymP='WMTp4VR>+2+@localhost/tidyappdb1"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:x6xzyi@localhost/tidyappdb1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = secrets.token_urlsafe(24)

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


api.add_resource(Home, "/", "/home")
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(Account, "/account")
api.add_resource(Logout, "/logout")
api.add_resource(About, "/about")
api.add_resource(Contact, "/contact")
api.add_resource(BnbListings, "/bnblistings")
api.add_resource(MaidListings, "/maidlistings")
api.add_resource(Disclaimer, "/disclaimer")
api.add_resource(BnbDashboard, "/bnbdashboard")
api.add_resource(AddBnbListing, "/addbnblisting")
api.add_resource(EditBnbListing, "/editbnblisting/<int:id>")
api.add_resource(PrivacyPolicy, "/privacypolicy")

if __name__ == "__main__":
    from db import db

    # init db
    db.init_app(app)
    app.run(port=5000, debug=True)
