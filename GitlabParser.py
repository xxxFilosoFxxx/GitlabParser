"""Осуществляет обход gitlab определенных пользователей
    и рассматривает их members, issues и размеры их репозиториев"""
# pylint: disable-msg=invalid-name
import platform
import argparse
from src.parser_git import ParserGit


if platform.system() == 'Windows':
    import ctypes
    KERNEL32 = ctypes.windll.kernel32
    KERNEL32.SetConsoleMode(KERNEL32.GetStdHandle(-11), 7)


def create_pars():
    """Создание аргументов командной строки"""
    parser = argparse.ArgumentParser(
        prog='GitlabParser',
        description='Displays incorrect gitlab users data (input .txt file)',
        epilog='(c) xxxFilosoFxxx 2019',
    )
    parser.add_argument(
        '-i', '--input',
        help='input .txt file',
        type=argparse.FileType(),
        required=True
    )
    parser.add_argument(
        '-t', '--token',
        help='input private_token',
        type=str,
        required=True
    )
    return parser


def main():
    """Передача аргументов командной строки исполняемой функции"""
    parser = create_pars()
    args = parser.parse_args()

    ParserGit.get_logs(road_to_file=args.input.name)
    ParserGit.parser_git(token=args.token)
    print('Чтение данных из gitlab с использованием файла %s завершено' % args.input.name)


if __name__ == '__main__':
    main()
