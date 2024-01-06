class Etudiant:
    def __init__(self, nom, prenom, matricule, notes):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.notes = notes

# Calculer la moyenne d'un étudiant
    def calculer_moyenne(self):
        if not self.notes:
            return 0  # Retourne 0 si l'étudiant n'a pas de notes
        return sum(self.notes) / len(self.notes)


# Création d'une liste d'etudiants
etudiant1 = Etudiant("Ivan", "Junior", "A12345", [80, 90, 75, 85])
etudiant2 = Etudiant("Merline", "Philidor", "B67890", [95, 88, 92, 78])
etudiant3 = Etudiant("Matin", "Pierre", "C54321", [70, 85, 88, 92])

promotion = [etudiant1, etudiant2, etudiant3]

# Afficher les informations sur chaque étudiant
for etudiant in promotion:
    print(f"Nom: {etudiant.nom}, Prénom: {etudiant.prenom}, Matricule: {etudiant.matricule}")

def trouver_etudiant_moyenne_maximale(promotion):
    if not promotion:
        return None  # Retourne None si la liste est vide

    etudiant_max_moyenne = max(promotion, key=lambda etudiant: etudiant.calculer_moyenne())
    return etudiant_max_moyenne

# Trouver l'étudiant ayant la note moyenne maximale
etudiant_max_moyenne = trouver_etudiant_moyenne_maximale(promotion)

# Afficher les informations sur l'étudiant
if etudiant_max_moyenne:
    print(f"L'étudiant avec la moyenne maximale est {etudiant_max_moyenne.prenom} {etudiant_max_moyenne.nom}.")
    print(f"Moyenne : {etudiant_max_moyenne.calculer_moyenne()}")
else:
    print("Aucun étudiant dans la promotion.")