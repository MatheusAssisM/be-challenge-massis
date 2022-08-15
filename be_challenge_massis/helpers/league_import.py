from datetime import datetime


def format_date_of_birth(date: str):
    if not date:
        return None
    return datetime.strptime(date, "%Y-%m-%d").date()
