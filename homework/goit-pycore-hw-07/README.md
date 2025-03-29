# CLI Assistant Bot

The assistant consists of two Python files: `main.py` and `addressbook.py`.

This structure was intentionally chosen to keep the project organized and readable:

- `main.py` contains the user interface and command processing logic.
- `addressbook.py` contains the class definitions, core functionality, and command handlers.

## Features

- Add and update contacts
- Store multiple phone numbers per contact
- Add and show birthdays
- View all contacts
- Display upcoming birthdays in the next 7 days
- Graceful error handling for invalid input

## Supported Commands

| Command                                  | Description                                   |
|------------------------------------------|-----------------------------------------------|
| `add [name] [phone]`                     | Add a new contact or phone to an existing one |
| `change [name] [old_phone] [new_phone]`  | Change a phone number for a contact           |
| `phone [name]`                           | Show all phone numbers for a contact          |
| `all`                                    | Show all contacts                             |
| `add-birthday [name] [DD.MM.YYYY]`       | Add a birthday to a contact                   |
| `show-birthday [name]`                   | Show the birthday of a contact                |
| `birthdays`                              | Show upcoming birthdays for the next 7 days   |
| `hello`                                  | Display greeting                              |
| `help`                                   | Display list of supported commands            |
| `close` / `exit`                         | Exit the assistant                            |
