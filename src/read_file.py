# pylint: disable=missing-docstring
import sys


def create_connect_file(road_to_file):
    """ Функция, открывающая файл с типом:
    fio;name;username
    ...
    Args:
        road_to_file: Пользователь вводит путь до файла
    Returns:
        logins_and_fullname: Возвращает словарь из ФИО и логинов.
    Raises:
        IndexError: Файл другого формата.
        FileNotFoundError: Не получилось найти нужный файл в системе
    """

    try:
        to_logins = []
        to_fullname = []
        with open(road_to_file, encoding='utf-8') as file:
            for line in file:
                to_fullname.append(line.split(';')[0])
                to_logins.append(line.split(';')[2])
        to_logins = [log.rstrip() for log in to_logins]
        logins_and_fullname = dict(zip(to_logins, to_fullname))
    except IndexError:
        sys.exit('Формат входного файла не подходит для исполнения скрипта')
    except FileNotFoundError:
        sys.exit('Входной файл не найден в системе')
    return logins_and_fullname
