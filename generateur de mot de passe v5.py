###PASSWORD GENERATOR###
from random import *
###LISTS CONTAINING EVERY ALLOWED SYMBOL IN A PASSWORD
symboles = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96]

###SHUFFLE FUNCTION
def melange(tab):
    for i in range(len(tab)):
        rand = randint(0, i)
        res = tab[i]
        tab[i] = tab[rand]
        tab[rand] = res
    return tab
###fonction qui transforme chaque valeur du tableau en string
###FUNCTION TRANSFORMING EVERY SYMBOL IN MY LIST INTO A STRING
def stringing(tableau, indice):
    a = str(tableau[indice])
    return a

###Declaration de la fonction pour determiner si la longueur du mot de passe entree par l'utilisateur est correcte###
###FUNCTION TO DETERMINATE IF THE LENGTH INPUT BT USER IS BETWEEN 12 AND 24
def longueur_choisie():
    longueur_mdp = int(input("Entrez le nombre de caractères voulus dans votre mot de passe entre 12 et 24: "))
    while longueur_mdp < 12 or longueur_mdp > 24:
        longueur_mdp = int(input("Cette longueur choisie n'est pas dans les normes, veuillez entrez un nombre compris entre 12 et 24: "))
    tableau_mdp = [0 for i in range(longueur_mdp)]
    return tableau_mdp




###Fonction qui permet de generer le mot de passe a partir de toutes les donnees precedentes
###FUNCTION TO CREATE PASSWORD USING ALL PREVIOUS DATA###
def mdp_type(tableau_mdp, symboles):
    i = 0
    nmb_symbole = len(tableau_mdp) //7
    nmb_majuscules = len(tableau_mdp) // 5
    nmb_nombre = len(tableau_mdp) // 5
    
    while nmb_symbole > 0:
        tableau_mdp[i] = chr(symboles[randint(0, len(symboles) - 1)])
        nmb_symbole -= 1
        i += 1
    while nmb_majuscules > 0:
        tableau_mdp[i] = chr(randint(65, 90))
        nmb_majuscules -= 1
        i += 1
    while nmb_nombre > 0:
        tableau_mdp[i] = chr(randint(48, 57))
        nmb_nombre -= 1
        i += 1
    while i <= len(tableau_mdp) - 1:
        tableau_mdp[i] = chr(randint(97, 122))  
        i += 1
    return tableau_mdp  

#programme principal
###MAIN PROGRAM
tableau_avantfin = longueur_choisie()

tableau_fini = mdp_type(tableau_avantfin, symboles)
for i in range(3):
    melange(tableau_fini)


res = tableau_fini[0]
for i in range(1, len(tableau_fini) - 1):
    res = res + stringing(tableau_fini, i)

print("Voici votre mot de passe: ", res)
