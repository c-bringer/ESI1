class CompteBancaire:
    def __init__(self, nom = 'Dupont', solde = 1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def getSolde(self):
        return self.solde

    def affiche(self):
        print('Le solde du compte bancaire de {0} est de {1} euros.'.format(self.nom, self.solde))