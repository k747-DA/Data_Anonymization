# Этот код импортирует класс Fernet из библиотеки cryptography.fernet, который позволяет нам использовать алгоритм шифрования Fernet для шифрования и дешифрования данных.
from cryptography.fernet import Fernet
import json


def generate_key():  # Это начало определения функции generate_key, которая генерирует случайный ключ шифрования с использованием метода Fernet.generate_key() и возвращает его.
    return Fernet.generate_key()


# Это начало определения функции load_key, которая принимает параметр file_path (путь к файлу ключа).
# Она пытается открыть файл, считать ключ из файла, и возвращает ключ.
# Если файл не найден, она генерирует новый ключ, записывает его в файл и возвращает новый ключ.
def load_key(file_path):
    try:
        with open(file_path, 'rb') as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Ключ шифрования не найден. Генерируем новый ключ...")
        key = generate_key()
        with open(file_path, 'wb') as key_file:
            key_file.write(key)
        return key

# Это начало определения функции encrypt_data,
# которая принимает данные и ключ, создает объект Fernet с использованием ключа,
# затем шифрует данные и возвращает зашифрованный результат
def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

#  Это начало определения функции decrypt_data, которая принимает зашифрованные данные и ключ,
#  создает объект Fernet с использованием ключа, затем дешифрует данные и возвращает дешифрованный результат.
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

# Это начало определения функции decrypt_data_from_file, которая принимает путь к файлу и ключ.
# Она открывает файл, считывает зашифрованные данные из файла, затем дешифрует и возвращает дешифрованный результат.
def decrypt_data_from_file(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as file:
        encrypted_data = json.load(file)["data"].encode()
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

#Это начало блока, в котором происходит попытка выполнить определенный блок кода.
# В этом случае, мы пытаемся открыть файл users.json для чтения.
try:
    #Это открытие файла users.json в режиме чтения с указанием кодировки utf-8. Файл будет открыт как объект file.
    with open('users.json', 'r', encoding='utf-8') as file:
        data = file.read()
    key = load_key('secret.key')

    encrypted_data = encrypt_data(data, key)
    with open('users_encrypted.json', 'w', encoding='utf-8') as file:
        json.dump({"data": encrypted_data.decode()}, file)
    print("Данные успешно зашифрованы и сохранены в файл users_encrypted.json")

    decrypted_data = decrypt_data_from_file('users_encrypted.json', key)
    with open('decrypted_users.json', 'w', encoding='utf-8') as file:
        json.dump({"data": decrypted_data}, file)
    with open('decryption_key.key', 'wb') as key_file:
        key_file.write(key)
    print("Зашифрованные данные успешно расшифрованы и сохранены в файл decrypted_users.json")
except (FileNotFoundError, json.JSONDecodeError) as e:
    print("Не удалось зашифровать/расшифровать данные из файла. Пожалуйста, убедитесь, что файлы существуют и содержат корректные данные.")