from datetime import datetime


def year_month_list(years_before_and_after: int) -> []:
    current_year = datetime.today().year

    start = current_year - years_before_and_after
    end = current_year + years_before_and_after + 1

    result = []
    for yr in range(start, end):
        for mn in range(1, 13):
            month_year = datetime(year=yr, month=mn, day=1).strftime("%B, %Y")
            result.append(month_year)
    return result
