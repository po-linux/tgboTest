#!/usr/bin/env python3
# fd - file descriptor (переменная(объект), которая позволяет работать с указанным файлом)

import json 


file_name = "/Users/polina/tgboTest/currency_api_bot/cbr_daily.json"
fd = open(file_name) 
currency_json = fd.read() 
fd.close()

cur_dict = json.loads(currency_json) #парсим (преобразовываем) json в структуру данных, с кот. можно работать
print(cur_dict["Date"])


def get_value(currency):
    value = cur_dict["Valute"][currency]["Value"] 
    return value

def get_nominal(currency):
    nominal = cur_dict["Valute"][currency]["Nominal"] 
    return nominal

def get_name(currency):
    name = cur_dict["Valute"][currency]["Name"] 
    return name

def get_help():
    cur_list = list() #создали пустой список, куда запишем все значения валют для тг 
    for cur in sorted(cur_dict["Valute"].keys()): #по очереди в алф. порядке бращаемся ко всем валютам из json
        name = get_name(cur)
        cur_list.append(f'{cur}: {name}') #записываем в список, используя форматирование строк f'...'
    return "\n".join(cur_list) #возвращаем строку, кот явл объединением всех эл-тов списка 
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