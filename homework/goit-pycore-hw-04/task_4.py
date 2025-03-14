def parse_input(user_input: str) -> tuple:
    """
    Splits the user input into command and arguments.
    The command is converted to lowercase, while arguments remain as typed.
    Returns a tuple: (command, [arg1, arg2, ...]).
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].lower().strip()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts: dict) -> str:
    """
    Adds a new contact to the dictionary or overwrites an existing one.
    Expects exactly 2 arguments: [name, phone].
    Returns a message indicating success or an error.
    """
    try:
        name, phone = args
    except ValueError:
        return "Error: 'add' command requires 2 arguments: name and phone."

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict) -> str:
    """
    Changes the phone number for an existing contact.
    Expects exactly 2 arguments: [name, new_phone].
    Returns a message indicating success or an error if the contact doesn't exist.
    """
    try:
        name, new_phone = args
    except ValueError:
        return "Error: 'change' command requires 2 arguments: name and new_phone."

    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Error: contact '{name}' not found."

def show_phone(args, contacts: dict) -> str:
    """
    Shows the phone number for a given contact.
    Expects exactly 1 argument: [name].
    Returns the phone number or an error message if not found.
    """
    if len(args) != 1:
        return "Error: 'phone' command requires exactly 1 argument: name."

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: contact '{name}' not found."

def show_all(contacts: dict) -> str:
    """
    Returns a string representation of all contacts.
    If no contacts are stored, returns a message indicating that.
    """
    if not contacts:
        return "No contacts found."
    result_lines = []
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")
    return "\n".join(result_lines)

def main() -> None:
    """
    Main function implementing the console assistant bot:
    - Keeps contacts in a dictionary.
    - Runs an infinite loop to process user commands.
    - Exits when the user types 'close' or 'exit'.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    # Main loop
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":  # Empty command
            continue

        else:
            print("Invalid command.")

# Run the main function
if __name__ == "__main__":
    main()
