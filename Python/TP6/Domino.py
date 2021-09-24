class Domino:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def affiche_points(self):
        print('Face A : {0} Face B : {1}'.format(self.a, self.b))

    def valeur(self):
        return self.a + self.b