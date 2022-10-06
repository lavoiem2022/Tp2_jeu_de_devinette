#Projet jeu de devinette fait par Mehdi Serge Lavoie 406
import random
boucle_jeu = True
nbr_essaies= 1
nombre = random.randint(1, 100)
print(nombre)
while boucle_jeu:


    user_guess = int(input("Donnez moi un nombre de 1 a 100: "))

    if user_guess > nombre:
        print("C'est un nombre plus bas")
        nbr_essaies +=1
    elif user_guess < nombre:
        print("C'est un nombre plus haut")
        nbr_essaies += 1
    elif user_guess == nombre:
        print ("Tu as gagner Bravo!. Tu as réussi en ", nbr_essaies," essaies")
        recommencer = input("Voulez vous recommencer oui ou non")
        if recommencer == "oui":
            nombre = random.randint(1, 100)
            nbr_essaies = 1
        elif recommencer == "non":
            boucle_jeu = False


    



