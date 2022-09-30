#Projet jeu de devinette fait par Mehdi Serge Lavoie 406
import random
boucle = True
while boucle:

    nombre = random.randint(1, 100)

def restart():
    recommence = input("Voulez-vous continuer?")
    if recommence == ("oui"):
        return True
    elif recommence == ("non"):
        return False
    return restart()

Start = int(input("Donnez moi un nombre de 1 a 100"))
if Start > nombre:
    print("C'est un nombre plus haut")
if Start < nombre:
    print("C'est un nombre plus bas")
if Start ^ nombre:
    print ("Tu as gagner Bravo!")



