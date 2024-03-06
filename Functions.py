import requests
import sys


def get(params: dict):
    map_request = "https://static-maps.yandex.ru/1.x/"
    map_params = params
    response = requests.get(map_request, params=map_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return response
