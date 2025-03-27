from collections import UserDict


class Field:
    """
    Base class for all fields in a contact record (e.g., Name, Phone).
    Stores a single string value.
    """
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Represents the contact's name. Required field.
    """
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


class Record:
    """
    Represents a contact record, containing a name and one or more phone numbers.
    """
    def __init__(self, contact_name: str):
        self.name = Name(contact_name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str):
        """Adds a new phone number to the contact."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Removes a phone number from the contact if it exists."""
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        """Replaces an existing phone number with a new one."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            self.phones.append(Phone(new_phone))

    def find_phone(self, phone: str) -> Phone | None:
        """Finds and returns the Phone object matching the given number, or None."""
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    """
    A collection of contact records.
    Inherits from UserDict and allows adding, finding, and deleting records.
    """
    def add_record(self, contact_record: Record):
        """Adds a new Record to the address book."""
        self.data[contact_record.name.value] = contact_record

    def find(self, contact_name: str) -> Record | None:
        """Finds and returns a Record by contact name."""
        return self.data.get(contact_name)

    def delete(self, contact_name: str):
        """Deletes a Record from the address book by name."""
        if contact_name in self.data:
            del self.data[contact_name]


# Example usage
if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Create and add a record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Display all records
    for name, record in book.data.items():
        print(record)

    # Find and edit phone number for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        # Find a specific phone number
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")

    # Delete Jane's record
    book.delete("Jane")
