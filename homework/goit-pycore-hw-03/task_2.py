import random


def generate_lottery_ticket(min_val: int, max_val: int, quantity: int) -> list:
    """
    Generates a sorted list of unique random numbers within a specified range.
    Returns an empty list if any parameter is invalid.

    Parameters:
        min_val (int): Minimum possible number (must be >= 1).
        max_val (int): Maximum possible number (must be <= 1000).
        quantity (int): Number of unique numbers to draw. It must be between 1
                        and the total number of available numbers in the range [min_val, max_val].

    Returns:
        list: A sorted list of unique random numbers if parameters are valid, otherwise an empty list.
    """
    # Validate all parameters in one compound condition
    if not (
        all(isinstance(x, int) for x in (min_val, max_val, quantity))
        and min_val >= 1
        and max_val <= 1000
        and 1 <= quantity <= (max_val - min_val + 1)
    ):
        return []

    # Generate and return the sorted list of unique random numbers
    return sorted(random.sample(range(min_val, max_val + 1), quantity))


# Replace 'min_val', 'max_val', and 'quantity' with your desired values:
print(f"Your lottery numbers: {generate_lottery_ticket(min_val, max_val, quantity)}")
