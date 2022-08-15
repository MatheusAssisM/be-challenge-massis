from datetime import datetime


def format_date_of_birth(date: str):
    if not date:
        return None
    return datetime.strptime(date, "%Y-%m-%d").date()


def format_datetime(date: str):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
