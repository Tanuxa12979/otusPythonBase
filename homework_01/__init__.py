import json
import os

MENU = '''
------------------------------
Выберите действие:
1 - открыть файл
2 - сохранить файл
3 - показать все контакты
4 - добавить контакт
5 - найти контакт
6 - изменить контакт
7 - удалить контакт
8 - выход
'''

# поля в файле: id, firstname, surname, phone_number, comment


# 1 Выбор файла для дальнейшей работы
def choose_and_open_file():
    k = 1
    while k:
        filename = input('''
Введите имя файла (необходимо указать абсолютный путь в формате D:/users/username/path/filename.json).
Для выбора файла по умолчанию нажмите enter без ввода доп информации.
Для возврата в главное меню введите 0
''')
        if filename == '0':
            return None, None
        if not filename:
            filename = 'contacts.json'
            print(f"\nНачинаем работу с файлом {filename}\n")
            k = 0
        else:
            if filename.count('\\') > 0:
                print("Имя файла должно быть указано в след. формате D:/users/username/path/filename.json. Обратите внимание на направление слеша")
                continue
            elif filename[-5:] != '.json':
                print("\nВыберите файл с расширением json")
                continue
            elif not os.path.isfile(filename):
                print("Такой файл не существует, попробуйте снова")
                continue
            else:
                k = 0
                print(f"\nНачинаем работу с файлом {filename}\n")
        with open(filename, "r") as my_file:
            contacts_json = my_file.read()
        contacts = json.loads(contacts_json)
    return contacts, filename


# 2 Сохранение информации в файл после работы
def save_info_in_file(filename, contacts):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file)
    print("Данные успешно сохранены")


def show_contact(user):
    print('Контакт: ', user['id'], end='\n')
    print('Имя: ', user['name'])
    print('Фамилия: ', user['surname'])
    print('Номер телефона: ', user['phone_number'])
    print('Комментарий: ', user['comment'], end='\n\n')


# 3 Вывод списка контактов в консоль
def show_all_contacts(contacts):
    for user in contacts['users']:
        show_contact(user)
    print("Конец записной книжки\n")


def max_id(contact_list):
    max_id = 0
    for contact in contact_list['users']:
        if contact['id'] > max_id:
            max_id = contact['id']
    return max_id


# 4. Добавление контакта
def add_contact(contacts):
    name = input("Введите имя ")
    surname = input("Введите фамилию ")
    phone_number = input("Введите номер телефона ")
    comment = input("Введите комментарий ")

    new_contact = {}
    new_contact['id'] = max_id(contacts)+1
    new_contact['name'] = name
    new_contact['surname'] = surname
    new_contact['phone_number'] = phone_number
    new_contact['comment'] = comment

    contacts['users'].append(new_contact)
    print("Пользователь успешно добавлен ")
    return contacts


# 5. Поиск по контактам можно делать отдельно по полям (имя, телефон, комментарий), так и общий (поисковое слово ищет сразу во всех полях контакта)
def find_contact(contacts):
    str_for_search = input('Введите строку для поиска ')
    contact_list = []
    for contact in contacts['users']:
        if (str_for_search in str(contact['id'])) or (str_for_search in contact['name']) or (str_for_search in contact['surname']) or (str_for_search in contact['phone_number']) or (str_for_search in contact['comment']):
            contact_list.append(contact)
    if contact_list:
        print("\nБыли найдены след. констакты: ")
        for contact in contact_list:
            show_contact(contact)
    else:
        print(f"Ни один контакт не был найден по строке {str_for_search} ")


# 6 Изменение контакта
def edit_contact(contacts):
    id = input("Введите айди контакта для изменения ")
    if id.isdecimal():
        for contact in contacts['users']:
            if contact['id'] == int(id):
                print("Контакт найден:")
                show_contact(contact)

                while True:
                    k = input('''
Выберите поле для изменения (введите номер):
1. Имя
2. Фамилия
3. Номер телефона
4. Комментарий
5. Возврат в главное меню
''')
                    a = {'1': 'name', '2': 'surname', '3': 'phone_number', '4': 'comment'}
                    if k == '5':
                        return None
                    elif k != '1' and k != '2' and k != '3' and k != '4':
                        print("Необходимо ввести одно из 5 значений. Контакт не был изменен")
                    else:
                        val = input(f'Введите новое значение для поля {a[k]} ')
                        contact[a[k]] = val
                        print("Поле было успешно изменено. Контакт имеет вид:")
                        show_contact(contact)
                        return None

    else:
        print("Необходимо ввести корректный номер (айди) контакта (целое положительное число). Контакт не был изменен")
    print("Контакта с таким номером не существует ")


def delete_contact_by_id(id, contacts):
    is_contact_in_list = False
    contact_index = 0
    status = 0
    for contact in contacts['users']:
        if contact['id'] == id and not is_contact_in_list:
            is_contact_in_list = True
            break
        contact_index += 1
    if not is_contact_in_list:
        print("Введенный контакт отсутствует в списке ")
    else:
        contacts['users'].pop(contact_index)
        print("Контакт успешно удален ")
        status = 1
    return contacts, status


def delete_contact_by_name(name, surname, contacts):
    is_contact_in_list = False
    contact_index = 0
    status = 0
    for contact in contacts['users']:
        if contact['name'] == name and contact['surname'] == surname and not is_contact_in_list:
            is_contact_in_list = True
            break
        contact_index += 1
    if not is_contact_in_list:
        print("Введенный контакт отсутствует в списке ")
    else:
        contacts['users'].pop(contact_index)
        print("Контакт успешно удален ")
        status = 1
    return contacts, status


# 7 Удаление контакта
def delete_contact(contacts):
    delete_con = ''
    while delete_con != '1' or delete_con != 2 or delete_con != 3:
        delete_con = input('''
Выберите действие:
1. Удалить контакт по его номеру (айди)
2. Удалить контакт по фамилии и имени
3. Выход в главное меню
''')

        if delete_con == '1':
            n = input("Введите номер (айди) контакта для удаления ")
            if n.isdecimal():
                contacts, status = delete_contact_by_id(int(n), contacts)
                return contacts, status
            else:
                print("Необходимо ввести корректный номер контакта (целое положительное число). Контакт не был удален")
        elif delete_con == '2':
            name = input("Введите имя контакта для удаления ")
            surname = input("Введите фамилию контакта для удаления ")
            contacts, status = delete_contact_by_name(name, surname, contacts)
            return contacts, status
        elif delete_con == '3':
            return contacts, 0
        else:
            print("Необходимо выбрать одно из предложенных ниже действий.", end=' ')


def menu():
    choice = 1
    is_file_opened = False
    is_info_saved = True
    filename = ''
    contacts = ''
    while choice != '8':
        choice = input(MENU)
        if not choice.isdecimal():
            print("Необходимо выбрать один из пунктов меню, попробуйте снова.")
            continue
        if int(choice) <= 0 or int(choice) > 8:
            print("Вы ввели неверное значение, попробуйте снова выбрать действие.")
            continue
        if choice == '8':
            if is_file_opened and not is_info_saved:
                should_save = input("Имеются несохраненные данные. Для сохранения введите save, иначе будет осуществлен выход без сохранения ")
                if should_save == 'save':
                    save_info_in_file(filename, contacts)
            print("Работа окончена. До свидания!")
            break
        elif choice == '1':
            contacts, filename = choose_and_open_file()
            if contacts is None:
                is_file_opened = False
                continue
            else:
                is_file_opened = True
        elif not is_file_opened:
            print("Сначала необходимо выбрать файл для работы ")
            continue
        elif choice == '2':
            save_info_in_file(filename, contacts)
            is_info_saved = True
        elif choice == '3':
            show_all_contacts(contacts)
        elif choice == '4':
            contacts = add_contact(contacts)
            is_info_saved = False
        elif choice == '5':
            find_contact(contacts)
        elif choice == '6':
            edit_contact(contacts)
            is_info_saved = False
        elif choice == '7':
            contacts, status = delete_contact(contacts)
            if status == 1:
                is_info_saved = False


menu()
