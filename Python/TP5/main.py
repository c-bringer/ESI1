print('1.1 Génération de tables de multiplication')
with open("tablemultiplication.txt", "w") as file:
  for i in range(2,31):
    for j in range(1,11):
      file.write("{}{} = {} |".format(j, i, i*j))
    file.write("\n")

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
tab_sentance = []
f = open("tablemultiplication.txt", "r")
for x in f:
    tab_sentance.append(str(f.readline()))
longest_sentance = ""
line_number = 0
boucle = 0

for tab in tab_sentance:
    if(len(longest_sentance) < len(tab_sentance[boucle])):
        longest_sentance = tab_sentance[boucle]
        line_number = boucle + 1
    boucle = boucle + 1

print(f"La ligne la plus longue est la {line_number}eme")
print(f"Elle contient {len(longest_sentance)} caractères, la voici :")
print(longest_sentance)

def nb_mots(chaine):
    word = []
    word_length = "" 
    word_list = chaine.split()
    most_long_word_line = 0
    number_of_word = len(word_list)
    for x in range(0, number_of_word):
        word.append(str(chaine.split()[x]))
        print(f'Ligne n°:{x+1}, longueur = {len(word[x])}, 1 mot.')
        if (len(word_length) < len(word[x])):
            word_length = word[x]
            most_long_word_line = x+1   
    print(f'La ligne la plus longue est la {most_long_word_line}eme,\nElle contient {len(word_length)} mots, la voici :\n{word_length}')
    return number_of_word

number_of_word = nb_mots(longest_sentance)
print(f'La ligne ayant le plus de mots est la {line_number}eme,\nElle contient {number_of_word} mots, la voici :\n{longest_sentance}')