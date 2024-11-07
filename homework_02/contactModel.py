import json
from typing import Union, Dict, List


class Contact:
    def __init__(self, id_contact: int, name:str , surname: str, phone_number:str , comment: str) -> None:
        self.id_contact = id_contact
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.comment = comment


class ContactList:
    def __init__(self, contacts: List[Dict[str, Union[int, str]]] = []) ->None:
        self.contacts = contacts

    def add_contact_to_contactlist(self, new_contact: Dict[str, Union[int, str]]):
        self.contacts.append(new_contact)


class FileWork:
    def __init__(self, path='contacts.json'):
        self.path = path

    def write_to_file(self, contacts):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(contacts, self.path)

    def read_from_file(self):
        with open(self.path, "r") as my_file:
            contacts_json = my_file.read()
        contacts = json.loads(contacts_json)
        return contacts["users"]