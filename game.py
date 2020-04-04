import pygame
from pathlib import Path
import os
import time
import random
import numpy as np
from level_generator import create_level
from walker import Walker
from character import Character

moveEvents = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
params_translate = [
    {'Up': 0, 'Down': 0, 'Left': -1, 'Right': 0},
    {'Up': -1, 'Down': 0, 'Left': 0, 'Right': 0}
]

class Game:
    def __init__(self, window):
        self.width = window.get_width()
        self.height = window.get_height()
        self.window = window
        self.empty = pygame.image.load(os.path.join("Game Images", "empty.png"))
        sizeX = round(self.width/10)
        sizeY = round(self.height/10)
        self.empty = pygame.transform.scale(self.empty, (sizeX, sizeY))
        self.char = pygame.image.load(os.path.join("Game Images", "character-removebg-preview.png")).convert_alpha()
        self.char = aspect_scale_x(self.char, sizeX)
        self.char_images = {
            'Up': self.char,
            'Down': pygame.transform.flip(self.char, False, True),
            'Left': pygame.transform.rotate(self.char, 90),
            'Right': pygame.transform.rotate(self.char, -90)
        }
        self.grass_door = pygame.image.load(os.path.join("Game Images", "door.png"))
        self.door = {
            'Up': pygame.transform.scale(self.grass_door, (sizeX, sizeY)),
            'Down': pygame.transform.flip(pygame.transform.scale(self.grass_door, (sizeX, sizeY)), False, True),
            'Left': pygame.transform.scale(pygame.transform.rotate(self.grass_door, 90), (sizeX, sizeY)),
            'Right': pygame.transform.scale(pygame.transform.rotate(self.grass_door, -90), (sizeX, sizeY))
        }
        self.grass = pygame.image.load(os.path.join("Game Images", "grass.png"))
        self.grass = pygame.transform.scale(self.grass, (sizeX, sizeY))
        self.wall = pygame.image.load(os.path.join("Game Images", "wall.png"))
        self.wall = pygame.transform.scale(self.wall, (sizeX, sizeY))
        self.play = True
        [self.grid, self.door_direction] = create_level([10, 10], startingWalkers=2, chanceWalkerChangeDir = 0.2, chanceWalkerSpawn = 0.05, chanceWalkerDestroy = 0.05, maxWalkers = 10, percentToFill = 0.2)
        self.player = Character([5, 5], 100)

    def display_grid(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                floor = self.grid[i][j]
                # color = (255, 0, 0)
                if floor == 'r':
                    self.window.blit(self.wall, (i * self.width/len(self.grid), j * self.height/len(self.grid[0])))
                elif floor == 'e':
                    self.window.blit(self.empty, (i * self.width/len(self.grid), j * self.height/len(self.grid[0])))
                elif floor == 'f':
                    self.window.blit(self.grass, (i * self.width / len(self.grid), j * self.height / len(self.grid[0])))
                elif floor == 'd':
                    self.window.blit(self.door[self.door_direction], (i * self.width / len(self.grid), j * self.height / len(self.grid[0])))

    def display_character(self):
        sizeX = self.width / len(self.grid)
        sizeY = self.height/len(self.grid[0])
        dif = self.char.get_height() - sizeX
        posX = int(self.player.pos[0] * sizeX + params_translate[0][self.player.dir]*dif)
        posY = int(self.player.pos[1] * sizeY + params_translate[1][self.player.dir]*dif)
        self.window.blit(self.char_images[self.player.dir], [posX, posY])
        pygame.draw.rect(self.window, (0, 255, 0), (self.player.pos[0] * sizeX , self.player.pos[1] * sizeY, 80, 5))


    def run(self):
        clock = pygame.time.Clock()
        while self.play:
            clock.tick(500)
            self.display_grid()
            self.display_character()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

                if event.type == pygame.KEYDOWN:
                    for index in range(0, 4):
                        if event.key == moveEvents[index]:
                            self.player.move(index, self.grid)

            pygame.display.update()


def aspect_scale_x(img, bx):
    ix, iy = img.get_size()
    scale_factor = bx/float(ix)
    sx = round(scale_factor * ix)
    sy = round(scale_factor * iy)

    return pygame.transform.scale(img, (sx, sy))
