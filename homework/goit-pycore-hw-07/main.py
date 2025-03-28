from collections import UserDict
from datetime import datetime, timedelta


class Field:
    """
    Base class for all fields in a contact record.
    Stores a single string or parsed value.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Represents the contact's name. Required field."""
    pass


class Phone(Field):
    """
    Represents a phone number. Validates that the number consists of exactly 10 digits.
    """
    def __init__(self, value: str):
        self._validate(value)
        super().__init__(value)

    @staticmethod
    def _validate(value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")


class Birthday(Field):
    """
    Represents a birthday. Validates format DD.MM.YYYY and stores as datetime.date.
    """
    def __init__(self, value: str):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(birthday_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    """
    Represents a contact record, containing a name, list of phones, and optional birthday.
    """
    def __init__(self, contact_name: str):
        self.name = Name(contact_name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            self.phones.append(Phone(new_phone))

    def find_phone(self, phone: str) -> Phone | None:
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"


class AddressBook(UserDict):
    """
    A collection of contact records. Inherits from UserDict and allows
    adding, finding, deleting records, and retrieving upcoming birthdays.
    """
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, contact_name: str) -> Record | None:
        return self.data.get(contact_name)

    def delete(self, contact_name: str):
        if contact_name in self.data:
            del self.data[contact_name]

    def get_upcoming_birthdays(self) -> list[str]:
        """
        Returns a list of users to congratulate during the upcoming week.
        If birthday falls on weekend, it is moved to Monday.
        """
        today = datetime.today().date()
        one_week_later = today + timedelta(days=7)
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= one_week_later:
                    celebration_day = birthday_this_year
                    if birthday_this_year.weekday() >= 5:  # Saturday or Sunday
                        # Move to next Monday
                        offset = 7 - birthday_this_year.weekday()
                        celebration_day = birthday_this_year + timedelta(days=offset)
                    formatted = celebration_day.strftime('%A %d.%m.%Y')
                    upcoming_birthdays.append(f"{record.name.value}: {formatted}")

        return upcoming_birthdays


# Example usage
if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john = Record("John")
    john.add_phone("1234567890")
    john.add_phone("5555555555")
    john.add_birthday("29.03.1998")
    book.add_record(john)

    # Create and add a record for Jane
    jane = Record("Jane")
    jane.add_phone("9876543210")
    jane.add_birthday("01.04.1992")
    book.add_record(jane)

    print("All contacts:")
    for contact in book.data.values():
        print(contact)

    print("\nUpcoming birthdays this week:")
    for line in book.get_upcoming_birthdays():
        print(line)
