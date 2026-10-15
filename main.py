"""Run examples for all completed homework tasks."""

from task_1 import get_days_from_today
from task_2 import get_numbers_ticket
from task_3 import normalize_phone
from task_4 import get_upcoming_birthdays


def main() -> None:
    """Print example results for all completed tasks."""
    print(get_days_from_today("2020-10-09"))
    print(get_days_from_today("2027-10-09"))
    print("Your lottery numbers:", get_numbers_ticket(1, 49, 6))

    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    normalized_numbers = [normalize_phone(number) for number in raw_numbers]
    print("Normalized phone numbers:", normalized_numbers)

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


if __name__ == "__main__":
    main()
