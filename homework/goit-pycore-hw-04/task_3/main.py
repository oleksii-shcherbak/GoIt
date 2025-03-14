from pathlib import Path
from colorama import init, Fore, Style
import sys


def sort_key(path: Path) -> str:
    """
    Returns the name of the path in lower-case for case-insensitive sorting.
    """
    return path.name.lower()


def print_dir_structure(directory: Path, indent_level: int = 0) -> None:
    """
    Recursively prints the structure of the given directory with colored output.

    Directories are printed in blue with a trailing slash.
    Files are printed in green.
    Items are indented based on their level in the directory tree.
    """
    # Get items in the directory, sorted alphabetically (case-insensitive)
    items = sorted(directory.iterdir(), key=sort_key)
    for item in items:
        indent = "    " * indent_level  # 4 spaces per indent level
        if item.is_dir():  # If the item is a directory
            # Print directory name in blue with a trailing slash
            print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            # Recursively print the contents of the subdirectory
            print_dir_structure(item, indent_level + 1)
        else:
            # Print file name in green
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main() -> None:
    """
    Main function that:
      - Initializes colorama for colored output.
      - Reads a directory path from the command-line arguments.
      - Checks if the path exists and is a directory.
      - Prints the directory structure with colored output.
    """
    init(autoreset=True)  # Initialize colorama for colored output

    if len(sys.argv) < 2:  # If no directory path is provided
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    # Get the directory path from the command-line arguments
    directory_path = Path(sys.argv[1])

    if not directory_path.exists():  # If the path does not exist
        print(f"Error: The specified path does not exist -> {directory_path}")
        sys.exit(1)

    if not directory_path.is_dir():  # If the path is not a directory
        print(f"Error: The specified path is not a directory -> {directory_path}")
        sys.exit(1)

    print(f"Structure of directory: {directory_path}\n")
    print_dir_structure(directory_path)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
