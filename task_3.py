"""Task 3: normalize Ukrainian phone numbers."""

import re


def normalize_phone(phone_number):
    """Return a phone number in the +380XXXXXXXXX format."""
    # Remove spaces, brackets, hyphens, and other extra characters.
    phone_number = re.sub(r"\D", "", phone_number)

    # Add the missing international prefix.
    if phone_number.startswith("380"):
        return "+" + phone_number

    return "+38" + phone_number


if __name__ == "__main__":
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
