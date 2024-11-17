from contactView import WorkWithConsole
from contactModel import *

#todo вынести все сообщения и переменные с ними из контроллера
#todo исключения
#todo вынести по возможности логику по каждому пункту в отдельную внутреннюю функцию
#todo написать для функций аннотации
#todo сделать список констактов -т список объектов класса констант

CHOSE_FILE_MSG = '''
Введите имя файла (необходимо указать абсолютный путь в формате D:/users/username/path/filename.json).
Для выбора файла по умолчанию нажмите enter без ввода доп информации.
Для возврата в главное меню введите 0
'''

DEL_CONTACT_MSG = '''
Выберите действие:
1. Удалить контакт по его номеру (айди)
2. Выход в главное меню
'''



class ContactController:
    def __init__(self):
        self.is_file_opened = False
        self.is_info_saved = True

    def menu_checks(self, chosen_menu: str) -> bool:
        if not chosen_menu.isdecimal() or 0 >= int(chosen_menu) or int(chosen_menu) > 8:
            return False
        return True


def start():
    controller = ContactController()
    choice = '0'
    file = FileWork()
    contactlist = ContactList()
    while choice != '8':
        choice = WorkWithConsole.choose_menu()
        check_result = controller.menu_checks(choice)
        if check_result is False:
            WorkWithConsole.print_msg(f'Необходимо выбрать один из пунктов меню, попробуйте снова.')
            continue
        if choice == '1':
            if controller.is_file_opened:
                WorkWithConsole.print_msg(f"Для работы уже выбран файл {file.path}, сначала завершите с ним работу ")
                continue
            while not controller.is_file_opened:
                user_file = WorkWithConsole.ask_user(CHOSE_FILE_MSG)
                if user_file == '0':
                    break
                else:
                    msg = file.check_chosen_file(user_file)
                    if msg is None:
                        controller.is_file_opened = True
                    else:
                        WorkWithConsole.print_msg(msg)
                        continue
                WorkWithConsole.print_msg(f"\nНачинаем работу с файлом {file.path}\n")
                contactlist.contacts = file.read_from_file()
        if controller.is_file_opened is False:
            WorkWithConsole.print_msg("Сначала необходимо выбрать файл для работы ")
            continue
        if choice == '2':
            file.write_to_file({'users': contactlist.contacts})
            controller.is_info_saved = True
            WorkWithConsole.print_msg(f"Данные успешно сохранены в файл {file.path}")
        elif choice == '3':
            WorkWithConsole.show_contact_list(contactlist.contacts)
        elif choice == '4':
            id_contact = contactlist.max_id() + 1
            name = WorkWithConsole.ask_user("Введите имя нового контакта ")
            surname = WorkWithConsole.ask_user("Введите фамилию нового контакта ")
            phone_number = WorkWithConsole.ask_user("Введите номер телефона нового контакта ")
            comment = WorkWithConsole.ask_user("Введите комментарий для нового контакта ")
            contact = Contact(id_contact, name, surname, phone_number, comment)
            contactlist.add_contact_to_contactlist(contact.contact_dict())
            WorkWithConsole.print_msg(f"Контакт {name} {surname} успешно добавлен. ")
            WorkWithConsole.show_contact_list(contactlist.contacts)
            controller.is_info_saved = False
        elif choice == '5':
            str_for_search = WorkWithConsole.ask_user("Введите строку для поиска ")
            found_contacts = contactlist.find_contacts(str_for_search)
            WorkWithConsole.print_msg("\nБыли найдены след. констакты: ")
            for found_contact in found_contacts:
                WorkWithConsole.show_contact(found_contact)
        elif choice == '6':
            id_contact = WorkWithConsole.ask_user("Введите айди контакта для изменения ")
            
        elif choice == '7':
            delete_con = ''
            while delete_con != '1' or delete_con != '2':
                delete_con = WorkWithConsole.ask_user(DEL_CONTACT_MSG)
                if delete_con == '1':
                    id_contact = WorkWithConsole.ask_user("Введите номер (айди) контакта для удаления ")
                    if id_contact.isdecimal():
                        msg = contactlist.delete_contact_by_id(id_contact)
                        if msg is None:
                            WorkWithConsole.print_msg("Контакт успешно удален.")
                            WorkWithConsole.show_contact_list(contactlist.contacts)
                            controller.is_info_saved = False
                            break
                        else:
                            WorkWithConsole.print_msg(msg)
                    else:
                        WorkWithConsole.print_msg(
                            "Необходимо ввести корректный номер контакта (целое положительное число). Контакт не был удален")
                elif delete_con == '2':
                    break
                else:
                    WorkWithConsole.print_msg("Необходимо выбрать одно из предложенных ниже действий.")
        elif choice == '8':
            if controller.is_file_opened and not controller.is_info_saved:
                if WorkWithConsole.ask_user("Имеются несохраненные данные. Для сохранения введите save, иначе будет осуществлен выход без сохранения ") == 'save':
                    file.write_to_file({'users':contactlist.contacts})
                    WorkWithConsole.print_msg("Информация сохранена в файл.")
            WorkWithConsole.print_msg("Работа окончена. До свидания!")
            break

