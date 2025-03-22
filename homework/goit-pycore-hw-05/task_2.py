import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Extracts all valid floating-point numbers from the input text and yields them one by one.

    A valid number is defined as a float (with a decimal point) that is surrounded by word boundaries.

    Args:
        text (str): Input text containing numbers and other content.

    Yields:
        float: Each valid floating-point number found in the text.
    """
    pattern = r'\b\d+\.\d+\b'
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total profit by summing all floating-point numbers generated from the input text.

    Args:
        text (str): Input text containing numbers.
        func (Callable): A generator function that extracts float numbers from text.

    Returns:
        float: Total sum of the extracted float numbers.
    """
    return sum(func(text))


if __name__ == "__main__":
    example_text = (
        "The employee's total income consists of several parts: 1000.01 as the base income, "
        "supplemented by additional earnings of 27.45 and 324.00 dollars."
    )

    total_income = sum_profit(example_text, generator_numbers)
    print(f"Total income: {total_income}")
