from random import random
from tkinter import*
from math import*

fenetre = Tk()


width = 400
height = 200

c = 5   # cell size

world = Canvas(fenetre, width=width, height=height)
world.pack()

presence = {}  # dictionnaire de walkers (contient les walkers présents pour la clé (x, y))


class Walker:
    """A walking square"""

    def __init__(self, pos_x, pos_y, color=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.dirx = fenetre.winfo_pointerx() - pos_x*c
        self.diry = fenetre.winfo_pointery() - pos_y*c
        presence[pos_x, pos_y] = [self]

    def encounter(self, fellow_walker):
        world.create_rectangle((self.pos_x-10)*c, (self.pos_y-10)*c, (self.pos_x+10)*c, (self.pos_y+10)*c, fill='green')

    def step(self, direction=-1):
        """
        Step in chosen direction
        N    E    S    O
        1    2    3    4
        """
        presence[self.pos_x, self.pos_y].remove(self)  

        if direction == -1:
            direction = 4*random()

        if direction <= 1:    # move north
            self.pos_x += 1
        elif direction <= 2:  # move east
            self.pos_x -= 1
        elif direction <= 3:  # move south
            self.pos_y += 1
        else:                 # move west
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

        # put walker on new cell
        if (self.pos_x, self.pos_y) in presence:
            presence[self.pos_x, self.pos_y].append(self)
        else:
            presence[self.pos_x, self.pos_y] = [self]

        # encounters with other walkers
        for w in presence[self.pos_x, self.pos_y]:
            if w != self:
                self.encounter(w)


bob = Walker(50, 40, 'red')
kenny = Walker(100, 100, 'blue')

world.create_rectangle(bob.pos_x*c, bob.pos_y*c, (bob.pos_x + 1)*c, (bob.pos_y + 1)*c, fill=bob.color)
world.create_rectangle(kenny.pos_x*c, kenny.pos_y*c, (kenny.pos_x + 1)*c, (kenny.pos_y + 1)*c, fill=kenny.color)
world.pack()


for i in range(20000):
    bob.step()
    kenny.step()

    world.create_rectangle(bob.pos_x*c, bob.pos_y*c, (bob.pos_x + 1)*c, (bob.pos_y + 1)*c, fill=bob.color)
    world.create_rectangle(kenny.pos_x * c, kenny.pos_y * c, (kenny.pos_x + 1) * c, (kenny.pos_y + 1) * c,
                           fill=kenny.color)
    world.pack()
    fenetre.update()


fenetre.mainloop()
