"""Осуществляет обход gitlab определенных пользователей
    и рассматривает их members, issues и размеры их репозиториев"""
# pylint: disable-msg=invalid-name
import platform
import argparse
from src.parse_git import parse_git


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

    parse_git(token=args.token, road_to_file=args.input.name)
    print('Read data from gitlab using %s file completed' % args.input.name)


if __name__ == '__main__':
    main()
