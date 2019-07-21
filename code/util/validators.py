# from schematics.exceptions import ValidationError
from werkzeug.security import safe_str_cmp


# def min_length(fld, min_length):
#     def validate(s):
#         if len(s) >= min_length:
#             return s
#         raise ValidationError("{} must be a minimum of {} characters long".format(fld, min_length))
#     return validate


def min_length(fld: str, min_len: int) -> bool:
    if len(fld) >= min_len:
        return True
    return False


def max_length(fld: str, max_len: int) -> bool:
    if len(fld) > max_len:
        return False
    return True


def in_length(fld: str, min_len: int, max_len: int) -> bool:
    if len(fld) > max_len or len(fld) < min_len:
        return False
    return True


def is_boolean(fld: str) -> bool:
    if isinstance(fld, bool):
        return True
    return False


def is_int(fld: str) -> bool:
    try:
        int(fld)
        return True
    except Exception as e:
        return False




def strings_match(str1: str, str2: str) -> bool:
    return safe_str_cmp(str1, str2)
