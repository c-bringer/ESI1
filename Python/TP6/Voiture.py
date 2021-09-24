# -*- coding: utf-8 -*-

class Voiture:
    def __init__(self, marque = 'Ford', couleur = 'rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0

    def choix_conducteur(self, nom):
        self.pilote = nom
    
    def accelerer(self, taux, duree):
        self.vitesse = taux * duree
    
    def affiche_tout(self):
        if self.pilote == 'personne':
            print('Cette voiture n\'a pas de conducteur !')
        else:
            print('{0} {1} pilotée par {2}, vitesse = {3} m/s.'.format(self.marque, self.couleur, self.pilote, self.vitesse))