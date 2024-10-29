import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption('Zero Deaths')
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.quit()
    quit()

if __name__ == '__main__':  #only run this main function if we run the file directly
    main(window)   # dont run if we import this in something and then run that

