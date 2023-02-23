import random


class Dice:
    def __init__(self, nb_face=6):
        self.nb_face = nb_face
        self.value = 0

    def roll(self):
        self.value = random.randint(1, self.nb_face)
