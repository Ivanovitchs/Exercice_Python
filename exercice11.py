class Etudiant:
    def __init__(self, nom, prenom, annee_naissance, note_informatique, note_mathematiques):
        self.nom = nom
        self.prenom = prenom
        self.annee_naissance = annee_naissance
        self.note_informatique = note_informatique
        self.note_mathematiques = note_mathematiques

    def afficher_informations(self):
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Année de naissance: {self.annee_naissance}")
        print(f"Note en Informatique: {self.note_informatique}")
        print(f"Note en Mathématiques: {self.note_mathematiques}")

# Exemple d'utilisation
etudiant1 = Etudiant("Dupont", "Jean", 1995, 80, 90)
etudiant2 = Etudiant("Martin", "Alice", 1998, 75, 85)

# Affichage des informations des étudiants
print("Informations de l'étudiant 1:")
etudiant1.afficher_informations()

print("\nInformations de l'étudiant 2:")
etudiant2.afficher_informations()


#Création de quelques étudiants 

# Création d'étudiants
etudiant1 = Etudiant("Dupont", "Jean", 1995, 80, 90)
etudiant2 = Etudiant("Martin", "Alice", 1998, 75, 85)
etudiant3 = Etudiant("Dubois", "Paul", 1997, 85, 88)

# Affichage des informations des étudiants
print("Informations de l'étudiant 1:")
etudiant1.afficher_informations()

print("\nInformations de l'étudiant 2:")
etudiant2.afficher_informations()

print("\nInformations de l'étudiant 3:")
etudiant3.afficher_informations()

