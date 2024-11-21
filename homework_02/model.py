import json
import os
from collections import namedtuple


class MenuIsNotValid(Exception):
    pass


def validate_user_input(user_choice, len_menu):
    if not user_choice.isdecimal() or 0 >= int(user_choice) or int(user_choice) > len_menu:
        raise MenuIsNotValid


class FileIsNotJson(Exception):
    pass


class FileWork:
    def __init__(self, path='contacts.json'):
        self.path = path

    def write_to_file(self, contacts):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(json.dumps(contacts))

    def read_from_file(self):
        with open(self.path, "r") as my_file:
            contacts_json = my_file.read()
        contacts = json.loads(contacts_json)
        return contacts["users"]

    @staticmethod
    def check_chosen_file(chosen_file : str) -> bool:
        '''Проверка файла на существование '''
        if not os.path.isfile(chosen_file):
            raise FileNotFoundError
        else:
            if chosen_file[-5:] != '.json':
                raise FileIsNotJson


class ContactFieldsAreEmpty(Exception):
    pass


class IdNotFound(Exception):
    pass


class PhoneBook:

    def __init__(self, contacts: dict[int, dict[str, str]] = {}) ->dict[int, dict[str, str]]:
        self.contacts = contacts

    def add_contact(self, contact: dict[str, str]):
        if not all(list(map(lambda x: x != '', contact.values()))):
            raise ContactFieldsAreEmpty
        new_id = max(self.contacts.keys())+1 if self.contacts else 1
        self.contacts[new_id] = contact
        return {new_id: self.contacts[new_id]}

    def _is_id_in_dict(self, id_contact: int) -> bool:
        if int(id_contact) not in self.contacts.keys():
            raise IdNotFound
        return True

    def delete_contact_by_id(self, id_contact: int) -> None:
        if self._is_id_in_dict(id_contact):
            del self.contacts[id_contact]

    def find_contact(self, text: str) -> [dict[int, dict[str, str]]]:
        res = {}
        for key, value in self.contacts.items():
            for key1, value1 in value.items():
                if text in value1:
                    res[key] = value
                    break
        return res

