from pathlib import Path

def get_cats_info(path: str) -> list:
    """
    Reads a text file containing information about cats and returns a list of dictionaries with cat information.

    Each line in the file is expected to be in the format:
        id,name,age

    Parameters:
        path (str): The file path to the cats file.

    Returns:
        list: A list of dictionaries, each with keys "id", "name", and "age".
              If an error occurs, an empty list is returned.
    """
    try:
        # Convert the string path to a Path object
        cats_file_path = Path(path)

        # Use the Path object to open the file
        with cats_file_path.open(mode="r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    cats = []  # List to store the cat information dictionaries

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines, if any

        try:
            cat_id, name, age = line.split(",")
        except ValueError as e:
            print(f"Skipping line due to format error: '{line}'. Error: {e}")
            continue

        # Append the cat information as a dictionary to the list
        cats.append({
            "id": str(cat_id),
            "name": str(name),
            "age": int(age),
        })

    return cats


if __name__ == "__main__":
    # Get the current working directory as a Path object
    current_dir = Path.cwd()

    # Construct the file path to the cats file
    file_path = current_dir / "cats_file.txt"

    # Call the function with the file path
    cats_info = get_cats_info(str(file_path))
    print(cats_info)
