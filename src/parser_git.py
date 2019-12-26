# pylint: disable=too-many-locals, too-many-branches, line-too-long
"""
Основной файл для работы с gitlab

Класс ParserGit использует несколько переменных класса для записи в них
необходимой для выполнения задачи информации.
Также имеются два метода: get_logs и parser_git

Сам скрипт можно написать в одну функцию, но это оказалось не практично,
как итог: работа с классами must have, т.к. работа с параметрами методов класса
дает обширную возможность для планировки кода.

P.s. Либо берем и разбиваем код на дерево функций, работающее друг с другом.
"""
import requests
from bs4 import BeautifulSoup
from .read_file import create_connect_file


PREPODS = ('anetto', 'FunnyWhale')  # example prepods


class ParserGit:
    """
    Класс, выполянющий:
    запись из файла ФИО и никнеймыов, записывает их в переменную logs.
    Совершает обход gitlab, работаю с переменными класса как с локальными параметрами
    """

    get_members = []
    get_issues = []
    get_url = []
    projects = []
    logs = {}

    @staticmethod
    def get_logs(road_to_file):
        """
        Осуществляет запись из файла в переменную logs
        в формате dict
        """
        ParserGit.logs = create_connect_file(road_to_file)
        return ParserGit.logs

    @staticmethod
    def parser_git(token):
        """ Функция, выполняющая обход gitlab
        Args:
            token: Пользователь вводит свой уникальный токен
        """
        parser = ParserGit()

        for log in parser.logs:
            log_user = requests.get("https://gitlab.com/api/v4/users?username=" + log)
            for i in log_user.json():
                id_user = i['id']

            project = requests.get('https://gitlab.com/api/v4/users/' + str(id_user)
                                   + '/projects?private_token=' + token)

            # Получение названий всех репозиториев
            for proj in project.json():
                parser.projects.append(proj['name'])

            # Получение всех members, привязанных к репозиториям
            for pro in project.json():
                parser.get_members.append(pro['_links']['members'])

            # Получение всех issues, привязанных к репозиториям
            for i in project.json():
                parser.get_issues.append(i['_links']['issues'])

            print('\x1b[1;4;35mСлушатель ' + str(parser.logs[log]) + ':\x1b[0m')
            to_projects = list(parser.projects)
            to_projects.reverse()
            for memb in parser.get_members:
                count_mem = 0
                mem = set()
                members = requests.get(memb + '?private_token=' + token)
                for i in members.json():
                    mem.add(i['username'])
                    count_mem += 1
                if count_mem == 0:
                    print(' -У слушателя \x1b[1;31mОТСУТСТВУЮТ\x1b[0m members в репозитории: \x1b[4m' +
                          str(to_projects.pop()) + '\x1b[0m')
                elif count_mem == 1:
                    print(' -У слушателя в members в репозитории \x1b[4m' + str(to_projects.pop()) +
                          '\x1b[0m \x1b[1;31mТОЛЬКО ПОЛЬЗОВАТЕЛЬ\x1b[0m: ' + str(mem))
                else:
                    total_mem = list(set(mem) - set(PREPODS))
                    if len(total_mem) > 1:
                        print(' -У слушателя в members в репозитории \x1b[4m' + str(to_projects.pop()) +
                              '\x1b[0m \x1b[1;31m ЕСТЬ ЛИШНИЕ ПОЛЬЗОВАТЕЛИ\x1b[0m: ' + str(total_mem))

            to_projects = list(parser.projects)
            to_projects.reverse()
            for i in parser.get_issues:
                count_is = 0
                issues = requests.get(i + '?private_token=' + token)
                for _ in issues.json():
                    count_is += 1
                if count_is > 0:  # Как пример вывода тех, у кого есть issues (вдруг достойны внимания)
                    print(' \x1b[0m-Количество issues в репозитории\x1b[0m \x1b[4m'
                          + str(to_projects.pop()) + '\x1b[0m: ' + str(count_is))

            to_projects = list(parser.projects)
            to_projects.reverse()
            for for_url in project.json():
                parser.get_url.append(for_url['web_url'])
            for for_url in parser.get_url:
                url = requests.get(for_url)
                soup = BeautifulSoup(url.text, 'html.parser')
                size = soup.find('div', {'class': 'nav-links quick-links'}).findAll('a')
                rep_size, rep_module = str(size[3].text).split(' ')[:2]
                if rep_module in ('Bytes', 'KB'):
                    pass
                elif rep_module == 'MB':
                    if float(rep_size) > 3:
                        print(' \x1b[1;31m-Размер репозитория \x1b[4m' + str(to_projects.pop()) +
                              '\x1b[1;31m больше 3 MB\x1b[0m: ' + rep_size + ' ' + rep_module)
                else:
                    print(' \x1b[1;31m-Размер репозитория \x1b[4m' + str(to_projects.pop()) +
                          '\x1b[1;31m больше 3 MB\x1b[0m: ' + rep_size + ' ' + rep_module)
            parser.projects.clear()
            parser.get_url.clear()
            parser.get_issues.clear()
            parser.get_members.clear()
