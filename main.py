#Projet jeu de devinette fait par Mehdi Serge Lavoie 406
import random
boucle_jeu = True
nbr_essaies= 1

borne_minimum = int(input("Choisis les bornes minimum"))
borne_maximum = int(input("Choisis les bornes maximum"))
nombre = random.randint(borne_minimum, borne_maximum)
print(nombre)
print ("Jai choisis un nombre de ",borne_minimum ," a " ,borne_maximum,"a toi de le deviner")


while boucle_jeu:



    user_guess = int(input("Donnez moi un nombre"))

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
            borne_minimum = int(input("Choisis les bornes minimum"))
            borne_maximum = int(input("Choisis les bornes maximum"))
            print("Jai choisis un nombre de ", borne_minimum, " a ", borne_maximum, "a toi de le deviner")
            nombre = random.randint(borne_minimum, borne_maximum)
            nbr_essaies = 1
        elif recommencer == "non":
            boucle_jeu = False


    



