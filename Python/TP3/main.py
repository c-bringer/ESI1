# -*- coding: utf-8 -*-

print('1.1 Modifier une liste')
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee.pop(len(annee) - 1)
annee.pop(len(annee) - 1)
annee.pop(len(annee) - 1)
print(annee)

print('/n 1.1.2 Puis rajoutez les mois \'Octobre\', \'Novembre\', \'Décembre\' à la fin')
annee.append('Octobre')
annee.append('Novembre')
annee.append('Decembre')
print(annee)

print('/n1.1.3 Supprimez les trois derniers éléments un par un, dans un premier temps')
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
annee.pop(len(annee) - 1)
annee.pop(len(annee) - 1)
annee.pop(len(annee) - 1)
annee.append('Octobre')
annee.append('Novembre')
annee.append('Decembre')
print(annee)

print('\n1.1.4 Pour aller plus loin : la liste ‘en compréhension’')
x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y + 1 for y in x]
print(resultat)

print('\n2. Tuples')
print('2.1 Accès aux éléments d’un tuple')
moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print(moisDeLannee[3])

print('\n2.2 Vérifier la présence d’un élément dans un tuple')
if 'Mars' in moisDeLannee:
    print('Mars est dans la tuples')
else:
    print('Mars est pas dans la tuples')

print('\n3. Dictionnaires')
print('3.1 Ajoutez des éléments au dictionnaire')
age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}
age["david"] = 22
age["veronique"] = 21
age["sylvie"] = 30
age["damien"] = 37
print(age)

print('\n3.2 Accéder à une valeur à partir d’une clé')
print(age["sylvie"])

print('\n3.3 Accéder à une valeur à partir d’une clé')
keys = list(age.keys())
values = list(age.values())
position = values.index(30)
print(keys[position])

print('\n3.4 Gérer des valeurs multiples')
club = {}
club["pierre durand"] = (1986, 1.72, 70)
club["victor dupont"] = (1987, 1.89, 57)
club["paul dupuis"] = (1989, 1.60, 92)
club["jean rieux"] = (1985, 1.88, 77)
print(club)

print('\n3.5 Afficher les données d’un sportif')
keys = list(club.keys())
values = list(club.values())
position = values.index((1986, 1.72, 70))
name = keys[position]
dateNaissSportif = club['pierre durand'][0]
poidsSportif = club['pierre durand'][2]
tailleSportif = club['pierre durand'][1]
formatDonnees = "Le sportif nommé {0} est né en {1}, sa taille est de {2}m et son poids est de {3}Kg"
print(formatDonnees.format(name, dateNaissSportif, tailleSportif, poidsSportif))

print('\n4. Entrées utilisateur')
print('4.1 Club sportif : variante')
keys = list(club.keys())
values = list(club.values())
s = raw_input("Votre nom: ")
if not s.isalpha():
    print("Merci de saisir un nom")
position = values.index(club[s])
name = keys[position]
dateNaissSportif = club['pierre durand'][0]
poidsSportif = club['pierre durand'][2]
tailleSportif = club['pierre durand'][1]
formatDonnees = "Le sportif nommé {0} est né en {1}, sa taille est de {2}m et son poids est de {3}Kg"
print(formatDonnees.format(name, dateNaissSportif, tailleSportif, poidsSportif))