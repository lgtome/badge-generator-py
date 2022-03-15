import re
import sys
from constants import front_arg_regex, post_arg_regex
from services.docker_parse_vars import docker_parse_variables


class BadgeGenerator:
    args_list = {"": ""}
    is_continued = False
    is_download_needed = False

    def __init__(self):
        self.args = sys.argv.copy()
        self.args.pop(0)
        for arg in self.args:
            try:
                left = re.search(front_arg_regex, arg).group()
                if left == '-n':
                    self.is_continued = True

                if arg == '-d':
                    self.is_download_needed = True
            except:
                print('...')
        if not self.is_continued and not docker_parse_variables():
            exit('Arg -n-- not provided!')

    def __parseArgs(self):
        if not self.args:
            return docker_parse_variables()

        for arg in self.args:
            try:
                left = re.search(front_arg_regex, arg).group()
                right = re.search(post_arg_regex, arg).group().strip('-')
                self.args_list.update({left: right})
            except:
                print(f'Arg \x1b[6;30;42m {arg} \x1b[0m not fully provided!')

        for i in self.args_list.keys():
            if current := i == '-n':
                name = self.args_list[i]
            if current := i == '-bC':
                bgColor = self.args_list[i]
                self.args_list.update({i: bgColor})
            elif (not self.args_list.get('-bC')):
                bgColor = 'white'
            if current := i == '-l':
                logo = self.args_list[i]
                self.args_list.update({i: logo})
            elif (not self.args_list.get('-l')):
                logo = 'spotify'
            if current := i == '-lC':
                logoColor = self.args_list[i]
                self.args_list.update({i: logoColor})
            elif (not self.args_list.get('-lC')):
                logoColor = 'white'
        return [name, logo, bgColor, logoColor]

    def __makeUrl(self):
        name, logoName, bgColor, logoColor = self.__parseArgs()
        url = f'https://img.shields.io/badge/{name}-{bgColor}.svg?&style=for-the-badge&logo={logoName}&logoColor={logoColor}'
        print(f'Your URL ✨ {url}')
        return url

    def init(self):
        return [self.__makeUrl(), self.is_download_needed]
