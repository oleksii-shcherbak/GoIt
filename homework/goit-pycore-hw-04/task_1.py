def total_salary(path: str) -> tuple:
    """
    Reads a text file containing developer salaries and computes the total and average salary.

    Each line in the file is expected to be in the format:
        Name,Salary

    Parameters:
        path (str): The file path to the salary file.

    Returns:
        tuple: (total, average) where:
            - total is the sum of all salaries.
            - average is the average salary.
          If any error occurs, (0, 0) is returned.
    """
    try:
        # Open the file with the specified encoding and read all lines
        with open(path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        # Handle exceptions and return default values
        print(f"Error reading file: {e}")
        print("Total salary: 0, Average salary: 0")
        return 0, 0

    total = 0  # To accumulate the total salary
    count = 0  # To count the number of valid salary entries

    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if not line:
            continue  # Skip empty lines if they exist

        try:
            # Split the line into name and salary parts
            name, salary_str = line.split(',')
            salary = int(salary_str)  # Convert the salary string to an integer
        except ValueError as ve:
            # If a line doesn't conform to the expected format, skip it
            print(f"Skipping line due to format error: '{line}'. Error: {ve}")
            continue

        total += salary
        count += 1

    # Compute the average salary and avoid division by zero
    average = total / count if count else 0

    print(f"Total salary: {total}, Average salary: {average}")
    return total, average

# Example usage
total_salary("salary_file.txt")
