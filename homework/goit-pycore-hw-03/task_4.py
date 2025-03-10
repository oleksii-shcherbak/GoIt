from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Returns a list of dictionaries for users who have birthdays within the next 7 days (including today).
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday.

    Each user in the input list is a dictionary with:
        - 'name': user's name (string)
        - 'birthday': user's birthday (string in the format 'YYYY.MM.DD')

    The returned list contains dictionaries with:
        - 'name': user's name
        - 'congratulation_date': greeting date as a string in the format 'YYYY.MM.DD'

    Parameters:
        users (list): List of random user dictionaries with birthday information.

    Returns:
        list: A list of dictionaries with upcoming birthday greetings.
    """
    result = []  # List to store users with upcoming birthdays
    today = datetime.today().date()  # Current date

    for user in users:
        # Parse the user's birthday string into a date object
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            # If the birthday format is incorrect, skip this user
            continue

        # Create a birthday date for the current year
        birthday_this_year = birthday.replace(year=today.year)
        # If the birthday has already passed this year, use next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Calculate the number of days between today and the birthday.
        delta_days = (birthday_this_year - today).days

        # Check if the birthday is within the next 7 days (including today)
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # If the birthday falls on Saturday (weekday() == 5) or Sunday (weekday() == 6),
            # adjust the congratulation date to the following Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            # Append the user's name and the formatted congratulation date to the result list
            result.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return result


# List of random users with their names and birthdays in the format 'YYYY.MM.DD'
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.13"},
    {"name": "Alice Brown", "birthday": "1995.03.15"},
    {"name": "Bob White", "birthday": "2000.03.09"},
]

# Call the function to get upcoming birthdays and print the results
upcoming_birthdays = get_upcoming_birthdays(users)
print(f"List of greetings for this week: {upcoming_birthdays}")
