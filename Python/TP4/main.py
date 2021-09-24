# -*- coding: utf-8 -*-

from __future__ import print_function

print('1. structures de contrôle : boucle for')
print('1.1 Écrire un programme qui écrit 50 fois « facile ! »')
x = 0
for i in range(50):
    print('Facile!')
    x += 1
print(x)

print('\n1.2 Afficher 25 étoiles « * » sur une ligne (avec une boucle )')
for i in range(25):
    print('*', end =' ')

print('\n1.3 Afficher tous les entiers de 21 à 145 avec une boucle for')
for i in range(20, 145):
    print(i + 1)

print('\n1.4 Afficher le carré de i avec i variant de 1 à 40 et affiche « le carre de 1 = 1 », « le carre de 2=4 »... « le carré de 40 = 1600 »')
res = '{0} = {1}'
for i in range(40):
    print(res.format(i, i**2))

print('\n1.5 Calculer la somme de tous les entiers de 21 à 145 puis l’afficher')
somme = 0
for i in range(20, 145):
    somme = somme + i
print('la somme est de {0}'.format(somme))

print('\n1.6 Calculer 35! (factorielle).')
def factorielle(n):
    if n == 0:
        return 1
    else:
        f = 1
        for k in range(2, n + 1):
            f = f * k
        return f
print(factorielle(35))

print('\n1.7 Afficher un triangle rectangle composé d\'étoiles « * » dont la largueur du côté est 15 *')
for i in range(1, 15 + 1, 1):
    print(i*'*')

print('\n2. structures de contrôle : boucle while')
print('2.1 remplissage de dictionnaire')
dicoAF = {}
saisie = 'o'
while (saisie == 'o'):
    eng = raw_input("Mot anglais: ")
    fr = raw_input("Mot francais: ")
    dicoAF[eng] = fr
    saisie = raw_input("Voulez vous continuer ? o ou autre touche pour stopper")
print('Taille du dico : {0}'.format(len(dicoAF)))
for k, v in dicoAF.items():
    print(k, v)

print('\n2.2 remplissage de dictionnaire : variante')
dicoAF = {}
saisie = 'o'
while (saisie == 'o'):
    eng = raw_input("Mot anglais: ")
    fr = raw_input("Mot francais: ")
    if eng[0] == '$' or fr[0] == '$':
        break
    dicoAF[eng] = fr
print('Taille du dico : {0}'.format(len(dicoAF)))
for k, v in dicoAF.items():
    print(k, v)

print('\n2.3 remplissage de dictionnaire : amélioration')
dicoAF = {}
saisie = 'o'
while (saisie == 'o'):
    eng = raw_input("Mot anglais: ")
    fr = raw_input("Mot francais: ")
    if eng[0] == '$' or fr[0] == '$':
        break
    dicoAF[eng] = fr
print('Taille du dico : {0}'.format(len(dicoAF)))
for k, v in dicoAF.items():
    print(k, v)
if len(dicoAF) <= 1:
    print('le dictionnaire contient {0} entrée'.format(len(dicoAF)))
else:
    print('le dictionnaire contient {0} entrées'.format(len(dicoAF)))

print('\n2.4 Construction d’un dictionnaire français anglais')
dicoFA = {v: k for k, v in dicoAF.iteritems()}
print(dicoAF)
print(dicoFA)