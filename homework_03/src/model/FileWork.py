import json
import os


class FileIsNotJson(Exception):
    pass


class FileWork:
    def __init__(self, path='../data/contacts.json'):
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
