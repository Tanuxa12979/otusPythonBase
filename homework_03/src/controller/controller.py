from typing import Optional, Union

from homework_03.view import view
from homework_03.view import text_ru
import logging
from homework_03.model import FileWork
from homework_03.model import PhoneBook


class FieldNotFound(Exception):
    pass


class MenuIsNotValid(Exception):
    pass


class Controller:
    def __init__(self):
        self.is_file_opened = False
        self.is_info_saved = True
        self.phonebook = PhoneBook.PhoneBook()
        # Добавление логирования
        self.logger2 = logging.getLogger(__name__)
        self.logger2.setLevel(logging.INFO)
        # настройка обработчика и форматировщика для logger2
        handler2 = logging.FileHandler(f"logs/{__name__}.log", mode='w')
        formatter2 = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        # добавление форматировщика к обработчику
        handler2.setFormatter(formatter2)
        # добавление обработчика к логгеру
        self.logger2.addHandler(handler2)

    def open_file(self, file: FileWork.FileWork) -> None:
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
            file_check_res = self.file_check_and_add(file, file_path)
            try:
                if file_check_res:
                    contact_list = file.read_from_file()
            except Exception as e:
                print(view.print_msg(text_ru.FILE_READ_PROBLEM))
                self.logger2.exception(f"Error while reading data: {e}")
                return None
            if file_check_res:
                for contact in contact_list:
                    self.phonebook.add_contact(contact)
                self.is_file_opened = True
                self.logger2.info(f"File {file.path} was open. Contacts data was read successfully")

    def write_to_file(self, file: FileWork.FileWork) -> None:
        """
        Сохранение информации в файл
        :param file: файловый объект
        :return: None
        """
        file.write_to_file({'users': [value for key, value in self.phonebook.contacts.items()]})
        self.logger2.info("Information was saved successfully to file %s", file.path)
        self.is_info_saved = True
        view.print_msg(text_ru.file_saved_info(file.path))

    def file_check_and_add(self, file: FileWork.FileWork, user_path: str) -> bool:
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
            FileWork.FileWork.check_chosen_file(user_path)
        except FileNotFoundError:
            view.print_msg(text_ru.FILE_NOT_FOUND_MSG)
            self.logger2.error(f"File %s wasn't found", user_path)
            return False
        except FileWork.FileIsNotJson:
            view.print_msg(text_ru.FILE_IS_NOT_JSON_MSG)
            self.logger2.error("Format of chosen file isn't json")
            return False
        else:
            file.path = user_path
            view.print_msg(text_ru.successfully_chose_file(file.path))
            self.logger2.info("File %s was successfully opened", user_path)
            return True

    def add_contact_to_phonebook(self, contact_fields: dict[str: str]) -> bool:
        """
        выбор константа для добавления
        :return: true в случае успешного добавления контакта
        """
        try:
            new_contact = self.phonebook.add_contact(contact_fields)
        except PhoneBook.ContactFieldsAreEmpty:
            view.print_msg(text_ru.ADD_CONTACT_FIELDS_ARE_EMPTY)
            self.logger2.exception("Trying to add contact with empty fields")
            return False
        else:
            view.print_msg(text_ru.ADDED_CONTACT_SUCCESSFULLY)
            view.print_phonebook(new_contact)
            self.logger2.info("User %s was added successfully", new_contact)
            return True

    def before_exit(self, file: FileWork.FileWork) -> None:
        """
        запрос на сохранение перед завершением работы программы при наличии несохраненных данных
        :param file: файловый объект
        :return: none
        """
        if not self.is_info_saved:
            save = view.user_input(text_ru.SAVE_BEFORE_EXIT)
            if save == 'save':
                self.write_to_file(file)

    def delete_contact(self, id_contact: str) -> bool:
        """
        Удаление константа
        :return: true в случае успешного удаления
        """
        try:
            self.phonebook.delete_contact_by_id(int(id_contact))
        except PhoneBook.IdNotFound:
            view.print_msg(text_ru.CONTACT_ID_NOT_FOUNT)
            self.logger2.exception("Contact to delete doesn't exist")
            return False
        except ValueError:
            view.print_msg(text_ru.CONTACT_ID_IS_NOT_CORRECT)
            self.logger2.exception("Contact with id %s doesn't exist", id_contact)
            return False
        else:
            view.print_msg(text_ru.contact_deleted_successfully(id_contact))
            self.logger2.info("Contact with id %s was deleted successfully", id_contact)
            return True

    def find_contact(self, text: str) -> Union[bool, dict[int, dict[str, str]]]:
        """
        Поиск и удаление контакта при его наличии
        :return:
        """
        found_contact_dict = self.phonebook.find_contact(text)
        if not found_contact_dict:
            view.print_msg(text_ru.CONTACT_NOT_FOUND)
            return False
        view.print_msg(text_ru.CONTACTS_FOUND)
        view.print_phonebook(found_contact_dict)
        return found_contact_dict

    def change_user(self, user_id: str, field: str, new_value: str) -> bool:
        """
        Изменение пользователя
        :return: true в случае успешного изменения, иначе None
        """
        try:
            id_to_delete = int(user_id)
            view.print_phonebook({id_to_delete: self.phonebook.contacts[id_to_delete]})
            if not field:
                return None
            elif field not in ('1', '2', '3', '4'):
                raise FieldNotFound
            field_key = text_ru.keys_dict[int(field)]
            self.phonebook.change_contact(id_to_delete, field_key, new_value)
        except ValueError:
            view.print_msg(text_ru.CONTACT_CHANGE_INCORRECT_ID)
            self.logger2.exception("Contact with id %s wasn't found", user_id)
            return False
        except (KeyError, PhoneBook.IdNotFound):
            view.print_msg(text_ru.CONTACT_NOT_FOUND)
            self.logger2.exception("Contact with id %s wasn't found", id_to_delete)
            return False
        except FieldNotFound:
            view.print_msg(text_ru.FIELD_NOT_FOUND)
            self.logger2.exception("Trying to change field %s that doesn't exist", field)
            return False
        else:
            view.print_msg(text_ru.CONTACT_CHANGED_SUCCESSFULLY)
            view.print_phonebook({id_to_delete: self.phonebook.contacts[id_to_delete]})
            self.logger2.info("Contact with id %s was changed successfully", id_to_delete)
            return True

    def menu_validation(self, choice: str, len_menu: int) -> None:
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
            self.logger2.exception("There is no menu item %s", choice)


def start():
    """
    Основная функция работы с меню
    """
    controller = Controller()
    file = FileWork.FileWork()
    choice = '0'
    while choice != '8':
        view.print_menu()
        choice = view.user_input()
        controller.menu_validation(choice, len(text_ru.MENU))
        if choice == '1':
            controller.open_file(file)
        if not controller.is_file_opened and choice in (str(i) for i in range(1, 7)):
            view.print_msg(text_ru.FILE_IS_NOT_OPEN)
        elif choice == '2':
            controller.write_to_file(file)
        elif choice == '3':
            view.print_phonebook(controller.phonebook.contacts)
        elif choice == '4':
            contact_fields = view.add_contact_ask_fields()
            res = controller.add_contact_to_phonebook(contact_fields)
            if res:
                controller.is_info_saved = False
        elif choice == '5':
            text = view.user_input(text_ru.FIND_CONTACT_TEXT)
            controller.find_contact(text)
        elif choice == '6':
            user_id = view.user_input(text_ru.CONTACT_CHANGE_ID)
            field = view.user_input(text_ru.CONTACT_CHANGE_FIELDS)
            new_value = view.user_input(text_ru.PRINT_NEW_VALUE)
            if controller.change_user(user_id, field, new_value):
                controller.is_info_saved = False
        elif choice == '7':
            id_contact = view.user_input(text_ru.DELETE_ID_USER)
            res = controller.delete_contact(id_contact)
            if res:
                controller.is_info_saved = False
        elif choice == '8':
            controller.before_exit(file)
