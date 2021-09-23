# -*- coding: utf-8 -*-

print('1.1 acces aux elements d\'une chaine')

print('\n1.1.1 initialiser la chaine ch et afficher sa longueur (la reponse doit etre 28)')
ch = 'Esope reste ici et se repose'
print(len(ch))

print('\n1.1.2 afficher le deuxieme mot de la chaine ch en utilisant les crochets et une plage [x :y]')
print(ch[0:5])

print('\n1.1.3 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :y]')
print(ch[22:28])

print('\n1.1.4 afficher le dernier mot de la chaine ch en utilisant les crochets et une plage [x :]')
print(ch[22:])

print('\n1.1.5 afficher le caractere \'c\' de deux manieres differentes')
print('c')
char = 'c'
ascii = ord(char)
print(chr(ascii))

print('\n1.2 Utilisation combinee de chaines et de variables')
print('1.2.1 Initialiser les chaines suivantes')
meteo = 'aujourd\'hui, il fait %s , la vitesse du vent est %s ,l\'humidite est %s'
tempDeg = "24°"
vitesseVent = "12Km/h"
humidite = "45%"
print(meteo % (tempDeg, vitesseVent, humidite))

print('\n1.2.2 Variante')
beau = 'beau'
vent = 'faible'
correcte = 'correcte'
print(meteo % (beau, vent, correcte))

print('\n1.2.3 Initialiser les chaines suivantes')
chaineA = "cette chaine"
chaineB = "contient %s caractères"
chaineC = "par contre"
chaineD = "celle-ci"
#cette chaine contient 34 caractères
print(chaineA + ' ' + chaineB % (len(chaineA + ' ' + chaineB) - 2))
#celle-ci contient 40 caractères par contre
#TODO
#print(chaineD + ' ' + chaineB + ' ' + chaineC % (len(chaineD + ' ' + chaineB + ' ' + chaineC) - 2))

print('\n1.2.4 Autre méthode de formatage de chaines')
chaineBnew = chaineB.replace("contient %s caractères", "contient {0} caractères")
chaineE = chaineA
chaineF = chaineD + chaineBnew + ' ' + chaineC
print(chaineF.format(len(chaineF)))