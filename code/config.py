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

    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://tidyuser:\G''ymP='WMTp4VR>+2+@localhost/tidyappdb1"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:x6xzyi@localhost/tidyappdb1"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SECRET_KEY"] = 'V-o_-abQ5zCli_Q7GuH-mU-pcRHKC1OG'