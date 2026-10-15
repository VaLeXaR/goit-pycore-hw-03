"""Task 2."""

import random


def get_numbers_ticket(min, max, quantity):
    """Return a sorted list of unique random numbers."""
    if min < 1 or max > 1000:
        return []
    if min > max:
        return []
    if quantity < 1 or quantity > max - min + 1:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()

    return numbers


if __name__ == "__main__":
    print("Your lottery numbers:", get_numbers_ticket(1, 49, 6))
