#!/usr/bin/env python3

import json
import requests


cb_api_path = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(cb_api_path)
curr_dict = response.json()
print(curr_dict["Date"])


def get_value(currency):
    value = curr_dict["Valute"][currency]["Value"]
    return value


def get_nominal(currency):
    nominal = curr_dict["Valute"][currency]["Nominal"]
    return nominal


def get_name(currency):
    name = curr_dict["Valute"][currency]["Name"]
    return name


def get_help():
    curr_list = list() #создали пустой список, куда запишем все значения валют для тг
    for cur in sorted(curr_dict["Valute"].keys()): #по очереди в алф. порядке бращаемся ко всем валютам из json
        name = get_name(cur)
        curr_list.append(f'{cur}: {name}') #записываем в список, используя форматирование строк f'...'
    return "\n".join(curr_list) #возвращаем строку, кот явл объединением всех эл-тов списка


"""
cur = input().upper()

if cur == "HELP":
    help_mes = get_help()
    print(help_mes)
    exit()

val = get_value(cur)
nom = get_nominal(cur)
name = get_name(cur)

print(nom, name, "равняется", val, "российских рублей")
print("1 рубль равняется", nom / val, name)
"""
