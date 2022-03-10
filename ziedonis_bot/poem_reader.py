from .constants import POEMS_FILE_PATH, POEM_SEPARATOR


def get_poems_all():
    
    with open(POEMS_FILE_PATH, 'r', encoding='utf-8') as poems_file:
        
        poems_all = poems_file.read()
        return poems_all


def get_poems_list():

    poems_all = get_poems_all()
    poems_list = poems_all.split(POEM_SEPARATOR)

    return poems_list


def remove_new_lines_and_spaces(string):

    import re

    string = string.replace('\n', ' ')
    string = re.sub(' +', ' ', string)

    return string