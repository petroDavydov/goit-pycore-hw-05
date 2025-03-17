from managed_contacts import *


CMD_CLOSE = {"close", "exit"}
CMD_HELLO = {"hello"}
CMD_ALL = {"all"}
CMD_ADD = {"add"}
CMD_CHANGE = {"change"}
CMD_PHONE = {"phone"}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in CMD_CLOSE:
            print("Good bye!")
            break
        elif command in CMD_HELLO:
            print("How can I help you?")
        elif command in CMD_ADD:
            print(add_contact(args, contacts))
        elif command in CMD_CHANGE:
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command in CMD_ALL:
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
