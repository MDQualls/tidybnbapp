from flask import session, flash, redirect, url_for
from functools import wraps


def begin_session(username, email_address, logged_in=False, is_admin=False):
    session["username"] = username
    session["email_address"] = email_address
    session["logged_in"] = logged_in
    session["is_admin"] = is_admin


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please login", "danger")
            return redirect(url_for("login"))

    return wrap


def is_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session and "is_admin" in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please login", "danger")
            return redirect(url_for("login"))

    return wrap


def end_session():
    session.clear()


def get_session_username():
    return session["username"]
