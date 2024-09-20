from random import random

import pygame
import random

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Тир.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/Цель.jpg")
target_wide = 80
target_height = 84

target_x = random.randint( a:0, SCREEN_WIDTH - target_wide )
target_y = random.randint( b: 0, SCREEN_HEIGHT - target_height)

color = (random.randint(a: 0, b: 255), random.randint(a: 0, b: 255), random.randint(a: 0, b: 255))



running = True
while running:
    pass

pygame.quit()
