from flask import redirect, url_for, flash
from flask_restful import Resource

from util.session import end_session, get_session_username, is_logged_in


class Logout(Resource):
    @is_logged_in
    def get(self):
        username = get_session_username()
        end_session()
        flash(
            "You have successfully logged out.  Thanks for visiting {}.".format(username), "success",
        )
        return redirect(url_for("home"))
