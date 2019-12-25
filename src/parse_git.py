import sys
import requests
from bs4 import BeautifulSoup
from src.read_file import create_connect_file


PREPODS = ('anetto', 'FunnyWhale')  # example prepods


def parse_git(token, road_to_file):
    """ Функция, выполняющая обход gitlab
    Args:
        token: Пользователь вводит свой уникальный токен
        road_to_file: Пользователь вводит путь до файла
    """
    logs = create_connect_file(road_to_file)
    user = requests.get('https://gitlab.com/api/v4/user?private_token=' + token)
    if 'message' in user.json():
        sys.exit('Введен неверный приватный ключ!')
    for log in logs:
        get_members = []
        get_issues = []
        get_url = []
        projects = []

        print('\x1b[1;4;35mСлушатель ' + str(logs[log]) + ':\x1b[0m')
        log_user = requests.get("https://gitlab.com/api/v4/users?username=" + log)
        for i in log_user.json():
            id_user = i['id']

        project = requests.get('https://gitlab.com/api/v4/users/' + str(id_user)
                               + '/projects?private_token=' + token)

        # Получение названий всех репозиториев
        for proj in project.json():
            projects.append(proj['name'])

        # Получение всех members, привязанных к репозиториям
        for pro in project.json():
            get_members.append(pro['_links']['members'])

        # Получение всех issues, привязанных к репозиториям
        for i in project.json():
            get_issues.append(i['_links']['issues'])

        to_projects = list(projects)
        to_projects.reverse()
        for memb in get_members:
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

        to_projects = list(projects)
        to_projects.reverse()
        for i in get_issues:
            count_is = 0
            issues = requests.get(i + '?private_token=' + token)
            for _ in issues.json():
                count_is += 1
            if count_is > 0:  # Как пример вывода тех, у кого есть issues (вдруг достойны внимания)
                print(' \x1b[0m-Количество issues в репозитории\x1b[0m \x1b[4m'
                      + str(to_projects.pop()) + '\x1b[0m: ' + str(count_is))

        to_projects = list(projects)
        to_projects.reverse()
        for for_url in project.json():
            get_url.append(for_url['web_url'])
        for for_url in get_url:
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