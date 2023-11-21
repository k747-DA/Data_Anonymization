from cryptography.fernet import Fernet
import pandas as pd
import json

# Генерация ключа
def generate_key():
    return Fernet.generate_key()

# Загрузка ключа
def load_key():
    try:
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Ключ шифрования не найден. Генерируем новый ключ...")
        key = generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
        return key

# Функция для обезличивания данных
def anonymize_data(data, columns):
    key = load_key()
    f = Fernet(key)
    for column in columns:
        if column in data:
            data[column] = f.encrypt(str(data[column]).encode()).decode()
    return data

# Функция для расшифровки данных
def decrypt_data(data, columns):
    key = load_key()
    f = Fernet(key)
    for column in columns:
        if column in data:
            data[column] = f.decrypt(data[column].encode()).decode()
    return data

# Получение данных из файла
with open('users.json', 'r', encoding='utf-8') as json_data:
    users = json.load(json_data)

# Обезличивание данных
anonymized_users = [anonymize_data(user, ['last_name', 'birth_date', 'address', 'passport_data', 'phone', 'other_data']) for user in users['users']]
with open('anonymized_users.json', 'w', encoding='utf-8') as file:
    json.dump(anonymized_users, file, indent=4, ensure_ascii=False)

# Получение обезличенных данных из файла
with open('anonymized_users.json', 'r', encoding='utf-8') as json_data:
    anonymized_users = json.load(json_data)

#запись в эксель файл засшифрованных данных
dec=pd.DataFrame(anonymized_users).to_excel("anon.xlsx")

# Расшифровка данных
decrypted_users = [decrypt_data(user, ['last_name', 'birth_date', 'address', 'passport_data', 'phone', 'other_data']) for user in anonymized_users]

# Запись в файл JSON
with open('decrypted_users.json', 'w', encoding='utf-8') as file:
    json.dump(decrypted_users, file, indent=4, ensure_ascii=False)

#запись в эксель файл разсшифрованных данных
dec=pd.DataFrame(decrypted_users).to_excel("decrypted.xlsx")
