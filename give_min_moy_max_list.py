import statistics

### Définition de la fonction ###

def MinMoyMax(liste):
    print("\n-----------------------")
    print(" Le minimum est : " , min(liste))
    print(" La moyenne est : " , statistics.median(liste))
    print(" Le maximum est : " , max(liste))
    print("\n(", min(liste) , "; " , end ='')
    print(statistics.median(liste) , "; " , end = '')
    print(max(liste) , ")")
    print("-----------------------")
    pass

### Utilisation de la fonction ###

MinMoyMax([-1, 2, 3.5, 6, 10, 18, 35])