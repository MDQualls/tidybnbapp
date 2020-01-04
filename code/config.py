import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('TIDYAPP_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('TIDYAPP_SECRET_KEY')

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('GMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('GMAIL_APP_PASS')

    # app.config["SQLALCHEMY_DATABASE_URI"] = "xxx"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "xxx"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SECRET_KEY"] = 'xxx'
