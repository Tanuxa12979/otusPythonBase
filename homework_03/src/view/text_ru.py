
MENU = [
            'открыть файл',
            'сохранить файл',
            'показать все контакты',
            'добавить контакт',
            'найти контакт',
            'изменить контакт',
            'удалить контакт',
            'выход']

keys_dict = {1: 'name', 2: 'surname', 3: 'phone_number', 4: 'comment'}

MENU_IS_NOT_VALID = f'Выбранного вами пункта меню не существует. Необходимо выбрать один из пунктов 1 - {len(MENU)} '

FILE_PATH_CHOOSE = '''
Введите путь к файлу в след. формате D:/users/username/path/filename.json. 
Для выбора файла по умолчанию нажмите Enter.
Для возврата в главное меню нажмите 0
'''

FILE_NOT_FOUND_MSG = 'Файл по указанному вами пути не существует'

FILE_IS_NOT_JSON_MSG = 'Расширение файла не поддерживается. Выберите файл с расширением json'

FILE_IS_OPEN_ALREADY = 'Для открытия нового файла необходимо завершить работу с предыдущим! '

FILE_READ_PROBLEM = 'Произошла проблема при считывании данных из файла '

FILE_IS_NOT_OPEN = 'Сначала необходимо открыть файл '


def file_saved_info(filename):
    return f'Информация успешно сохранена в файл {filename}'

def successfully_chose_file(name: str) -> str:
    return f'Начинаем работу с файлом {name} '

ADD_CONTACT_FIELDS_ARE_EMPTY = 'Для добавления контакта необходимо заполнить все поля '

ADDED_CONTACT_SUCCESSFULLY = 'Контакт успешно добавлен в телефонную книгу'

SAVE_BEFORE_EXIT = 'Для сохранения изменений введите save, иначе данные не будут сохранены! '

SAVED_INFO_SUCCESSFULLY = 'Информация успешно сохранена в файл '

DELETE_ID_USER = 'Введите айди пользователя для удаления: '

CONTACT_ID_NOT_FOUNT = 'Пользователь с указанным айди не найден '

CONTACT_ID_IS_NOT_CORRECT = 'Введен некорректный айди '

def contact_deleted_successfully(id):
    return f'Контакт с айди {id} успешно удален. '

CONTACT_DELETED_SUCCESSFULLY = 'Контакт успешно'

FIND_CONTACT_TEXT = 'Введите строку для поиска '

CONTACT_NOT_FOUND = 'Контакт не был найден! '

CONTACTS_FOUND = 'Были найдены след. контакты: '

CONTACT_CHANGE_FIELDS = '''
Выберите для изменения одно из полей (введите номер поля):
1. Имя
2. Фамилия
3. Номер телефона
4. Комментарий
Для возврата в главное меню нажмите enter
'''

CONTACT_CHANGE_ID = 'Введите айди контакта для изменения: '

PRINT_NEW_VALUE = 'Введите новое значение для выбранного поля: '

FIELD_NOT_FOUND = 'Номер поля некорректный '

CONTACT_CHANGE_INCORRECT_ID = 'Айди контакта - целое число '

CONTACT_CHANGED_SUCCESSFULLY = 'Контакт был успешно изменен '



