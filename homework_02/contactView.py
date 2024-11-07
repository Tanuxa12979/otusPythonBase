#print input

class WorkWithConsole:

    @staticmethod
    def print_menu_list():
        options = [
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
        for i in range(1, len(options)+1):
            print(f'{i}. {options[i-1]} ')

    @staticmethod
    def choose_menu():
        WorkWithConsole.print_menu_list()
        return input("\nВведите значение:  ")

    @staticmethod
    def print_err(msg):
        print(msg)


