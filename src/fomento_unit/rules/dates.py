from datetime import datetime, date
from typing import Union


MIN_DATE = date(2013, 1, 1)


def get_today_date():
    return date.today()


def get_date_or_default(target: Union[str, None]) -> Union[datetime.date, None]:
    today = get_today_date()

    if target is None:
        return today

    try:
        target = datetime.strptime(target, '%d-%m-%Y').date()
    except ValueError:
        return None

    if target < MIN_DATE or target > today:
        return None

    return target
