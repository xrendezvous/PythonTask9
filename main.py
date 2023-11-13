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
    return f"Contact {name} added with phone number {phone}"

@input_error
def change(*args, **kwargs):
    name, phone = args
    if name in user:
        user[name] = phone
        return f"Phone number for {name} updated to {phone}"
    else:
        return KeyError

@input_error
def phone(*args, **kwargs):
    name = args[0]
    if name in user:
        return f"The phone number for {name} is {user[name]}"
    else:
        return KeyError
def exit_handler():
    return

