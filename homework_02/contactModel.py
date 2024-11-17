import json
import os.path
from typing import Union, Dict, List


class Contact:

    def __init__(self, id_contact: int, name: str, surname: str, phone_number: str, comment: str) -> None:
        self.id_contact = id_contact
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.comment = comment

    def contact_dict(self):
        return {'id':self.id_contact, 'name': self.name, 'surname': self.surname, 'phone_number': self.phone_number, 'comment': self.comment}



class ContactList:
    def __init__(self, contacts: List[Dict[str, Union[int, str]]] = []) -> None:
        self.contacts = contacts

    def add_contact_to_contactlist(self, new_contact: Dict[str, Union[int, str]]):
        self.contacts.append(new_contact)

    def find_contacts(self, str_for_search):
        contact_list = []
        for contact in self.contacts:
            if (str_for_search in str(contact['id'])) or (str_for_search in contact['name']) or (
                    str_for_search in contact['surname']) or (str_for_search in contact['phone_number']) or (
                    str_for_search in contact['comment']):
                contact_list.append(contact)
        return contact_list



    def delete_contact_by_id(self, id_contact):
        is_contact_in_list = False
        contact_index = 0
        for contact in self.contacts:
            if contact['id'] == int(id_contact) and not is_contact_in_list:
                is_contact_in_list = True
                break
            contact_index += 1
        if not is_contact_in_list:
            return "Введенный контакт отсутствует в списке "
        else:
            self.contacts.pop(contact_index)

    def max_id(self):
        res = 0
        for contact in self.contacts:
            if contact['id'] > res:
                res = contact['id']
        return res

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

    def check_chosen_file(self, chosen_file):
        if chosen_file != '':
            if chosen_file.count('\\') > 0:
                return "Имя файла должно быть указано в след. формате D:/users/username/path/filename.json. Обратите внимание на направление слеша"
            elif chosen_file[-5:] != '.json':
                return "\nВыберите файл с расширением json"
            elif not os.path.isfile(chosen_file):
                return "Такой файл не существует, попробуйте снова"
            self.path = chosen_file

