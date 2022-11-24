#!/usr/bin/env python3

import json
import requests


cb_api_path = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(cb_api_path)
curr_dict = response.json()


def get_value(currency):
    value = curr_dict["Valute"][currency]["Value"]
    return value


def get_nominal(currency):
    nominal = curr_dict["Valute"][currency]["Nominal"]
    return nominal


def get_name(currency):
    name = curr_dict["Valute"][currency]["Name"]
    return name


def get_date():
    date = curr_dict["Date"]
    return date


def get_help():
    curr_list = list()
    for cur in sorted(curr_dict["Valute"].keys()):
        name = get_name(cur)
        curr_list.append(f'{cur}: {name}')
    return "\n".join(curr_list)


def get_currency_rate(currency):    
    if currency not in curr_dict["Valute"]:
        return "Указана неизвестная валюта"

    val = get_value(currency)
    nom = get_nominal(currency)
    name = get_name(currency)
    rub_curr = val / nom
    curr_rub = nom / val

    output = f"1 <b>{name}</b> равняется {curr_rub} <b>Российских рублей</b>\n"
    output += f"1 <b>Российский рубль</b> равняется {rub_curr} <b>{name}</b>"

    return output


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
