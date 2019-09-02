from flask import Blueprint
import datetime

templatefilters = Blueprint('templatefilters', __name__)


@templatefilters.app_template_filter()
def format_datetime(value, fmt='%Y-%m-%d'):
    """Format a date time to (Default): Y-m-d"""
    if not isinstance(value, datetime.datetime):
        try:
            return datetime.datetime.strptime(value, fmt)
        except Exception as e:
            return ""
    return value.strftime(fmt)
