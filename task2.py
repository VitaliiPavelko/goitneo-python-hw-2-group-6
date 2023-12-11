class Field:
    def __init__(self, value):
        if type(value) != str:
            raise TypeError()

        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if len(value) < 1:
            raise ValueError()

        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError()

        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)

        if phone is None:
            """
                that might be custom error like PhoneNotFoundError(ValueError)
                but I woudn't create new file :)
            """
            raise ValueError()

        phone.value = new_phone

class AddressBook():
    def __init__(self):
        self.data = {}


    def add_record(self, record):
        name = record.name.value
        self.data[name] = record


    def find(self, name):
        if name not in self.data:
            return None

        return self.data[name]


    def delete(self, name):
        if name not in self.data:
            return None
        self.data.pop(name)


book = AddressBook()

john_record = Record("John")

p = john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")