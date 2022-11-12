###PASSWORD GENERATOR###
from random import *
###LISTS CONTAINING EVERY ALLOWED SYMBOL IN A PASSWORD
symboles = [33, 34, 35, 36, 37, 38, 38, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 123]
majuscules = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
nombres = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
minuscules = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
###SHUFFLE FUNCTION
def echange(tab):
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
    longueur_mdp = int(input("Entrez le nombre de caractères voulus dans votre mot de passe entre 12 et 24:" + " "))
    while longueur_mdp < 12 or longueur_mdp > 24:
        longueur_mdp = int(input("Cette longueur choisie n'est pas dans les normes, veuillez entrez un nombre compris entre 12 et 24"))
    return tableau(longueur_mdp)


###Generation d'un tableau de la taille choisie par l'utilisateur###
###CREATION OF A LIST OF THE LENGTH CHOSEN BY USER
def tableau(longueur):
    tableau_mdp = [0 for i in range(longueur)]
    return tableau_mdp


###Fonction qui permet de generer le mot de passe a partir de toutes les donnees precedentes
###FUNCTION TO CREATE PASSWORD USING ALL PREVIOUS DATA###
def mdp_type(tableau_mdp, symboles, majuscules, nombres, minuscules):
    i = 0
    nmb_symbole = len(tableau_mdp) //7
    nmb_majuscules = len(tableau_mdp) // 5
    nmb_nombre = len(tableau_mdp) // 5
    
    while nmb_symbole > 0:
        tableau_mdp[i] = chr(symboles[randint(0, len(symboles) - 1)])
        nmb_symbole -= 1
        i += 1
    while nmb_majuscules > 0:
        tableau_mdp[i] = chr(majuscules[randint(0, len(majuscules) - 1)])
        nmb_majuscules -= 1
        i += 1
    while nmb_nombre > 0:
        tableau_mdp[i] = chr(nombres[randint(0, len(nombres) - 1)])
        nmb_nombre -= 1
        i += 1
    while i <= len(tableau_mdp) - 1:
        tableau_mdp[i] = chr(minuscules[randint(0, len(minuscules) - 1)])  
        i += 1
    return tableau_mdp  

#programme principal
###MAIN PROGRAM
tableau_avantfin = longueur_choisie()

tableau_fini = mdp_type(tableau_avantfin, symboles, majuscules, nombres, minuscules)
for i in range(3):
    echange(tableau_fini)


res = tableau_fini[0]
for i in range(1, len(tableau_fini) - 1):
    res = res + stringing(tableau_fini, i)

print("Voici votre mot de passe: ", res)
#print("Here's your password: ", res)
