import pygame
import sys
import os
import requests

toponym = input().split()

delta = ['0.005', '0.005']
par_z = 0

map_request = "https://static-maps.yandex.ru/1.x/"

map_params = {
    "ll": ",".join([toponym[0], toponym[1]]),
    "spn": ",".join(delta),
    "z": str(par_z),
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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and par_z <= 21:
            print(par_z)
            par_z += 1

            map_params = {
                "ll": ",".join([toponym[0], toponym[1]]),
                "spn": ",".join(delta),
                "z": str(par_z + 1),
                "l": "map"
            }

            response = requests.get(map_request, params=map_params)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            screen.blit(pygame.image.load(map_file), (0, 0))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pass
    pygame.display.flip()
pygame.quit()
