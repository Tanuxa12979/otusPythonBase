from typing import Optional

import view
import model
import text_ru

class Controller:
    def __init__(self):
        self.is_file_opened = False
        self.is_info_saved = True
        self.phonebook = model.PhoneBook()

    def open_file(self, file: model.FileWork) -> None:
        '''
        открытие файла и запись списка конактов в phonebook
        :param file: файловый объект
        :return: None
        '''
        if self.is_file_opened:
            view.print_msg(text_ru.FILE_IS_OPEN_ALREADY)
            return None
        while not self.is_file_opened:
            file_path = view.user_input(text_ru.FILE_PATH_CHOOSE)
            if file_path == '0':
                break
            file_check_res = self._file_check_and_add(file, file_path)
            try:
                contact_list = file.read_from_file()
            except:
                print(view.print_msg(text_ru.FILE_READ_PROBLEM))
                return None
            for contact in contact_list:
                self.phonebook.add_contact(contact)
            if file_check_res:
                self.is_file_opened = True

    def write_to_file(self, file: model.FileWork) -> None:
        '''
        Сохранение информации в файл
        :param file: файловый объект
        :return: None
        '''
        file.write_to_file({'users': [value for key, value in self.phonebook.contacts.items()]})
        self.is_info_saved = True
        view.print_msg(text_ru.file_saved_info(file.path))

    @staticmethod
    def _file_check_and_add(file: model.FileWork, user_path: str) -> bool:
        if user_path == '':
            view.print_msg(text_ru.successfully_chose_file(file.path))
            return True
        try:
            model.FileWork.check_chosen_file(user_path)
        except FileNotFoundError:
            view.print_msg(text_ru.FILE_NOT_FOUND_MSG)
            return False
        except model.FileIsNotJson:
            view.print_msg(text_ru.FILE_IS_NOT_JSON_MSG)
            return False
        else:
            file.path = user_path
            view.print_msg(text_ru.successfully_chose_file(file.path))
            return True

    def add_contact_to_phonebook(self):
        contact_fields = view.add_contact_ask_fields()
        try:
            new_contact = self.phonebook.add_contact(contact_fields)
        except model.ContactFieldsAreEmpty:
            view.print_msg(text_ru.ADD_CONTACT_FIELDS_ARE_EMPTY)
        else:
            view.print_msg(text_ru.ADDED_CONTACT_SUCCESSFULLY)
            view.print_phonebook(new_contact)
            return True

    def before_exit(self, file: model.FileWork) -> None:
        if not self.is_info_saved:
            save = view.user_input(text_ru.SAVE_BEFORE_EXIT)
            if save == 'save':
                self.write_to_file(file)

    def delete_contact(self) -> bool:
        id_contact = view.user_input(text_ru.DELETE_ID_USER)
        try:
            self.phonebook.delete_contact_by_id(int(id_contact))
        except model.IdNotFound:
            view.print_msg(text_ru.CONTACT_ID_NOT_FOUNT)
        except ValueError:
            view.print_msg(text_ru.CONTACT_ID_IS_NOT_CORRECT)
        else:
            view.print_msg(text_ru.contact_deleted_successfully(id_contact))
            return True

    def find_contact(self):
        text = view.user_input(text_ru.FIND_CONTACT_TEXT)
        found_contact_dict = self.phonebook.find_contact(text)
        if not found_contact_dict:
            view.print_msg(text_ru.CONTACT_NOT_FOUND)
        view.print_msg(text_ru.CONTACTS_FOUND)
        view.print_phonebook(found_contact_dict)



def _menu_validation(choice: str, len_menu: int) -> None:
    try:
        model.validate_user_input(choice, len_menu)
    except model.MenuIsNotValid:
        view.print_msg(text_ru.MENU_IS_NOT_VALID)


def start():
    """Основная функция работы с меню"""
    controller = Controller()
    file = model.FileWork()
    choice = '0'
    while choice != '8':
        view.print_menu()
        choice = view.user_input()
        _menu_validation(choice, len(text_ru.MENU))
        if choice == '1':
            controller.open_file(file)
        if not controller.is_file_opened and choice != '8':
            view.print_msg(text_ru.FILE_IS_NOT_OPEN)
        elif choice == '2':
            controller.write_to_file(file)
        elif choice == '3':
            view.print_phonebook(controller.phonebook.contacts)
        elif choice == '4':
            res = controller.add_contact_to_phonebook()
            if res:
                controller.is_info_saved = False
        elif choice == '5':
            controller.find_contact()
        elif choice == '6':
            pass
        elif choice == '7':
            res = controller.delete_contact()
            if res:
                controller.is_info_saved = False
        elif choice == '8':
            controller.before_exit(file)
