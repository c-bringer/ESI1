import random

class JeuDeCartes:
    def __init__(self):
        self.cartes = [ 
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
            (13, 0),
            (14, 0),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (11, 1),
            (12, 1),
            (13, 1),
            (14, 1),
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (6, 2),
            (7, 2),
            (8, 2),
            (9, 2),
            (10, 2),
            (11, 2),
            (12, 2),
            (13, 2),
            (14, 2),
            (2, 3),
            (3, 3),
            (4, 3),
            (5, 3),
            (6, 3),
            (7, 3),
            (8, 3),
            (9, 3),
            (10, 3),
            (11, 3),
            (12, 3),
            (13, 3),
            (14, 3)
        ]

    def nom_carte(self, cartes):
        type = ''
        number = ''

        if cartes[1] == 0:
            type = 'Pique'
        elif cartes[1] == 1:
            type = 'Trefle'
        elif cartes[1] == 2:
            type = 'Carreau'
        else:
            type = 'Coeur'

        if cartes[0] == 14:
            number = 'As'
        elif cartes[0] == 13:
            number = 'Roi'
        elif cartes[0] == 12:
            number = 'Dame'
        elif cartes[0] == 11:
            number = 'Valet'
        else:
            number = cartes[0]

        return '{0} de {1}'.format(number, type)

    def battre(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if len(self.cartes) < 1:
            valeur = None
        else:
            valeur = self.cartes[0]
            self.cartes.pop(0)

        return valeur