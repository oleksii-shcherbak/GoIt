import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to a standard format by keeping only digits and a leading '+'.

    The function removes all characters except digits and the '+' sign at the beginning.
    If the international code is missing:
      - If the number starts with "380", it prepends a '+'.
      - Otherwise, it prepends "+38".

    Parameters:
        phone_number (str): The phone number in any format.

    Returns:
        str: The normalized phone number.
    """
    # Remove whitespace and check if the phone number starts with a '+'
    s = phone_number.strip()
    has_plus = s.startswith("+")

    # Remove all non-digit characters from the phone number
    digits = re.sub(r"\D", "", s)

    # Build the normalized phone number based on the presence of the international code
    if has_plus:
        normalized = "+" + digits
    else:
        if digits.startswith("380"):
            normalized = "+" + digits
        else:
            normalized = "+38" + digits

    return normalized


# A list of raw phone numbers in various formats
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

# Initialize an empty list to store the normalized phone numbers
sanitized_numbers = []
for phone_number in raw_numbers:
    normalized = normalize_phone(phone_number)
    sanitized_numbers.append(normalized)

print(f"Normalized phone numbers for SMS campaign: {sanitized_numbers}")
