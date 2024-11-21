import text_ru


def print_menu() -> None:
    '''Вывод списка меню '''
    print("Выберите действие: ")
    for i, item in enumerate(text_ru.MENU, 1):
        print(f'{i}. {item} ')


def user_input(msg: str = '') -> str:
    '''Запрос данных у пользователя через консоль'''
    return input(msg)


def print_msg(msg: str) -> None:
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

def print_phonebook(contacts: dict[int,dict[str, str]]) -> None:
    '''Печать в консоль контакста'''
    for key, value in contacts.items():
        print('Контакт с id:', key)
        print(' '*4, 'name: ', value['name'])
        print(' '*4, 'surname: ', value['surname'])
        print(' '*4, 'phone_number: ', value['phone_number'])
        print(' '*4, 'comment: ', value['comment'], '\n')

def add_contact_ask_fields():
    contact = {'name': user_input("Введите имя: "), 'surname': user_input("Введите фамилию: "),
               'phone_number': user_input("Введите номер телефона: "), 'comment': user_input("Введите комментарий: ")}
    return contact



