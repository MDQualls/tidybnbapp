from models.user import UserModel
from passlib.hash import pbkdf2_sha256


class Security:

    response = {
        "success": False,
        "message": "Login attempt failed.  Check your user name and password.",
        "user": None,
    }

    def authenticate(self, email_address, password_candidate):

        user = UserModel.find_by_email(email_address)

        if user is None:
            return Security.response

        if Security.validate(password_candidate, user.password):
            Security.response["success"] = True
            Security.response[
                "message"
            ] = "Login successful.  Welcome to the site {}.".format(user.username)
            Security.response["user"] = user
            return Security.response

        return Security.response

    @classmethod
    def encrypt(cls, value: str):
        crypt = pbkdf2_sha256.hash(str(value))
        return crypt

    @classmethod
    def validate(cls, val1, val2):
        return pbkdf2_sha256.verify(val1, val2)
