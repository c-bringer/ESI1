from CompteBancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    def __init__(self, nom = 'Dupont', solde = 1000):
        CompteBancaire.__init__(self, nom, solde)
        self.taux = 0.3

    def changeTaux(self, valeur):
        self.taux = valeur

    def capitalisation(self, nombreMois):
        print('Capitalisation sur {0} mois au taux mensuel de {1} %.'.format(nombreMois, self.taux))
        CompteBancaire.depot(self, ((nombreMois * 30) / 365) * self.taux / 100 * CompteBancaire.getSolde(self))