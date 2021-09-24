from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return round(pi * (self.rayon * self.rayon), 2)