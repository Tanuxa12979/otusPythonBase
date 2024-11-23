from typing import Optional

import view
import model
import text_ru


class FieldNotFound(Exception):
    pass

class MenuIsNotValid(Exception):
    pass


class Controller:
    def __init__(self):
        self.is_file_opened = False
        self.is_info_saved = True
        self.phonebook = model.PhoneBook()

    def open_file(self, file: model.FileWork) -> None:
        """
        открытие файла и запись списка конактов в phonebook
        :param file: файловый объект
        :return: None
        """
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
        """
        Сохранение информации в файл
        :param file: файловый объект
        :return: None
        """
        file.write_to_file({'users': [value for key, value in self.phonebook.contacts.items()]})
        self.is_info_saved = True
        view.print_msg(text_ru.file_saved_info(file.path))

    @staticmethod
    def _file_check_and_add(file: model.FileWork, user_path: str) -> bool:
        """
        Проверка существования файла и его открытие
        :param file: файловый объект
        :param user_path: путь к к файлу
        :return: true в случае успешного открытия, false иначе
        """
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

    def add_contact_to_phonebook(self) -> bool:
        """
        выбор константа для добавления
        :return: true в случае успешного добавления контакта
        """
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
        """
        запрос на сохранение перед завершением работы программы при наличии несохраненных данных
        :param file: файловый объект
        :return: none
        """
        if not self.is_info_saved:
            save = view.user_input(text_ru.SAVE_BEFORE_EXIT)
            if save == 'save':
                self.write_to_file(file)

    def delete_contact(self) -> bool:
        """
        Удаление константа
        :return: true в случае успешного удаления
        """
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

    def find_contact(self) -> None:
        """
        Поиск и удаление контакта при его наличии
        :return:
        """
        text = view.user_input(text_ru.FIND_CONTACT_TEXT)
        found_contact_dict = self.phonebook.find_contact(text)
        if not found_contact_dict:
            view.print_msg(text_ru.CONTACT_NOT_FOUND)
        view.print_msg(text_ru.CONTACTS_FOUND)
        view.print_phonebook(found_contact_dict)

    def change_user(self) -> bool:
        """
        Изменение пользователя
        :return: true в случае успешного изменения, иначе None
        """
        try:
            id_to_delete = int(view.user_input(text_ru.CONTACT_CHANGE_ID))
            view.print_phonebook({id_to_delete: self.phonebook.contacts[id_to_delete]})
            field = view.user_input(text_ru.CONTACT_CHANGE_FIELDS)
            if not field:
                return None
            elif field not in ('1', '2', '3', '4'):
                raise FieldNotFound
            new_value = view.user_input(text_ru.PRINT_NEW_VALUE)
            field_key = text_ru.keys_dict[int(field)]
            self.phonebook.change_contact(id_to_delete, field_key, new_value)
        except ValueError:
            view.print_msg(text_ru.CONTACT_CHANGE_INCORRECT_ID)
        except (KeyError, model.IdNotFound):
            view.print_msg(text_ru.CONTACT_NOT_FOUND)
        except FieldNotFound:
            view.print_msg(text_ru.FIELD_NOT_FOUND)
        else:
            view.print_msg(text_ru.CONTACT_CHANGED_SUCCESSFULLY)
            view.print_phonebook({id_to_delete: self.phonebook.contacts[id_to_delete]})
            return True


def _menu_validation(choice: str, len_menu: int) -> None:
    """
    Проверка выбранного пользователем пункта меню
    :param choice: выбранный пользователем пунтк меню
    :param len_menu: количество пунктов в меню
    :return: none
    """
    try:
        if not choice.isdecimal() or 0 >= int(choice) or int(choice) > len_menu:
            raise MenuIsNotValid
    except MenuIsNotValid:
        view.print_msg(text_ru.MENU_IS_NOT_VALID)


def start():
    """
    Основная функция работы с меню
    """
    controller = Controller()
    file = model.FileWork()
    choice = '0'
    while choice != '8':
        view.print_menu()
        choice = view.user_input()
        _menu_validation(choice, len(text_ru.MENU))
        if choice == '1':
            controller.open_file(file)
        if not controller.is_file_opened and choice in (str(i) for i in range(1, 7)):
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
            if controller.change_user():
                controller.is_info_saved = False
        elif choice == '7':
            res = controller.delete_contact()
            if res:
                controller.is_info_saved = False
        elif choice == '8':
            controller.before_exit(file)
