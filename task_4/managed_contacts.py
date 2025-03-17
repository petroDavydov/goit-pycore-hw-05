from decorators import input_error


@input_error
def add_contact(args:list, contacts:dict):
    if len(args) != 2:
        raise ValueError()
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args:list, contacts:dict):
    if len(args) != 2:
        raise ValueError()
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError()


@input_error
def show_phone(args:list, contacts:dict):
    if len(args) != 1:
        raise ValueError()
    name = args[0]
    return contacts.get(name, "Contact not found.")


@input_error
def show_all(contacts:dict):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts found."
