from datetime import datetime


def get_days_from_today():
    """
    Continuously prompts the user to input a date in the 'YYYY-MM-DD' format until a valid date is entered.
    Then calculates the number of days between the provided date and today's date.

    Returns:
        int: The difference in days between today's date and the entered date.
             The result is negative if the entered date is in the future.
    """
    # Loop until a valid date is provided
    while True:
        # Prompt the user to enter a date in the specified format
        date_str = input("Enter a date in 'YYYY-MM-DD' format: ")
        try:
            # Try to convert the input string into a date object
            input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            break  # If the conversion is successful, exit the loop
        except ValueError:
            # If a ValueError occurs, the date format is incorrect
            print("Invalid date format. Please try again.")

    # Obtain the current date
    current_date = datetime.today().date()
    # Calculate the difference in days between the current date and the entered date
    days_diff = (current_date - input_date).days

    # Output the result
    print(f"Number of days between the entered date and today: {days_diff}")
    # Return the difference
    return days_diff


# Execute the function
get_days_from_today()
