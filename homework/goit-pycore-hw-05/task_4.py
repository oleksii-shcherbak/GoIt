def input_error(func):
    """
    Decorator that handles common user input errors and returns friendly messages.
    Catches ValueError, KeyError, and IndexError without stopping the program.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter a valid user name."
        except IndexError:
            return "Enter the argument for the command."
    return wrapper


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


@input_error
def add_contact(args, contacts: dict) -> str:
    """
    Adds a new contact to the dictionary or overwrites an existing one.
    Expects exactly 2 arguments: [name, phone].
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict) -> str:
    """
    Changes the phone number for an existing contact.
    Expects exactly 2 arguments: [name, new_phone].
    """
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args, contacts: dict) -> str:
    """
    Shows the phone number for a given contact.
    Expects exactly 1 argument: [name].
    """
    name = args[0]
    return contacts[name]


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

        elif command == "":
            continue

        else:
            print("Invalid command.")


# Run the main function
if __name__ == "__main__":
    main()
