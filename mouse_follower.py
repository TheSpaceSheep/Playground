from random import random
from tkinter import*
from math import*

fenetre = Tk()


width = 1920
height = 1080

c = 5   # cell size

world = Canvas(fenetre, width=width, height=height)
world.pack()


class Walker:
    """A walking square"""

    def __init__(self, pos_x, pos_y, color=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.dirx = fenetre.winfo_pointerx() - pos_x*c
        self.diry = fenetre.winfo_pointery() - pos_y*c

    def step(self, direction=-1):
        """
        Step in chosen direction
        N    E    S    O
        1    2    3    4
        If no direction is specified, it is chosen randomly
        (influenced the position of the mouse cursor)
        """
        self.dirx = fenetre.winfo_pointerx() - self.pos_x*c
        self.diry = fenetre.winfo_pointery() - self.pos_y*c

        if direction == -1:
            direction = 4*random()

        sepx = tanh(self.dirx / 1980) + 1
        sepy = tanh(self.diry / 1080) + 1

        if direction <= sepx:        # move north
            self.pos_x += 1
        elif direction <= 2:         # move east
            self.pos_x -= 1
        elif direction <= 2 + sepy:  # move south
            self.pos_y += 1
        elif direction <= 4:         # move west
            self.pos_y -= 1

        # dealing with borders
        if self.pos_x >= width//c:
            self.pos_x -= 1
        elif self.pos_x < 0:
            self.pos_x += 1
        elif self.pos_y >= height//c:
            self.pos_y -= 1
        elif self.pos_y < 0:
            self.pos_y += 1


bob = Walker(50, 40, 'red')
world.create_rectangle(bob.pos_x*c, bob.pos_y*c, (bob.pos_x + 1)*c, (bob.pos_y + 1)*c, fill=bob.color)
world.pack()


while 1:
    bob.step()

    world.create_rectangle(bob.pos_x*c, bob.pos_y*c, (bob.pos_x + 1)*c, (bob.pos_y + 1)*c, fill=bob.color)
    world.pack()

    fenetre.update()


