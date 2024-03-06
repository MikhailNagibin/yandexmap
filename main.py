import pygame
import sys
import os
from Functions import get

toponym = input().split()


map_request = "https://static-maps.yandex.ru/1.x/"
map_params = {
    "ll": ",".join([toponym[0], toponym[1]]),
    "spn": ",".join(['0.005', '0.005']),
    "l": "map",
    "scale": '1.0'
}


response = get(map_params)


pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load("map.png"), (0, 0))
pygame.display.flip()
ranning = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if map_params['scale'] != '4.0' and event.key == pygame.K_w:
                map_params['scale'] = str(float(map_params['scale']) + 0.5)
                print(map_params['scale'])
            elif map_params['scale'] != '1.0' and event.key == pygame.K_s:
                map_params['scale'] = str(float(map_params['scale']) - 0.5)
                print(map_params['scale'])
            response = get(map_params)
            screen.blit(pygame.image.load("map.png"), (0, 0))
    pygame.display.flip()
#37.547746 55.913202