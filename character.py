import numpy as np

move_directions = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0]
]

dir_names = ['Up', 'Down', 'Left', 'Right']


class Character:
    def __init__(self, pos=None, health=100):
        self.pos = pos
        self.dir = 'Up'

    def move(self, key, map_grid):
        self.dir = dir_names[key]
        new_pos = np.add(self.pos, move_directions[key])
        if map_grid[new_pos[0]][new_pos[1]] == 'f':
            self.pos = new_pos
