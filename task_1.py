"""Task 1."""

from datetime import datetime


def get_days_from_today(date):
    """Return the number of days from the given date to today."""
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ValueError("The date must be in the YYYY-MM-DD format")

    # Use only the date, so the time does not affect the result.
    today = datetime.today().date()
    given_date = given_date.date()

    difference = today - given_date
    return difference.days


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))
    print(get_days_from_today("2027-10-09"))
