# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
from types import resolve_bases

def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)

###### exercice 01
def makeDico(file, sep):
    dns = {}
    i = 0
    with open(file, 'r') as f:
        for line in f:
            lineSep = line.split(sep)
            dns.update({lineSep[0] : lineSep[1].replace('\n', '')})
            i += 1
    f.close()
    print("Creation d'un dictionnaire a partir du fichier \'{0}\' avec \'{1}\' entrees".format(file, i))
    return dns

###### exercice 02
def verifUrl(url):
    result = False

    if url.count('.') == 1 and len(url.split('.')[1]) <= 3:
        result = True
    else:
        print("url mal formee")
	
    return result

###### exercice 03
def getTLD(url):
	result = False
	result = verifUrl(url)

	if result == False:
		print('TLD mal formee')
		return False
	else:
		return url.split('.')[1]

###### exercice 04
def verifTLD(tldOK, tld):
	for t in tldOK:
		if t == tld:
			return True
	print('TLD absente')
	return False

###### exercice 05
def ipVerifFormat(adresseIp):
	result = False
	splitIp = adresseIp.split('.')
	
	if adresseIp.count('.') == 3:
		if int(splitIp[0]) >= 0 and int(splitIp[0]) <= 255:
			if int(splitIp[1]) >= 0 and int(splitIp[1]) <= 255:
				if int(splitIp[2]) >= 0 and int(splitIp[2]) <= 255:
					if int(splitIp[3]) >= 0 and int(splitIp[3]) <= 255:
						result = True
	else:
		print('nombre de champs incorrect')
	return result

###### exercice 06
def makeTLD(dico):
    tldOk = []
    for e, k in dico.items():
        if not getTLD(e) in tldOk:
            tldOk.append(getTLD(e))
    print("Creation d'une liste de TLD comprenant {} entrees".format(len(tldOk)))
    return tldOk


# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns:
	def __init__(self, dico):
		self.__resolDns = dico

###### exercice 08
	def resolDns(self, url):
		result = False

		if url.count('.') == 1 and len(url.split('.')[1]) <= 3:
			for e, k in self.__resolDns.items():
				if e == url:
					return k
		else:
			print("erreur de format de l\'url")
		
		print('url introuvable')
		return result

###### exercice 09
	def resolInverse(self, adresseIp):
		result = False
		splitIp = adresseIp.split('.')
		
		if adresseIp.count('.') == 3:
			if int(splitIp[0]) >= 0 and int(splitIp[0]) <= 255:
				if int(splitIp[1]) >= 0 and int(splitIp[1]) <= 255:
					if int(splitIp[2]) >= 0 and int(splitIp[2]) <= 255:
						if int(splitIp[3]) >= 0 and int(splitIp[3]) <= 255:
							for e, k in self.__resolDns.items():
								if k == adresseIp:
									return e
		else:
			print('erreur de format de l\'adresse IP')

		print('adresse IP inconnue')
		return result

###### exercice 10
	def addAsso(self, url, adresseIp):
		if self.ipVerifFormat(adresseIp) == True:
			if self.verifUrl(url) == True:
				if not adresseIp in self.__resolDns.values():
					self.__resolDns[url] = adresseIp
					return True
				else:
					print('existingIP')
			else:
				print('malformedUrl')
		else:
			print('malformedAddress')
	
	def ipVerifFormat(self, adresseIp):
		result = False
		splitIp = adresseIp.split('.')
		
		if adresseIp.count('.') == 3:
			if int(splitIp[0]) >= 0 and int(splitIp[0]) <= 255:
				if int(splitIp[1]) >= 0 and int(splitIp[1]) <= 255:
					if int(splitIp[2]) >= 0 and int(splitIp[2]) <= 255:
						if int(splitIp[3]) >= 0 and int(splitIp[3]) <= 255:
							result = True
		return result

	def verifUrl(self, url):
		result = False

		if url.count('.') == 1 and len(url.split('.')[1]) <= 3:
			result = True
		
		return result

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
	print(resolveDns)
	
	###### exercice 02
	print("exercice 02 #######################")
	resultVerifUrl = verifUrl('toto.fr')
	print(resultVerifUrl)
	resultVerifUrl = verifUrl('to.to.fr')
	print(resultVerifUrl)
	resultVerifUrl = verifUrl('toto.frog')
	print(resultVerifUrl)

	###### exercice 03
	print("exercice 03 #######################")
	resultGetTLD = getTLD('toto.fr')
	print(resultGetTLD)
	resultGetTLD = getTLD('to.to.fr')
	print(resultGetTLD)
	resultGetTLD = getTLD('toto.frog')
	print(resultGetTLD)

	###### exercice 04
	print("exercice 04 #######################")
	listTLD = ['fr', 'com', 'net']
	resultVerifTLD = verifTLD (listTLD, resultGetTLD)
	print(resultVerifTLD)

	###### exercice 05
	print("exercice 05 #######################")
	resultAdresseIp = ipVerifFormat('1.1.1.1')
	print(resultAdresseIp)
	resultAdresseIp = ipVerifFormat('1.2.3.4.5')
	print(resultAdresseIp)
	resultAdresseIp = ipVerifFormat('256.1.1.1')
	print(resultAdresseIp)
	resultAdresseIp = ipVerifFormat('255.1.1.256')
	print(resultAdresseIp)

	###### exercice 06
	print("exercice 06 #######################")
	tldOK = makeTLD(resolveDns)
	print(tldOK)

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
	print("exercice 07 #######################")
	s = serveurDns(resolveDns)

	###### exercice 08
	print("exercice 08 #######################")
	adresseIp = s.resolDns('Leboncoin.fr')
	print(adresseIp)
	adresseIp = s.resolDns('Leboncoin.xyz')
	print(adresseIp)

	###### exercice 09
	print("exercice 09 #######################")
	url = s.resolInverse('193.164.196.17')
	print(url)
	url = s.resolInverse('193.164.196.18')
	print(url)
	
	###### exercice 10
	print("exercice 10 #######################")
	resultat = s.addAsso('developpez.net', '87.98.128.200')
	print(resultat)
	resultat = s.addAsso('coding.nzl', '87.98.128.200')
	print(resultat)
	resultat = s.addAsso('developpez.net', '271.98.128.200')
	print(resultat)
	resultat = s.addAsso('developpez.net', '87.98.1280.200')
	print(resultat)

	#‘developpez.net’, ‘87.98.128.200’
	#‘coding.nzl’, ‘87.98.128.200’
	#‘developpez.net’, ‘271.98.128.200’
	#‘developpez.net’, ‘87.98.1280.200’

if __name__=="__main__":
	print("main()")
	main()