#!/usr/bin/env python3

import json
import requests
from time import time


cb_api_path = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(cb_api_path)
curr_dict, ts = response.json(), time()


def update_cache():
    response = requests.get(cb_api_path)
    curr_dict = response.json()
    print("update_cache")
    return curr_dict, time()


def get_value(currency):
    global curr_dict, ts
    if time() - ts > 300:
        curr_dict, ts = update_cache()
    value = curr_dict["Valute"][currency]["Value"]
    return value


def get_nominal(currency):
    global curr_dict, ts
    if time() - ts > 300:
        curr_dict, ts = update_cache()
    nominal = curr_dict["Valute"][currency]["Nominal"]
    return nominal


def get_name(currency):
    global curr_dict, ts
    if time() - ts > 300:
        curr_dict, ts = update_cache()
    name = curr_dict["Valute"][currency]["Name"]
    return name


def get_date():
    global curr_dict, ts
    if time() - ts > 300:
        curr_dict, ts = update_cache()
    date = curr_dict["Date"]
    return date


def get_help():
    global curr_dict
    curr_list = list()
    for cur in sorted(curr_dict["Valute"].keys()):
        name = get_name(cur)
        curr_list.append(f'{cur}: {name}')
    return "\n".join(curr_list)


def get_currency_rate(currency):
    global curr_dict, ts
    if time() - ts > 300:
        curr_dict, ts = update_cache()

    if currency not in curr_dict["Valute"]:
        return "Указана неизвестная валюта"

    val = get_value(currency)
    nom = get_nominal(currency)
    name = get_name(currency)
    rub_curr = val / nom
    curr_rub = nom / val

    output = f"1 <b>{name}</b> равняется {rub_curr} <b>Российских рублей</b>\n"
    output += f"1 <b>Российский рубль</b> равняется {curr_rub} <b>{name}</b>"

    return output
