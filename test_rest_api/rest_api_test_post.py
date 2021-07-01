import requests
import json

# Адрес вашего REST-сервера
SERVER_ADDR = "http://127.0.0.1:23991/api"

# Загружаем json-строку из файла
def json_from_file(filename):
    json_file = open(filename, 'r')
    data = json_file.read()
    json_file.close()
    return data

if __name__ == '__main__':
    # Проверка GET-запроса
    resp = requests.get(SERVER_ADDR + "/product")
    result = resp.json()
    print("GET result:", result)

    # Проверка POST-запроса
    json_data = json_from_file("post.json")     # загружаем данные из файла
    resp = requests.post(SERVER_ADDR + "/product", data=json_data, headers={'content-type': 'application/json'})
    result = resp.json()
    print("POST result:", result)
    
    input("Нажмите Enter для выхода...")