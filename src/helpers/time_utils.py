from datetime import datetime, timedelta


def date_hours_minutes_return():
    return datetime.today().strftime('%Y-%m-%d %H:%M')


def return_date_for_payments(days):
    date = datetime.today()
    modified_date = date + timedelta(days=days)
    return modified_date.strftime("%d.%m.%Y")


def return_date_for_calendar_autopayments(days):
    date = datetime.today()
    modified_date = date + timedelta(days=days)
    return modified_date.strftime("%-d")
