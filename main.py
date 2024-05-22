"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: main.py
Purpose of Document: Acting as the main file to run the majority of the code from
Referenced Code:


"""

import pygame
import sys
from player import player

pygame.init()

display = pygame.display.set_mode((1280,720 ))
clock = pygame.time.Clock()
running = True

player(400, 300 ,32, 32)
display_scroll = [0,0]


while running:
    display.fill((24,164,86))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        display_scroll[0] -= 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5
    

    clock.tick(60)
    pygame.display.update()
  