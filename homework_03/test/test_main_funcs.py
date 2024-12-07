import pytest
from homework_03.test.conftest import create_file_and_controller, create_and_delete_file


# тесты на открытие файла
def test_existing_file_check_and_add(create_file_and_controller, create_and_delete_file):
    file, controller = create_file_and_controller
    controller.file_check_and_add(file, '1.json')
    assert file.path == '1.json'


def test_default_file_check_and_add(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.file_check_and_add(file, '')
    assert file.path == '../data/contacts.json'


def test_not_existing_file_check_and_add(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.file_check_and_add(file, '1.json')
    assert controller.file_check_and_add(file, '1.json') is False


# тесты на сохранение информации
def test_save_info_into_file(create_file_and_controller, create_and_delete_file):
    contact_json = {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    file, controller = create_file_and_controller
    # добавление пользователя
    controller.phonebook.add_contact(contact_json)
    file.path = '1.json'
    # сохранение информации в файл
    file.write_to_file({'users': [value for key, value in controller.phonebook.contacts.items()]})
    # открытие файла и считывание информации
    contact = file.read_from_file()
    # сверка данных
    assert contact[0] == contact_json


#тесты на добавление контакта
def test_add_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {}
    contact_json = {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    result = controller.add_contact_to_phonebook(contact_json)
    assert result is True
    assert controller.phonebook.contacts[1] == contact_json


def test_add_empty_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {}
    contact_json = {"name": "", "surname": "", "phone_number": "", "comment": ""}
    result = controller.add_contact_to_phonebook(contact_json)
    assert result is False


#тесты на поиск контактов
def test_find_existing_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {
        1: {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"},
        2: {"name": "Kail", "surname": "Brook", "phone_number": "+79182223245", "comment": "Older sister"},
        3: {"name": "Nik", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    }
    res_list = controller.find_contact('Ka')
    assert res_list == {
        1: {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"},
        2: {"name": "Kail", "surname": "Brook", "phone_number": "+79182223245", "comment": "Older sister"}}


def test_find_not_existing_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {
        1: {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"},
        2: {"name": "Kail", "surname": "Brook", "phone_number": "+79182223245", "comment": "Older sister"},
        3: {"name": "Nik", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    }
    res = controller.find_contact('Ma')
    assert res is False


#тест на изменение контактов
@pytest.mark.parametrize(
    "user_id, field, new_value",
    [
        (1, "1", "Sonya"),
        (1, "2", "Popova"),
        (1, "3", "791823423423"),
        (1, "4", "The best friend")
    ]
)
def test_change_contact(user_id, field, new_value, create_file_and_controller):
    dict_fields = {"1": "name", "2": "surname", "3": "phone_number", "4": "comment"}
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {}
    contact_json = {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    controller.add_contact_to_phonebook(contact_json)
    controller.change_user(user_id, field, new_value)
    assert controller.phonebook.contacts[user_id][dict_fields[field]] == new_value


#тесты на удаление контактов
def test_delete_existing_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {}
    contact_json = {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    controller.add_contact_to_phonebook(contact_json)
    controller.delete_contact("1")
    assert controller.phonebook.contacts == {}


def test_delete_not_existing_contact(create_file_and_controller):
    file, controller = create_file_and_controller
    controller.phonebook.contacts = {}
    contact_json = {"name": "Kate", "surname": "Ten", "phone_number": "+79182223245", "comment": "Older sister"}
    controller.add_contact_to_phonebook(contact_json)
    res = controller.delete_contact("2")
    assert res is False
