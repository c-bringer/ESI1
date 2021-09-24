# -*- coding: utf-8 -*-

from Domino import Domino
from CompteBancaire import CompteBancaire
from Voiture import Voiture
from CompteEpargne import CompteEpargne

print('1. Classe Domino')
d1 = Domino(2, 6)
d2 = Domino(4, 3)
d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())
liste_dominos = []
for i in range(7):
    liste_dominos.append(Domino(6, i))
print(liste_dominos[3])

print('\n\n\n\n\n2. classe CompteBancaire')
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
#Le solde du compte bancaire de Duchmol est de 950 euros.
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()
#Le solde du compte bancaire de Dupont est de 1025 euros.

print('\n\n\n\n\n3. Classe Voiture')
a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
a1.affiche_tout()
#Cette voiture n'a pas de conducteur !
a2.affiche_tout()
#Ford verte pilotée par Juliette, vitesse = 21.6 m/s.
a3.affiche_tout()
#Mercedes rouge pilotée par personne, vitesse = 0 m/s.

print('\n\n\n\n\n4. Classe CompteEpargne')
c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 950 euros.
c1.capitalisation(12)
#Capitalisation sur 12 mois au taux mensuel de 0.3 %.
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 984.769981274 euros.
c1.changeTaux(.5)
c1.capitalisation(12)
#Capitalisation sur 12 mois au taux mensuel de 0.5 %.
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 1045.50843891 euros.
