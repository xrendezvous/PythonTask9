def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone number'
        except IndexError:
            return 'Enter user name'

    return inner

user = {}

def hello_handler():
    return 'Hello, how can I help you?'

@input_error
def add(*args, **kwargs):
    name, phone = args
    user[name] = phone
    return f"Contact {name.capitalize()} added with phone number {phone}"

@input_error
def change(*args, **kwargs):
    name, phone = args
    if name in user:
        user[name] = phone
        return f"Phone number for {name.capitalize()} updated to {phone}"
    else:
        return KeyError

@input_error
def get_phone(*args, **kwargs):
    name = args[0]
    if name in user:
        return f"The phone number for {name.capitalize()} is {user[name]}"
    else:
        return KeyError

@input_error
def show_all(*args, **kwargs):
    if user:
        contacts = "\n".join(f"{name.capitalize()}: {phone}" for name, phone in user.items())
        return f"All contacts:\n{contacts}"
    else:
        return "No contacts available"

def exit_handler():
    return "Good bye!"

def main():
    while True:
        command = input("Enter a command: ").lower()
        if command in ["good bye", "close", "exit"]:
            print(exit_handler())
            break
        elif command == "hello":
            print(hello_handler())
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add(name, phone))
            except ValueError:
                print("Give me name and phone number")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change(name, phone))
            except ValueError:
                print("Give me name and phone number")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except IndexError:
                print("Give me name and phone number")
        elif command == "show all":
            print(show_all())
        else:
            print("Invalid command. Please, try again")

if __name__ == "__main__":
    main()

