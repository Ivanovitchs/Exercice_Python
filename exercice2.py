import random
import time

tableau = [2,5,10,2,1,4]
j=0
n=0
for i in tableau:
   moyenne =+ j+i/len(tableau)


print("la moyenne de ce tableau est : " ,moyenne) 
nombre_entier = int(input("Veuillez entrer un nombre entier à rechercher : "))
taille_tableau = int(input("Veuillez entrer la taille du tableau : "))
tableau2 = [random.randint(1, 100) for _ in range(taille_tableau)]

# Fonction pour calculer la moyenne d'une liste
def calculer_moyenne(lst):
    return sum(lst) / len(lst)

# Fonction pour rechercher un élément dans une liste
def rechercher_element(lst, element):
    return element in lst


# Mesurer le temps nécessaire pour calculer la moyenne
debut_calcul_moyenne = time.time()
resultat_moyenne = calculer_moyenne(tableau2)
fin_calcul_moyenne = time.time()
temps_calcul_moyenne = fin_calcul_moyenne - debut_calcul_moyenne 

# Mesurer le temps pour rechercher un élément dans une liste
debut_rechercher_element_liste = time.time()
resultat_element = rechercher_element(tableau2, nombre_entier)
fin_rechercher_element_liste = time.time()
temps_recherche_element = fin_rechercher_element_liste - debut_rechercher_element_liste 

for i in tableau:

    print("le nombre d'occurence de " + str(i) +  " est : " , str(tableau.count(i)))
    if i>=10:
        n =+1


       

print("le nombre d'élément suppérieur ou égale à 10 est : ", n )
print("la valeur maximale du tableau est : ",  max(tableau))
if nombre_entier in tableau:
    print("Ce nombre existe dans le tableau")
else :
    print("ce nombre n'existe pas dans le tableau")
print("Tableau d'entiers aléatoires :", tableau2)
print("Le temps nécessaire pour calculer la moyenne est :", temps_calcul_moyenne)
print("Le temps nécessaire pour rechercher un élement dans un tableau :", temps_recherche_element)

