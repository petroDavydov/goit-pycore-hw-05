from decorators import input_error


# Add contact

@input_error
def add_contact(args: list, contacts: dict):
    if len(args) != 2:
        raise ValueError()
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Change phone number for existing contact

@input_error
def change_contact(args: list, contacts: dict):
    if len(args) != 2:
        raise ValueError()
    name, phone = args
    if name not in contacts:
        raise KeyError()
    contacts[name] = phone
    return "Contact updated."


# Show phone number for existing contact

@input_error
def show_phone(args: list, contacts: dict):
    if len(args) != 1:
        raise ValueError()
    name = args[0]
    if name not in contacts:
        raise KeyError(f"Error: Contact does not exist.")
    return contacts[name]


# Print all contacts
@input_error
def show_all_contacts(contacts: dict) -> str:
    if not contacts:
        raise KeyError("No contacts found.")
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
