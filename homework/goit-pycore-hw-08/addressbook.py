from collections import UserDict
from datetime import datetime, timedelta
import pickle
import os

# ========================= BASE FIELD AND ITS SUBCLASSES ==========================

class Field:
    """Base class for contact fields."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Represents a contact's name."""
    pass


class Phone(Field):
    """
    Represents a contact's phone number.
    Validates 10-digit numeric format.
    """
    def __init__(self, value: str):
        self._validate(value)
        super().__init__(value)

    @staticmethod
    def _validate(value: str):
        """Check that the phone consists of exactly 10 digits."""
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")


class Birthday(Field):
    """
    Represents a contact's birthday as a date object.
    Accepts date in DD.MM.YYYY format.
    """
    def __init__(self, value: str):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(birthday_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


# =========================== RECORD AND ADDRESSBOOK ===========================

class Record:
    """
    Stores contact information:
    - required name (Name)
    - optional birthday (Birthday)
    - multiple phones (Phone)
    """
    def __init__(self, contact_name: str):
        self.name = Name(contact_name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        """Add a new phone number to the contact."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Remove an existing phone number from the contact."""
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        """Replace old phone with a new phone number."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            self.phones.append(Phone(new_phone))

    def find_phone(self, phone: str) -> Phone | None:
        """Find a phone object in the contact by its value."""
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, birthday: str):
        """Set or update the contact's birthday."""
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones_str}{birthday_str}"
        )


class AddressBook(UserDict):
    """
    A container for storing and managing multiple contact records.
    Supports:
    - add, find, delete contacts
    - upcoming birthday detection
    """
    def add_record(self, record: Record):
        """Add a Record instance to the address book."""
        self.data[record.name.value] = record

    def find(self, contact_name: str) -> Record | None:
        """Find a contact by name. Returns the Record or None."""
        return self.data.get(contact_name)

    def delete(self, contact_name: str):
        """Delete a contact by name, if it exists."""
        if contact_name in self.data:
            del self.data[contact_name]

    def get_upcoming_birthdays(self) -> list[str]:
        """
        Return a list of upcoming birthdays within the next 7 days.
        If birthday falls on weekend, shift congratulations to Monday.
        """
        today = datetime.today().date()
        one_week_later = today + timedelta(days=7)
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year)
                if today <= birthday <= one_week_later:
                    if birthday.weekday() >= 5:
                        birthday += timedelta(days=(7 - birthday.weekday()))
                    formatted = birthday.strftime('%A %d.%m.%Y')
                    upcoming.append(f"{record.name.value}: {formatted}")

        return upcoming


# =============================== FILE OPERATIONS ===============================

DATA_FILE = "addressbook.pkl"


def save_data(book: AddressBook, filename: str = DATA_FILE):
    """
    Save the entire address book to a binary file using pickle.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = DATA_FILE) -> AddressBook:
    """
    Load address book from disk.
    If file doesn't exist, return empty AddressBook instance.
    """
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return AddressBook()


# ============================== ERROR HANDLING ==============================

def input_error(func):
    """
    Decorator for handling common input-related errors
    and returning user-friendly messages.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Please enter valid data."
        except IndexError:
            return "Not enough arguments. Please check your input."
    return wrapper


# ============================== COMMAND HANDLERS ==============================

@input_error
def add_contact(args, book: AddressBook):
    """
    Add a contact or append a phone number to an existing contact.
    Usage: add [name] [phone]
    """
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """
    Change an existing phone number for a contact.
    Usage: change [name] [old_phone] [new_phone]
    """
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."
    record.edit_phone(old_phone, new_phone)
    return f"{name}'s phone updated."


@input_error
def show_phone(args, book: AddressBook):
    """
    Show all phone numbers for a contact.
    Usage: phone [name]
    """
    name, *_ = args
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."
    return f"{name}: {', '.join(p.value for p in record.phones)}"


@input_error
def show_all(book: AddressBook):
    """
    Display all contacts in the address book.
    Usage: all
    """
    if not book.data:
        return "No contacts found."
    return "\n".join(str(r) for r in book.data.values())


@input_error
def add_birthday(args, book: AddressBook):
    """
    Add a birthday to an existing contact.
    Usage: add-birthday [name] [DD.MM.YYYY]
    """
    name, birthday_str, *_ = args
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."
    record.add_birthday(birthday_str)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    """
    Show a contact's birthday if it exists.
    Usage: show-birthday [name]
    """
    name, *_ = args
    record = book.find(name)
    if not record:
        return f"Contact '{name}' not found."
    if not record.birthday:
        return f"No birthday set for {name}."
    return f"{name}'s birthday is {record.birthday}"


@input_error
def birthdays(book: AddressBook):
    """
    Show list of upcoming birthdays within the next 7 days.
    Usage: birthdays
    """
    result = book.get_upcoming_birthdays()
    return "\n".join(result) if result else "No birthdays this week."
