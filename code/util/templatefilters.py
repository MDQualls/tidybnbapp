import jinja2
import flask
import datetime
from util.validators import is_date

blueprint = flask.Blueprint('templatefilters', __name__)


@blueprint.app_template_filter()
def format_datetime(value, fmt='%Y-%m-%d'):
    """Format a date time to (Default): Y-m-d"""
    if not isinstance(value, datetime.datetime):
        return ""
    x = value.strftime(fmt)
    return x
