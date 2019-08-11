from werkzeug.security import safe_str_cmp
from datetime import datetime, time, timedelta


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


def is_date(fld: str) -> bool:
    try:
        datetime.strptime(fld, '%Y-%m-%d')
        return True
    except Exception as e:
        return False


def is_time(fld: str) -> bool:
    FMT = '%H:%M:%S'
    try:
        if len(fld) == 5:
            fld = "{}:{}".format(fld, '00')
        datetime.strptime(fld, FMT)
        return True
    except ValueError:
        return False


def verify_time_diff_positive(from_time: str, to_time: str) -> bool:
    try:
        FMT = '%H:%M:%S'
        if len(from_time) == 5:
            from_time = "{}:{}".format(from_time, '00')
        time_from_date = datetime.strptime(from_time, FMT)
        if len(to_time) == 5:
            to_time = "{}:{}".format(to_time, '00')
        time_to_date = datetime.strptime(to_time, FMT)
        from_delta = timedelta(hours=time_from_date.hour, minutes=time_from_date.minute)
        to_delta = timedelta(hours=time_to_date.hour, minutes=time_to_date.minute)
        return from_delta < to_delta
    except Exception as e:
        return False


def are_dates_distinct(date1: str, date2: str) -> bool:
    try:
        FMT = '%Y-%m-%d %H:%M:%S %p'
        first_date = datetime.strptime(date1, FMT)
        second_date = datetime.strptime(date2, FMT)
        return first_date == second_date
    except Exception as e:
        return False
