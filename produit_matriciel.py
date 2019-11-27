"""Produit matriciel

Demande a l'utilisateur deux matrices et vérifie si le produit matriciel est possible.
Si c'est possible le produit matriciel est effectué et la matrice résultante est renvoyée.

Voici le fonctionnement étape par étape du script :

1) Encodage
2) Vérification
3) Résultat

Attention ce site a besoin du module numpy pour fonctionner

Réalisé dans le cadre des laboratoires d'introduction à la programmation (IE-IR-B1) 
Auteur : Henrotte Alexandre, avec l'aide de monsieur BOURRADA
"""
# SOLUTION --> dans la fonction "encodage_matrice" : itérer les colonnes dans les lignes et non pas les lignes dans les colonnes #

import numpy as np # Permet de trier les matrices

def encodage_matrice(n_lignes, n_colonnes):
    """Convertit la matrice de l'utilisateur en liste"""

    matrice = []
    
    for i in range(n_lignes):
        for z in range(n_colonnes):
            print("Encodez la donnée de la ligne", i + 1 ,"colonne", z + 1, ": ", end="")
            matrice.append(int(input()))
    return matrice

def produit_matriciel_possible(n_colonnes_matrice_1, n_lignes_matrice_2):
    """Vérifie si le produit matriciel est mathématiquement possible"""

    if n_colonnes_matrice_1 == n_lignes_matrice_2:
        return True
    else :
        return False

def produit_ligne_colonne(matrice_1,matrice_2,nombre_element,indice_ligne,indice_colonne):
    """Effectue le produit des lignes de la matrice 1 avec les colonnes de la matrice 2"""

    resultat_produit = 0

    for i in range(nombre_element):
        resultat_produit += matrice_1[nombre_element*indice_ligne+i]*matrice_2[indice_colonne+nombre_element*i]

    return resultat_produit

def matrice_resultante(matrice_1, matrice_2, n_lignes_matrice_1, n_lignes_matrice_2, n_colonnes_matrice_2):
    """Retourne la matrice résultante sous forme de liste"""

    matrice_resultante = []

    for i in range(n_lignes_matrice_1):
        for j in range(n_colonnes_matrice_2):
            resultat_produit = produit_ligne_colonne(matrice_1,matrice_2,n_lignes_matrice_2,i,j) 
            matrice_resultante.append(resultat_produit)

    return matrice_resultante

def main():
    """Demande aux utilisateurs les données nécessaires au script et appelle les fonction pour afficher la matrice résultante"""

    print("----- 1ère matrice -----")
    n_lignes_matrice_1 = int(input("Nombres de lignes : "))
    n_colonnes_matrice_1 = int(input("Nombres de colonnes : "))

    matrice_1 = encodage_matrice(n_lignes_matrice_1, n_colonnes_matrice_1)

    print("----- 2ème matrice -----")
    n_lignes_matrice_2 = int(input("Nombres de lignes : "))
    n_colonnes_matrice_2 = int(input("Nombres de colonnes : "))

    matrice_2 = encodage_matrice(n_lignes_matrice_2, n_colonnes_matrice_2)
    print("------------------------\n")

    if produit_matriciel_possible:
        matrice_final = matrice_resultante(matrice_1, matrice_2, n_lignes_matrice_1, n_lignes_matrice_2, n_colonnes_matrice_2)

        sorted_matrice_1 = np.array_split(matrice_1, n_colonnes_matrice_1)
        sorted_matrice_2 = np.array_split(matrice_2, n_colonnes_matrice_2)
        sorted_matrice_resultante = np.array_split(matrice_final, n_colonnes_matrice_2)

        for i, j, z in zip(sorted_matrice_1, sorted_matrice_2, sorted_matrice_resultante):
            print("%3s %0s %3s %0s  %3s" % (i, "-", j, "------", z))

main()