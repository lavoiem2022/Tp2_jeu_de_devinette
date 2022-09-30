#Projet jeu de devinette fait par Mehdi Serge Lavoie 406
import random
boucle = True

nombre = random.randint(1, 100)
print(nombre)
while boucle:



    user_guess = int(input("Donnez moi un nombre de 1 a 100"))

    if user_guess > nombre:
        print("C'est un nombre plus bas")
    elif user_guess < nombre:
        print("C'est un nombre plus haut")
    else:
        print ("Tu as gagner Bravo!")




