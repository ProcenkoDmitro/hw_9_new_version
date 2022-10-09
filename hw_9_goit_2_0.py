import time
PHONE_BOOK = {

}

def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return wrapper


@input_error
def hello_handler():    
    return 'How can I help you?'


@input_error
def quit_handler():    
    return 'Good bye, see you soon:)'


@input_error
def add_contact_handler(data):    
    name, phone = create_data(data)
    if name in PHONE_BOOK:
        raise ValueError('A contact with that name is already exist!')
    PHONE_BOOK[name] = phone
    return f'New contact has been added: {name}: {phone}.'


@input_error
def change_handler(data):    
    name, phone = create_data(data)
    if name in PHONE_BOOK:
        PHONE_BOOK[name] = phone
        return f'You changed phone to {name}. New phone is {name}.'
    return 'Use add command plz.'


@input_error
def phone_handler(name):    
    if name.strip() not in PHONE_BOOK:
        raise ValueError('This contact does not exist.')
    return PHONE_BOOK.get(name.strip())


@input_error
def show_all_handler():    
    contacts = ''
    for key, value in PHONE_BOOK.items():
        contacts += f'{key} : {value} \n'
    return contacts


COMMANDS_DICT = {
        'hello': hello_handler, 
        'add': add_contact_handler,
        'change': change_handler,
        'phone': phone_handler,
        'show all': show_all_handler, 
        'good bye': quit_handler,
        'close': quit_handler,
        'exit': quit_handler
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_command)


def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Smth wrong with name.')
    if not phone.isnumeric():
        raise ValueError('Smth wrong with phone.')
    return name, phone


def break_command():    
    return 'Sorry, I can`t understand you('


def main():    
    print('Hello, your assistants start working)')
    while True:
        user_input = input('')
        result = change_input(user_input)
        time.sleep(1)
        print(result)
        if result == 'Good bye, see you soon:)':
            quit()


if __name__ == '__main__':
    main()