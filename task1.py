"""
    The idea is to map the error to the message
    Usage:

    @input_error(ValueError, "Phone number must be 10 digits")
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
"""
def input_error(err, message):
    def dec(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except err:
                return message

        return inner

    return dec



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args

@input_error(ValueError, "Invalid arguments. Expected: change <username> <phone>")
@input_error(KeyError, "Contact already exists. Use change command to update phone")
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        raise KeyError("Contact already exists")

    contacts[name] = phone

    return "Contact added."


@input_error(KeyError, "Contact does not exist. Use add command first")
@input_error(ValueError, "Invalid arguments. Expected: change <username> <phone>")
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError()

    contacts[name] = phone

    return "Contact updated."


@input_error(KeyError, "Contact does not exist")
@input_error(ValueError, "Invalid arguments. Expected: phone <username>")
def show_phone(args, contacts):
    name, = args

    return contacts[name]

@input_error(ValueError, "No contacts added, use add command to add some")
def show_all(contacts):
    if not len(contacts.keys()):
        raise ValueError

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        command_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(command_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        output = "Invalid command."

        if command == "add":
            output = add_contact(args, contacts)
        elif command == "change":
            output = change_contact(args, contacts)
        elif command == "phone":
            output = show_phone(args, contacts)
        elif command == "all":
            output = show_all(contacts)
        elif command == "hello":
            output = "How can I help you?"

        print(output)


if __name__ == "__main__":
    main()
