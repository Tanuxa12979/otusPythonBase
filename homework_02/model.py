import json
import os


class FileIsNotJson(Exception):
    pass


class ContactFieldsAreEmpty(Exception):
    pass


class IdNotFound(Exception):
    pass


class FileWork:
    def __init__(self, path='data/contacts.json'):
        self.path = path

    def write_to_file(self, contacts: dict[str, list[dict[str, str]]]) -> None:
        """
        Запись данных в файл
        :param contacts: словарь: ключ users значение - список словарей контактов
        :return: none
        """
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(json.dumps(contacts))

    def read_from_file(self) -> list[dict[str, str]]:
        """
        Чтение данных из файла и их возврат в виде списка словарей
        :return: список словарей контактов
        """
        with open(self.path, "r") as my_file:
            contacts_json = my_file.read()
        contacts = json.loads(contacts_json)
        return contacts["users"]

    @staticmethod
    def check_chosen_file(chosen_file: str) -> None:
        """
        Проверка файла на существование и корректность формата
        :param chosen_file: путь к фаайлу
        :return: none
        """
        if not os.path.isfile(chosen_file):
            raise FileNotFoundError
        else:
            if chosen_file[-5:] != '.json':
                raise FileIsNotJson


class PhoneBook:

    def __init__(self, contacts: dict[int, dict[str, str]] = {}) -> dict[int, dict[str, str]]:
        self.contacts = contacts

    def add_contact(self, contact: dict[str, str]) -> dict[int, dict[str, str]]:
        """
        Добавление нового контакта записную книгу
        :param contact: словарь с ключами и значениями для добавления нового контакта
        :return: словарь словарей, где ключ - айди нового контакта, словарь с информацией по контакту
        """
        if not all(list(map(lambda x: x != '', contact.values()))):
            raise ContactFieldsAreEmpty
        new_id = max(self.contacts.keys())+1 if self.contacts else 1
        self.contacts[new_id] = contact
        return {new_id: self.contacts[new_id]}

    def _is_id_in_dict(self, id_contact: int) -> bool:
        """
        Проверка наличия айди в списке контактов
        :param id_contact: айди для поиска
        :return: true если находится, исключение иначе
        """
        if int(id_contact) not in self.contacts.keys():
            raise IdNotFound
        return True

    def delete_contact_by_id(self, id_contact: int) -> None:
        """
        Удаление контакта из телефонной книги по айди
        :param id_contact: айди контакта для удаления
        :return: none
        """
        if self._is_id_in_dict(id_contact):
            del self.contacts[id_contact]

    def find_contact(self, text: str) -> [dict[int, dict[str, str]]]:
        """
        Поиск контактов, в значениях полей которых есть вхождение выбранной строки
        :param text: строка для поиска
        :return: список найденных контактов (список словарей, где словарь - ключи значения отдельного контакта)
        """
        res = {}
        for key, value in self.contacts.items():
            for key1, value1 in value.items():
                if text in value1:
                    res[key] = value
                    break
        return res

    def change_contact(self, contact_id: int,  field_key: str, field_value: str) -> None:
        """
        Изменение контакта по айди
        :param contact_id: айди контакта для изменения
        :param field_key: ключ изменяемого поля
        :param field_value: новое значение
        :return:
        """
        if not self._is_id_in_dict(contact_id):
            raise IdNotFound
        self.contacts[contact_id][field_key] = field_value

