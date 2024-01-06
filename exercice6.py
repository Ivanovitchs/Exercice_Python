
import random

def copie(t):
    # Utilisation de la fonction list() pour créer une copie
    copie_tableau = list(t)  

    # Modification de la copie
    copie_tableau[0] = 99

    return copie_tableau

# Exemple d'utilisation
original = [1, 2, 3, 4, 5]
copie_resultat = copie(original)

# Vérification que la modification de la copie n'altère pas l'original
print("Tableau original:", original)
print("Copie modifiée:", copie_resultat)


def inverse(t):
    # Utilisation de la notation de tranches pour inverser le tableau
    tableau_inverse = t[::-1]

    return tableau_inverse

# Exemple d'utilisation
original = [1, 2, 3, 4, 5]
inverse_resultat = inverse(original)

# Affichage des résultats
print("Tableau original:", original)
print("Tableau inversé:", inverse_resultat)



def tableau_premiers_entiers(n):
    return list(range(1, n+1))

def tableau_premiers_entiers_melanges(n):
    entiers = tableau_premiers_entiers(n)
    random.shuffle(entiers)
    return entiers

def tableau_premiers_entiers_inverses(n):
    return list(range(n, 0, -1))

# Exemples d'utilisation
n = 10

tableau_ordre = tableau_premiers_entiers(n)
tableau_melange = tableau_premiers_entiers_melanges(n)
tableau_inverse = tableau_premiers_entiers_inverses(n)

print("Tableau ordre :", tableau_ordre)
print("Tableau mélangé :", tableau_melange)
print("Tableau inverse :", tableau_inverse)

def ligne_dans_fichier(f, n, t):
    with open(f, 'a') as fichier:
        fichier.write(f"{n}\t{t}\n")

# Exemple d'utilisation
nom_fichier = "exemple.txt"
n_valeur = 42
t_valeur = 3.14

ligne_dans_fichier(nom_fichier, n_valeur, t_valeur)


import time

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def temps_tri_bulles(t):
    copie = t.copy()  # Crée une copie du tableau pour éviter de modifier l'original
    debut = time.time()  # Enregistre le temps de début

    tri_bulles(copie)  # Effectue le tri à bulles sur la copie

    fin = time.time()  # Enregistre le temps de fin
    temps_execution = fin - debut  # Calcule la différence pour obtenir le temps d'exécution
    return temps_execution

# Exemple d'utilisation
tableau_original = [4, 2, 7, 1, 9, 5, 3, 8, 6]
temps_execution_tri = temps_tri_bulles(tableau_original.copy())

print("Tableau original :", tableau_original)
print("Temps d'exécution du tri à bulles :", temps_execution_tri, "secondes")


import random
import time

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def temps_tri_bulles(t):
    debut = time.time()
    tri_bulles(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_melange(nmin, nmax, pas, fois, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\tTemps moyen de tri\n")

        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau_melange = [random.randint(1, 1000) for _ in range(n)]
                temps_total += temps_tri_bulles(tableau_melange.copy())

            temps_moyen = temps_total / fois
            fichier.write(f"{n}\t{temps_moyen}\n")

# Exemple d'utilisation
nmin = 100
nmax = 500
pas = 100
fois = 10
nom_fichier_resultats = "resultats_stats_melange.txt"

stats_melange(nmin, nmax, pas, fois, nom_fichier_resultats)

import time

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def temps_tri_bulles(t):
    debut = time.time()
    tri_bulles(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_ordonne(nmin, nmax, pas, fois, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\tTemps moyen de tri\n")

        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau_ordonne = list(range(1, n + 1))
                temps_total += temps_tri_bulles(tableau_ordonne.copy())

            temps_moyen = temps_total / fois
            fichier.write(f"{n}\t{temps_moyen}\n")

# Exemple d'utilisation
nmin = 100
nmax = 500
pas = 100
fois = 10
nom_fichier_resultats = "resultats_stats_ordonne.txt"

stats_ordonne(nmin, nmax, pas, fois, nom_fichier_resultats)

import time

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def temps_tri_bulles(t):
    debut = time.time()
    tri_bulles(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_inverse(nmin, nmax, pas, fois, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\tTemps moyen de tri\n")

        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau_inverse = list(range(n, 0, -1))
                temps_total += temps_tri_bulles(tableau_inverse.copy())

            temps_moyen = temps_total / fois
            fichier.write(f"{n}\t{temps_moyen}\n")

# Exemple d'utilisation
nmin = 100
nmax = 500
pas = 100
fois = 10
nom_fichier_resultats = "resultats_stats_inverse.txt"

stats_inverse(nmin, nmax, pas, fois, nom_fichier_resultats)


import time

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def temps_tri_bulles(t):
    debut = time.time()
    tri_bulles(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_fichier(nmin, nmax, pas, fois, nom_fichier, fonction_generation_tableau):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\tTemps moyen de tri\n")

        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau = fonction_generation_tableau(n)
                temps_total += temps_tri_bulles(tableau.copy())

            temps_moyen = temps_total / fois
            fichier.write(f"{n}\t{temps_moyen}\n")

def tableau_ordonne(n):
    return list(range(1, n + 1))

def tableau_inverse(n):
    return list(range(n, 0, -1))

def tableau_melange(n):
    import random
    return random.sample(range(1, n + 1), n)

# Générer les fichiers de statistiques
nmin = 100
nmax = 1000
pas = 100
fois = 5

nom_fichier_ordonne = "resultats_stats_ordonne.txt"
nom_fichier_inverse = "resultats_stats_inverse.txt"
nom_fichier_melange = "resultats_stats_melange.txt"

stats_fichier(nmin, nmax, pas, fois, nom_fichier_ordonne, tableau_ordonne)
stats_fichier(nmin, nmax, pas, fois, nom_fichier_inverse, tableau_inverse)
stats_fichier(nmin, nmax, pas, fois, nom_fichier_melange, tableau_melange)




import time
import random

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def tri_insertion(t):
    for i in range(1, len(t)):
        key = t[i]
        j = i - 1
        while j >= 0 and key < t[j]:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key

def tri_selection(t):
    for i in range(len(t)):
        min_index = i
        for j in range(i + 1, len(t)):
            if t[j] < t[min_index]:
                min_index = j
        t[i], t[min_index] = t[min_index], t[i]

def tri_rapide(t):
    if len(t) <= 1:
        return t
    pivot = t[len(t) // 2]
    left = [x for x in t if x < pivot]
    middle = [x for x in t if x == pivot]
    right = [x for x in t if x > pivot]
    return tri_rapide(left) + middle + tri_rapide(right)

def temps_tri(t, methode_tri):
    debut = time.time()
    methode_tri(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_tri(nmin, nmax, pas, fois, nom_fichier, *methodes_tri):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\t")
        for methode_tri in methodes_tri:
            fichier.write(f"Temps moyen de tri ({methode_tri.__name__})\t")
        fichier.write("\n")

        for n in range(nmin, nmax + 1, pas):
            fichier.write(f"{n}\t")
            for methode_tri in methodes_tri:
                temps_total = 0
                for _ in range(fois):
                    tableau = [random.randint(1, 1000) for _ in range(n)]
                    temps_total += temps_tri(tableau.copy(), methode_tri)
                temps_moyen = temps_total / fois
                fichier.write(f"{temps_moyen}\t")
            fichier.write("\n")

# Exemple d'utilisation
nmin = 100
nmax = 500
pas = 100
fois = 5

nom_fichier_resultats = "resultats_stats_tri.txt"

# Appel de la fonction stats_tri avec les méthodes de tri à comparer
stats_tri(nmin, nmax, pas, fois, nom_fichier_resultats, tri_bulles, tri_insertion, tri_selection, tri_rapide)

import time
import random
import statistics

def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

def tri_insertion(t):
    for i in range(1, len(t)):
        key = t[i]
        j = i - 1
        while j >= 0 and key < t[j]:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key

def tri_selection(t):
    for i in range(len(t)):
        min_index = i
        for j in range(i + 1, len(t)):
            if t[j] < t[min_index]:
                min_index = j
        t[i], t[min_index] = t[min_index], t[i]

def tri_rapide(t):
    if len(t) <= 1:
        return t
    pivot = t[len(t) // 2]
    left = [x for x in t if x < pivot]
    middle = [x for x in t if x == pivot]
    right = [x for x in t if x > pivot]
    return tri_rapide(left) + middle + tri_rapide(right)

def temps_tri(t, methode_tri):
    debut = time.time()
    methode_tri(t)
    fin = time.time()
    temps_execution = fin - debut
    return temps_execution

def stats_tri(nmin, nmax, pas, fois, nom_fichier, *methodes_tri):
    with open(nom_fichier, 'w') as fichier:
        fichier.write("Taille du tableau\t")
        for methode_tri in methodes_tri:
            fichier.write(f"Temps moyen de tri ({methode_tri.__name__})\tÉcart-type ({methode_tri.__name__})\t")
        fichier.write("\n")

        for n in range(nmin, nmax + 1, pas):
            fichier.write(f"{n}\t")
            for methode_tri in methodes_tri:
                temps_total = 0
                temps_carres = 0

                for _ in range(fois):
                    tableau = [random.randint(1, 1000) for _ in range(n)]
                    temps = temps_tri(tableau.copy(), methode_tri)
                    temps_total += temps
                    temps_carres += temps ** 2

                temps_moyen = temps_total / fois
                ecart_type = (temps_carres / fois - (temps_moyen ** 2)) ** 0.5
                fichier.write(f"{temps_moyen}\t{ecart_type}\t")
            fichier.write("\n")

# Exemple d'utilisation
nmin = 100
nmax = 500
pas = 100
fois = 5

nom_fichier_resultats = "resultats_stats_tri.txt"

# Appel de la fonction stats_tri avec les méthodes de tri à comparer
stats_tri(nmin, nmax, pas, fois, nom_fichier_resultats, tri_bulles, tri_insertion, tri_selection, tri_rapide)
