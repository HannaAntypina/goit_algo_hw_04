def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue  
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            hello()
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command. Please enter a valid command.")

def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args
    
    
    valid_commands = ["hello", "add", "change", "phone", "all", "exit", "close"]
    if command not in valid_commands:
        print("Invalid command.")
        return None, []

    return command, args

def hello():
    print("How can I help you?")

def add_contact(args, contacts):
    if len(args) != 2:
        print("Invalid command. Usage: add [name] [phone]")
        return
    name, phone = args
    contacts[name] = phone
    print("Contact added.")
def change_contact(args, contacts):
    if len(args) != 2:
        print("Invalid command. Usage: change [name] [phone]")
        return
    name, new_phone = args
    if name not in contacts:
        print("Contact not found.")
        return
    contacts[name] = new_phone
    print("Contact updated.")

def show_phone(args, contacts):
    if len(args) != 1:
        print("Invalid command. Usage: phone [name]")
        return
    name = args[0]
    if name not in contacts:
        print("Contact not found.")
        return
    print(contacts[name])

def show_all(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

if __name__ == "__main__":
    main()