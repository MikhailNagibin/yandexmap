import pygame
import sys
import os
import requests

toponym = input().split()


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


map_request = "https://static-maps.yandex.ru/1.x/"

map_params = {
    "ll": ",".join([toponym[0], toponym[1]]),
    "spn": ",".join(['0.005', '0.005']),
    "l": "map"
}


response = requests.get(map_request, params=map_params)
if not response:

    print("Ошибка выполнения запроса:")
    print(map_request)

    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()