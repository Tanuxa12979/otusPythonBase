from contactView import WorkWithConsole
from contactModel import *


class ContactController:
    def __init__(self):
        self.is_file_opened = False
        self.is_info_saved = True

    def menu_checks(self, chosen_menu: str) -> bool:
        if not chosen_menu.isdecimal() or 0 >= int(chosen_menu)  or int(chosen_menu) > 8:
            return False
        return True

def main():
    controller = ContactController()
    choice = '0'
    while choice != '8':
        choice = WorkWithConsole.choose_menu()
        check_result = controller.menu_checks(choice)
        if check_result is False:
            WorkWithConsole.print_err(f'Необходимо выбрать один из пунктов меню, попробуйте снова.')

