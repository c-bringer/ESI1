from Cylindre import Cylindre

class Cone(Cylindre):
    def __init(self, rayon, hauteur):
        Cylindre.__init__(self, rayon, hauteur)

    def volume(self):
        return round(super().volume() / 3, 2)