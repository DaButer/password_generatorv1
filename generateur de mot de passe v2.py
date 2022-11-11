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

###Declaration des fonctions pour determiner si la longueur du mot de passe entree par l'utilisateur est correcte###
###FUNCTIONS TO DETERMINATE IF THE LENGTH INPUT BT USER IS BETWEEN 12 AND 24
def longueur_choisie():
    longueur_mdp = int(input("Entrez le nombre de caractères voulus dans votre mot de passe entre 12 et 24:" + " "))
    return longueur(longueur_mdp)

def longueur(longueur):
    if longueur < 12 or longueur > 24:
        print("Cette longueur choisie est trop courte, veuillez entrez un nombre compris entre 12 et 20" )
        longueur_choisie()
    else:
        return tableau(longueur)
###Generation d'un tableau de la taille choisie par l'utilisateur###
###CREATION OF A LIST OF THE LENGTH CHOSEN BY USER
def tableau(longueur):
    tableau_mdp = [0 for i in range(longueur)]
    return tableau_mdp

###Fonction pour determiner le nombres de symboles, majuscules et chiffres dans le tableau###
###FUNCTIONS TO DETERMINATE THE NUMBER OF SYMBOLS, MAJ, AND MIN IN THE LIST
def nmbsymboles(tableau_mdp):
    return len(tableau_mdp) //7

def maj(tableau_mdp):
    return len(tableau_mdp) // 5
    
    

def nmb(tableau_mdp):
    return len(tableau_mdp) // 5
    
###Fonction qui permet de generer le mot de passe a partir de toutes les donnees precedentes
###FUNCTION TO CREATE PASSWORD USING ALL PREVIOUS DATA###
def mdp_type(tableau_mdp, symboles, majuscules, nombres, minuscules):
    i = 0
    nmb_symbole = nmbsymboles(tableau_mdp)
    nmb_majuscules = maj(tableau_mdp)
    nmb_nombre = nmb(tableau_mdp)
    
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
print(tableau_fini)

res = tableau_fini[0]
for i in range(1, len(tableau_fini) - 1):
    res = res + stringing(tableau_fini, i)

print(res)