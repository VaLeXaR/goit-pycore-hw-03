"""Task 4: find upcoming birthdays."""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """Return birthdays that are today or within the next seven days."""
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Use the next year's birthday if this year's birthday has passed.
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Move weekend congratulations to the following Monday.
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime(
                        "%Y.%m.%d"
                    ),
                }
            )

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.10.16"},
        {"name": "Jane Smith", "birthday": "1990.10.18"},
        {"name": "Olena Kovalenko", "birthday": "1992.10.22"},
        {"name": "Michael Brown", "birthday": "1988.11.05"},
        {"name": "Sofia Wilson", "birthday": "1995.11.20"},
        {"name": "Andriy Shevchenko", "birthday": "1991.12.03"},
        {"name": "Maria Johnson", "birthday": "1987.12.25"},
        {"name": "David Miller", "birthday": "1990.01.10"},
    ]

    print("Upcoming birthdays:", get_upcoming_birthdays(users))
