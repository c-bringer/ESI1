from Cercle import Cercle

class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur

    def volume(self):
        return round(Cylindre.surface(self) * self.hauteur, 2)