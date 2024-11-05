#print input

class WorkWithConsole:

    @staticmethod
    def choose_menu():
        choice = input('''
        ------------------------------
        Выберите действие:
        1 - открыть файл
        2 - сохранить файл
        3 - показать все контакты
        4 - добавить контакт
        5 - найти контакт
        6 - изменить контакт
        7 - удалить контакт
        8 - выход
        ''')
        return choice


print(WorkWithConsole.choose_menu())
