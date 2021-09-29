# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico(fileName, c):
    dns = {}
    with open(fileName, 'r') as f:
        i = 1
        for line in f:
            #lineContent = re.findall(r'[^,\s]+', f.readline(line))
            lineContent = f.readline(line).split(sep = c)
            print(lineContent)
            i = i + 1
    return 'Creation d\'un dictionnaire a partir du fichier \'{0}\' avec \'{0}\' entrees'.format(fileName, i)

###### exercice 02
def verifUrl(url):
    import re
    regex = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    print(re.match(regex, url) is not None)

###### exercice 03


###### exercice 04


###### exercice 05
    

###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
	from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
	print("exercice 00 #######################")
	salutations = exempleHello("Michel")
	print(salutations)
	print(salutations.split(sep=" "))

	###### exercice 01
	print("exercice 01 #######################")
	resolveDns = makeDico('dns.txt', ',')
	
	###### exercice 02
	print("exercice 02 #######################")
	result = verifUrl(resolveDns[0])

	###### exercice 03
	print("exercice 03 #######################")


	###### exercice 04
	print("exercice 04 #######################")


	###### exercice 05
	print("exercice 05 #######################")


	###### exercice 06
	print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
	print("exercice 07 #######################")


	###### exercice 08
	print("exercice 08 #######################")


	###### exercice 09
	print("exercice 09 #######################")
	
	###### exercice 10
	print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()