print('1.1 Génération de tables de multiplication')
def tableMulti(n):
    # Fonction générant la table de multiplication par n (10 termes)
    # La table sera renvoyée sous forme d'une chaîne de caractères :
    i, ch = 0, ""
    while i < 10:
        i = i + 1
        ch = ch + str(i) + "*" + str(n) + " = " + str(i * n) + " | "
    return ch
NomF = input("Nom du fichier à créer : ")
fichier = open(NomF, 'w')
# Génération des tables de 2 à 30 :
table = 2
while table < 31:
    fichier.write(tableMulti(table) + '\n')
    table = table + 1
fichier.close()



print('\n1.2 Recherche et affichage de la phrase la plus longue')
plusLongue = max(open('tablemultiplication.txt'), key=len)
with open('tablemultiplication.txt','r') as f:
    i = 1
    for line in f:
        if plusLongue == f.readline(i):
            break
        i = i + 1
print("La ligne la plus longue est la {}eme,".format(i))
size = len(max(open('tablemultiplication.txt'), key=len))
print("Elle contient {} caractères, la voici :".format(size))
print(plusLongue)



print('\n1.3 Recherche et affichage de la phrase la plus longue : variante')
def nbMots(chaineCharactere):
    return len(chaineCharactere.split())

def tailleChaine(chaineCharactere):
    return len(chaineCharactere)

with open('tablemultiplication.txt','r') as f:
    i = 0
    numMots = 0
    numLigne = 0
    ligne = ""
    for line in f:
        print("Ligne n°:{}, longueur = {}, {} mots.".format(i,tailleChaine(line),nbMots(line)))
        i = i + 1
        if(numMots<nbMots(line)):
            numMots = nbMots(line)
            numLigne = i
            ligne = line
    print("La ligne la plus longue est la {}eme,".format(numLigne))
    print("Elle contient {} mots, la voici :".format(numMots))
    print(line)



print('\n1.4 Recherche et affichage de la phrase la plus longue : variante avec filter')
# la fonction booléenne
def hasSpace(x):
    return(x==" ")
# la nouvelle méthode sans boucle for ni while
def nbMots (chaine):
    listeEspaces = list(filter(hasSpace,chaine))
    # décommenter pour voir la liste résultante
    #print(listeEspaces)
    nbSpaces = len(listeEspaces)
    return nbSpaces+1



print('\n1.5 Arrondi de nombres à virgule')
with open('test.txt','r') as f:
    for line in f:
        nombre = float(line)
        fichier = open('autre.txt','a')
        fichier.writelines([str(round(nombre,0))+"\n"])