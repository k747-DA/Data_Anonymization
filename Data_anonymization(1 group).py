import PySimpleGUI as sg
import json
import datetime

def check_fio(str):
    answer = any(i.isdigit() for i in str)
    return answer

def check_date(str):
    try:
        valid_date = datetime.datetime.strptime(str, '%d.%m.%Y')
    except ValueError:
        return False
    return valid_date
def check_gender(str):
    if (any(i.isdigit() for i in str) or not (str in ['men', 'women', 'мужской', 'муж', 'женский', 'жен',
        'м','ж'])):
        return False
    return True

def check_materal(str):
    if not(str in ['замужем', 'женат', 'не женат', 'не замужем', 'нет']):
        return False
    return True
def check_child(str):
    if (str in ['да', 'нет', 'есть']):
        return True
    return False
def check_pass(str):
    try:
        pass_series, pass_num = str.split()
        if ((any(i.isdigit() for i in pass_series) and any(i.isdigit() for i in pass_num)) and len(pass_series) == 4 and len(pass_num) == 6):
            return True
        else:
            return False
    except ValueError:
        raise 'Ошибка'
def check_inn(str):
    if not(any(i.isdigit() for i in str) and len(str) != 10):
        return False
    return True
def check_phone(str):
    result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', str)
    return bool(result)
def check_email(str):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(pattern, str):
        return True
    else:
        return False
def check_birthPlace(str):
    try:
        birth_region, birth_city, birth_country = str.split("-")
        if not(any(i.isdigit() for i in birth_region) and any(i.isdigit() for i in birth_city) and any(i.isdigit() for i in birth_country)):
            return True
        else:
            return False
    except ValueError:
        raise 'Ошибка'
def check_livePlace(str):
    try:
        birth_region, birth_city, birth_country = str.split("-")
        if not (any(i.isdigit() for i in birth_region) and any(i.isdigit() for i in birth_city)):
            return True
        else:
            return False
    except ValueError:
        raise 'Ошибка'
try:
    with open('users.json', 'r', encoding='utf-8') as json_data:
        users = json.load(json_data)
except json.decoder.JSONDecodeError:
    users = {}
except (FileExistsError, OSError):
    with open('users.json', 'w', encoding='utf-8') as file:
        users = {}
        json.dump(users, file)

while True:
    print('Заполните следующие данные: ')

    while (True):
        last_name = input('Фамилия: ').title()
        if not check_fio(last_name):
            break
    while(True):
        first_name = input('Имя: ').title()
        if not check_fio(first_name):
            break
    while(True):
        patronymic = input('Отчество: ').title()
        if not check_fio(patronymic):
            break

    while(True):
        birth_date = input('Дата рождения (ДД.ММ.ГГГГ): ')
        if check_date(birth_date):
            break
    while(True):
        birth_place = input('Место рождения (Город-Регион-Страна): ')
        if check_birthPlace(birth_place):
            break
    while(True):
        live_place = input('Место фактического проживания (Регион — Город — Адрес): ')
        if(check_livePlace(live_place)):
            break
    while(True):
        gender = input('Пол (М/Ж): ')
        gender = gender.lower()
        if check_gender(gender):
            break
    while(True):
        marital_status = input('Семейное положение (Женат/Замужем): ')
        marital_status = marital_status.lower()
        if check_materal(marital_status):
            break
    while (True):
        child_info = input('Сведения о детях (Есть/Нет): ').lower()
        if check_child(child_info):
            break
    while(True):
        passport = input('Паспортные данные (Серия и №): ')
        if check_pass(passport):
            break
    while(True):
        inn_number = input('ИНН: ')
        if check_inn(inn_number):
            break
    while(True):
        phone = input('Номер телефона: ')
        if check_phone(phone):
            break
    while(True):
        email = input('E-mail (Почта): ')
        if check_email(email):
            break

    # city = input('Город: ')
    # address = input('Улица: ')
    # b_day, b_month, b_year = birth_date.split('.')
    #birth_city, birth_region, birth_country = birth_place.replace(',', ' ').split()
    #birth_place = ', '.join([birth_city, birth_region, birth_country])

    #live_region, live_city, live_address = live_place.split(', ')
    #live_place = ', '.join([live_region, live_city, live_address])

    #pass_series, pass_num = passport.replace(',', ' ').split()
    #passport = ' '.join([pass_series, pass_num])

    user = {
        'last_name': last_name,
        'first_name': first_name,
        'patronymic': patronymic,
        'birth_date': birth_date,
        'gender': gender,
        'marital_status': marital_status,
        'child_info': child_info,
        'passport_data': passport,
        'INN': inn_number,
        'birth_place': birth_place,
        #'address': live_place,
        'phone': [phone],
        'other_data': {
            'e-mail': [email]
        }

    }

    if 'users' not in users:
        users['users'] = []
    users['users'].append(user)

    users['count'] = len(users['users'])

    choice = input('Добавить ещё пользователя? (Да/Нет): ')
    if choice.lower() in ['нет', 'no', 'n']:
        break

with open('users.json', 'r+', encoding='utf-8') as file:
    json.dump(users, file, indent=4, ensure_ascii=False)
