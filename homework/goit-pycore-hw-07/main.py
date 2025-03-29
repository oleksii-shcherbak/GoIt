from addressbook import (
    AddressBook, add_contact, change_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays
)


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses raw user input into a command and list of arguments.
    Returns an empty command if input is blank.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def print_help():
    """
    Displays a well-formatted list of available commands.
    """
    commands = {
        "add [name] [phone]": "Add a new contact or phone to existing contact",
        "change [name] [old] [new]": "Change a phone number",
        "phone [name]": "Show phone numbers for a contact",
        "all": "Show all contacts",
        "add-birthday [name] [DD.MM.YYYY]": "Add birthday to a contact",
        "show-birthday [name]": "Show birthday for a contact",
        "birthdays": "Show upcoming birthdays in the next 7 days",
        "hello": "Get a greeting from the bot",
        "close / exit": "Exit the program"
    }

    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd.ljust(35)} - {desc}")
    print()


def main():
    """
    Command-line assistant for managing contacts.
    """
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "":
            continue

        elif command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "help":
            print_help()

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
