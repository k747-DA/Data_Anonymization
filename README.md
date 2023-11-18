<h1 align="center">Data anonymization</h1>
Задача по предмету Информационная безопасность (2 группа).

Задача 1 группы: https://github.com/AhmetshaLee/IS-database-project#is-database-project (ИС-проект базы данных)
<h3 align="center">Цель работы</h3>
Цель работы: создать программу, которая будет обезличивать файл, совместимый с программой от группы 1.

<h3 align="center">Используемые библиотеки и язык прогромирования</h3> 

Язык прогромирования выбран: ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Используемые библиотеки: 
cryptography - это библиотека Python для обеспечения криптографических функций. Данная библиотека была выбрана, так как она предоставляет разнообразные инструменты и алгоритмы для выполнения шифрования, дешифрования, создания хешей сообщений и генерации ключей. В програме код импортирует класс Fernet из библиотеки cryptography.fernet, который позволяет нам использовать алгоритм шифрования Fernet для шифрования и дешифрования данных.

Для установки cryptography нужно выполнить команду:

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=$+pip+install+cryptography)](https://git.io/typing-svg)

Использование встроеной библиотеки Python json, которая предоставляет функции для работы с данными в формате JSON.

<h3 align="center">Описание кода</h3> 
  1. def generate_key(): - Это начало определения функции generate_key, которая генерирует случайный ключ шифрования с использованием метода Fernet.generate_key() и возвращает его.

  2. def load_key(file_path): - Это начало определения функции load_key, которая принимает параметр file_path (путь к файлу ключа). Она пытается открыть файл, считать ключ из файла, и возвращает ключ. Если файл не найден, она генерирует новый ключ, записывает его в файл и возвращает новый ключ.

  3. def encrypt_data(data, key): - Это начало определения функции encrypt_data, которая принимает данные и ключ, создает объект Fernet с использованием ключа, затем шифрует данные и возвращает зашифрованный результат.

  4. def decrypt_data(encrypted_data, key): - Это начало определения функции decrypt_data, которая принимает зашифрованные данные и ключ, создает объект Fernet с использованием ключа, затем дешифрует данные и возвращает дешифрованный результат.

  5. def decrypt_data_from_file(file_path, key): - Это начало определения функции decrypt_data_from_file, которая принимает путь к файлу и ключ. Она открывает файл, считывает зашифрованные данные из файла, затем дешифрует и возвращает дешифрованный результат.

  6. try: - Это начало блока, в котором происходит попытка выполнить определенный блок кода. В этом случае, мы пытаемся открыть файл users.json для чтения.
with open('users.json', 'r', encoding='utf-8') as file: - Это открытие файла users.json в режиме чтения с указанием кодировки utf-8. Файл будет открыт как объект file.

  7. key = load_key('secret.key') - Это вызов функции load_key для загрузки ключа из файла secret.key.

  8. encrypted_data = encrypt_data(data, key) - Это вызов функции encrypt_data для шифрования данных из файла с использованием загруженного ключа.

  9. with open('users_encrypted.json', 'w', encoding='utf-8') as file: - Это открытие файла users_encrypted.json в режиме записи с указанием кодировки utf-8. Файл будет открыт как объект file.

 10. json.dump({"data": encrypted_data.decode()}, file) - Это запись зашифрованных данных в формате JSON в файл users_encrypted.json.

  11. decrypted_data = decrypt_data_from_file('users_encrypted.json', key) - Это вызов функции decrypt_data_from_file для дешифровки данных из файла users_encrypted.json с использованием ключа.
Далее идет блок кода, где дешифрованные данные записываются в файл decrypted_users.json и ключ сохраняется в файл decryption_key.key.

  12. except (FileNotFoundError, json.JSONDecodeError) as e: - Это начало блока, который выполняется в случае возникновения исключений FileNotFoundError или json.JSONDecodeError. В данном случае, если такие исключения возникнут, будет выведено сообщение об ошибке. 

<h3 align="center">Data anonymization</h3>

Ссылка на призентацию: https://docs.google.com/presentation/d/1tCGOnWw2tFFuYsGEm9Hs45owa1jznmdL/edit?usp=sharing&
