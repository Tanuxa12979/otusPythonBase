from typing import Dict, Union, List


class WorkWithConsole:

    @staticmethod
    def print_menu_list():
        menu_list = [
            'открыть файл',
            'сохранить файл',
            'показать все контакты',
            'добавить контакт',
            'найти контакт',
            'изменить контакт',
            'удалить контакт',
            'выход']
        print('\n', "-"*50, sep='\n')
        print("Выберите действие: ")
        for i, item in enumerate(menu_list):
            print(f'{i + 1}. {item} ')

    @staticmethod
    def choose_menu():
        WorkWithConsole.print_menu_list()
        return input("\nВведите значение:  ")

    @staticmethod
    def print_msg(msg):
        print(msg)


    @staticmethod
    def ask_user(msg):
        return input(msg)


    @staticmethod
    def show_contact(contact: Dict[str, Union[str, int]]) -> None:
        '''
            Вывод данных о контакте в консоль

            :param contact: словарь с данными о контакте
            :returns: None
        '''
        print('Контакт: ', contact['id'], end='\n')
        print('Имя: ', contact['name'])
        print('Фамилия: ', contact['surname'])
        print('Номер телефона: ', contact['phone_number'])
        print('Комментарий: ', contact['comment'], end='\n\n')

    @staticmethod
    def show_contact_list(contacts: List[Dict[str, Union[str, int]]]) -> None:
        '''
            Вывод списка контактов в консоль

            :param contacts: первоначальный словарь с контактами
            :returns: None
        '''
        print('\n', '*' * 30, '', sep = '\n')
        for contact in contacts:
            WorkWithConsole.show_contact(contact)
        print("Конец записной книжки\n")


