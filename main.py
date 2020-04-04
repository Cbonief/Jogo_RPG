import pygame
from game import Game

if __name__ == "__main__":
    win = pygame.display.set_mode((800, 600))
    rpg = Game(win)
    pygame.init()
    rpg.run()
