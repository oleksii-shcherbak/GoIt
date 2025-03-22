import sys


def parse_log_line(line: str) -> dict:
    """
    Parses a single line of the log file and extracts date, time, level, and message.

    Args:
        line (str): A line from the log file.

    Returns:
        dict: Parsed log components as keys: date, time, level, message.
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list[dict]:
    """
    Loads and parses all logs from the given file path.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list[dict]: List of parsed log entries.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parse_log_line(line) for line in file if parse_log_line(line)]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read file '{file_path}'.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    """
    Filters logs by the specified level.

    Args:
        logs (list[dict]): The list of log entries.
        level (str): The level to filter by.

    Returns:
        list[dict]: Filtered list of logs.
    """
    return list(filter(lambda log: log["level"].upper() == level.upper(), logs))


def count_logs_by_level(logs: list[dict]) -> dict[str, int]:
    """
    Counts the number of logs per logging level.

    Args:
        logs (list[dict]): The list of log entries.

    Returns:
        dict[str, int]: A dictionary with levels as keys and counts as values.
    """
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict[str, int]) -> None:
    """
    Displays log counts in a formatted table.

    Args:
        counts (dict[str, int]): Dictionary of log level counts.
    """
    print("Log Level        | Count")
    print("-----------------|-------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_log_details(logs: list[dict], level: str) -> None:
    """
    Displays detailed logs for a specific level.

    Args:
        logs (list[dict]): The full list of logs.
        level (str): The level to display details for.
    """
    filtered_logs = filter_logs_by_level(logs, level)
    if not filtered_logs:
        print(f"No log entries found for level '{level.upper()}'.")
        return

    print(f"\nLog details for level '{level.upper()}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    """
    Entry point of the script. Parses command-line arguments and displays log analysis.
    """
    if len(sys.argv) < 2:
        print("Usage: python task_3.py sample.log [LEVEL]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        display_log_details(logs, level_filter)


if __name__ == "__main__":
    main()
