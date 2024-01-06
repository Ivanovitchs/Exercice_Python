class Entier:
    def __init__(self, valeur=0):
        self.valeur = int(valeur)

    def additionner(self, autre_entier):
        if isinstance(autre_entier, Entier):
            return Entier(self.valeur + autre_entier.valeur)
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def soustraire(self, autre_entier):
        if isinstance(autre_entier, Entier):
            return Entier(self.valeur - autre_entier.valeur)
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def multiplier(self, autre_entier):
        if isinstance(autre_entier, Entier):
            return Entier(self.valeur * autre_entier.valeur)
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def diviser(self, autre_entier):
        if isinstance(autre_entier, Entier):
            if autre_entier.valeur != 0:
                return Entier(self.valeur // autre_entier.valeur)
            else:
                raise ValueError("La division par zéro est interdite.")
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def afficher(self):
        print(self.valeur)

# Exemple d'utilisation
entier1 = Entier(5)
entier2 = Entier(3)

resultat_addition = entier1.additionner(entier2)
resultat_soustraction = entier1.soustraire(entier2)
resultat_multiplication = entier1.multiplier(entier2)
resultat_division = entier1.diviser(entier2)

print("Addition :")
resultat_addition.afficher()

print("Soustraction :")
resultat_soustraction.afficher()

print("Multiplication :")
resultat_multiplication.afficher()

print("Division :")
resultat_division.afficher()

#Class abstrait avec les listes

class Entier:
    def __init__(self, valeur=0):
        self.chiffres = [int(chiffre) for chiffre in str(abs(valeur))]
        self.chiffres.reverse()  # Pour que le chiffre le moins significatif soit à la fin

    def additionner(self, autre_entier):
        if isinstance(autre_entier, Entier):
            resultat = Entier()
            taille_max = max(len(self.chiffres), len(autre_entier.chiffres))
            retenue = 0

            for i in range(taille_max):
                chiffre1 = self.chiffres[i] if i < len(self.chiffres) else 0
                chiffre2 = autre_entier.chiffres[i] if i < len(autre_entier.chiffres) else 0

                somme = chiffre1 + chiffre2 + retenue
                retenue = somme // 10
                resultat.chiffres.append(somme % 10)

            if retenue:
                resultat.chiffres.append(retenue)

            return resultat
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def multiplier_par_chiffre(self, chiffre):
        resultat = Entier()
        retenue = 0

        for i in range(len(self.chiffres)):
            produit = self.chiffres[i] * chiffre + retenue
            retenue = produit // 10
            resultat.chiffres.append(produit % 10)

        if retenue:
            resultat.chiffres.append(retenue)

        return resultat

    def multiplier(self, autre_entier):
        if isinstance(autre_entier, Entier):
            resultat = Entier()

            for i in range(len(autre_entier.chiffres)):
                chiffre = autre_entier.chiffres[i]
                partie_produit = self.multiplier_par_chiffre(chiffre)
                partie_produit.chiffres = [0] * i + partie_produit.chiffres
                resultat = resultat.additionner(partie_produit)

            return resultat
        else:
            raise TypeError("L'argument doit être un objet de type Entier.")

    def afficher(self):
        chiffres_str = ''.join(map(str, reversed(self.chiffres)))
        print(int(chiffres_str))

# Exemple d'utilisation
entier1 = Entier(123)
entier2 = Entier(456)

# Opération d'addition
resultat_addition = entier1.additionner(entier2)
print("Addition :")
resultat_addition.afficher()

# Opération de multiplication
resultat_multiplication = entier1.multiplier(entier2)
print("Multiplication :")
resultat_multiplication.afficher()


