from Cercle import Cercle
from Cylindre import Cylindre
from Cone import Cone
from JeuDeCartes import JeuDeCartes

print('1. Classe Cercle')
cyl = Cylindre(5, 7)
print(cyl.surface())
#78.54
print(cyl.volume())
#549.78

print('\n\n\n\n\n2. classe Cone')
co = Cone(5,7)
print(co.volume())
#183.26

print('\n\n\n\n\n3. Classe jeuDeCartes')
jeu = JeuDeCartes()
jeu.battre()
for n in range(53): # tirage des 52 cartes :
    c = jeu.tirer()
    if c == None: 
        print('Terminé !')
    else:
        print(jeu.nom_carte(c))