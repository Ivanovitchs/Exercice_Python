def index_minimum(t, d, f):
    # Vérifier que les indices sont valides
    if d < 0 or f >= len(t) or d > f:
        raise ValueError("Indices invalides")

    # Initialiser l'indice du minimum avec la première position dans la plage spécifiée
    indice_minimum = d

    # Parcourir la plage spécifiée pour trouver l'indice du minimum
    for i in range(d + 1, f + 1):

        if t[i] < t[indice_minimum]:
            indice_minimum = i

    # Renvoyer l'indice du minimum
    return indice_minimum

# Exemple d'utilisation
tableau = [5, 2, 8, 1, 4, 6]
indice_min = index_minimum(tableau, 1, 3)
print("L'indice de la plus petite valeur dans la plage spécifiée est :", indice_min)



# Tri à bulle

def tri_bulles(tableau):
    n = len(tableau)

    # Parcourir tous les éléments du tableau
    for i in range(n):
        # Le dernier i éléments sont déjà triés, donc on les ignore
        for j in range(0, n - i - 1):
            # Échanger les éléments s'ils sont dans le mauvais ordre
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

# Exemple d'utilisation
tableau = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(tableau)

print("Tableau trié:", tableau)


#Fonction dichotomatique

def recherche_dichotomique(tableau, element_recherche):
    gauche = 0 
    droite = len(tableau) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        # Vérifier si l'élément se trouve à gauche, à droite ou au milieu
        if tableau[milieu] == element_recherche:
            return milieu  # L'élément a été trouvé, renvoie de son indice
        elif tableau[milieu] < element_recherche:
            gauche = milieu + 1  # L'élément est à droite du milieu
        else:
            droite = milieu - 1  # L'élément est à gauche du milieu

    return -1  # L'élément n'est pas dans le tableau

# Exemple d'utilisation
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_recherche = 7
resultat = recherche_dichotomique(tableau, element_recherche)

if resultat != -1:
    print(f"L'élément {element_recherche} se trouve à l'indice {resultat}.")
else:
    print(f"L'élément {element_recherche} n'est pas dans le tableau.")


#Proposition d'une procédure d'insertion qui ajoute un élement e à sa place dans un tableau.
def insertion(e, t, n):
    # Augmenter la taille du tableau
    n = n + 1

    # Déterminer la position d'insertion de l'élément
    position_insertion = n - 1

    """while position_insertion > 0 and t[position_insertion - 1] > e:
        # Déplacer les éléments plus grands vers la droite
        t[position_insertion] = t[position_insertion - 1]
        position_insertion -= 1"""
  
    t.insert(position_insertion,e)
    
    # Insérer l'élément à sa position correcte




tableau = [1, 3, 5, 7, 9]
taille = len(tableau)
element_insertion = 4

insertion(element_insertion, tableau, taille)

# Exemple d'utilisation

def tri_extraction(t):
    for i in range(len(t)):
        # Trouver l'index du minimum dans la partie non triée du tableau
        min_index = index_minimum(t, i, len(t) - 1)

        # Échanger l'élément minimum avec le premier élément non trié
        t[i], t[min_index] = t[min_index], t[i]

def index_minimum(t, d, f):
    min_index = d

    # Parcourir la plage spécifiée
    for i in range(d + 1, f + 1):
        if t[i] < t[min_index]:
            min_index = i

    return min_index

# Exemple d'utilisation
tableau = [64, 25, 12, 22, 11]
tri_extraction(tableau)
tri_extraction(tableau)
print("Tableau après insertion :", tableau)
print("Tableau trié:", tableau)


def tri_insertion(t):
    for i in range(1, len(t)):
        # Insérer l'élément courant à sa place dans les i-1 premières cases triées
        insertion(t[i], t, i)

def insertion(element, tableau, n):
    j = n - 1
    
    # Déplacer les éléments plus grands que l'élément courant vers la droite
    while j >= 0 and tableau[j] > element:
        tableau[j + 1] = tableau[j]
        j -= 1
    
    # Insérer l'élément à sa place correcte
    tableau[j + 1] = element
tableau = [12, 11, 13, 5, 6]
tri_insertion(tableau)
print("Tableau trié:", tableau)

