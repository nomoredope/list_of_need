import requests
from bs4 import BeautifulSoup
import json
import pandas
import re
import os
# from elevate import elevate


def domen_only(url: str):
    a = ''
    for i in range(len(url)):
        if url[i] != '/' and url[i] != '\\':
            if url[i] == '.':
                a += '~'
            else:
                a += url[i]
        else:
            break
    return a


def check_template(url: str):
    try:
        with open(f'C:\\Users\\schen\\PycharmProject\\pythonProject\\storage'
                  f'\\parse_templates\\{domen_only(url)}.json', 'r', encoding='utf-8') as openfile:
            return [True, json.load(openfile)]
    except Exception as ex:
        print(ex)
        return [False, ex]


def First_check(url: str):
    template = check_template(url)
    if template[0]:
        return template[1]
    else:
        return False



