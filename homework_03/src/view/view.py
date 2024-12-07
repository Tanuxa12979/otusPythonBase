from homework_03.src.view import text_ru


def print_menu() -> None:
    """
    Вывод списка меню
    :return: none
    """
    print("Выберите действие: ")
    for i, item in enumerate(text_ru.MENU, 1):
        print(f'{i}. {item} ')


def user_input(msg: str = '') -> str:
    """
    Запрос данных у пользователя через консоль
    :param msg: текст отображаемый в консоли
    :return: введенное пользователем значение
    """
    return input(msg)


def print_msg(msg: str) -> None:
    """
    Вывод сообщения в консоль
    :param msg: текст сообщения
    :return: none
    """
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


def print_phonebook(contacts: dict[int, dict[str, str]]) -> None:
    """
    Вывод информации по переданным контактам в консоль
    :param contacts: словарь словарей с переданными контактами
    :return: none
    """
    for key, value in contacts.items():
        print(f'| Contact {key: <4} |name:{value["name"]: <8}| surname:{value["surname"]:<8} |phone_number:{value["phone_number"]:<15} |comment:{value["comment"]:<15} |')
    print("\n")


def add_contact_ask_fields() -> dict[str, str]:
    """
    Получение от пользователя значений полей нового контакта и формирование словаря
    :return: словарь, где ключи - поля контакта, значения - введенные пользователем значения
    """
    contact = {'name': user_input("Введите имя: "), 'surname': user_input("Введите фамилию: "),
               'phone_number': user_input("Введите номер телефона: "), 'comment': user_input("Введите комментарий: ")}
    return contact



