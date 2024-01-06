class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        else:
            raise IndexError("La pile est vide")

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]
        else:
            raise IndexError("La pile est vide")

    def taille(self):
        return len(self.elements)


# Exemple d'utilisation de la pile
ma_pile = Pile()
ma_pile.empiler(1)
ma_pile.empiler(2)
ma_pile.empiler(3)

print("Sommet de la pile:", ma_pile.sommet())
print("Taille de la pile:", ma_pile.taille())

while not ma_pile.est_vide():
    print("Dépile:", ma_pile.depiler())






class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        else:
            raise IndexError("La pile est vide")

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]
        else:
            raise IndexError("La pile est vide")

    def taille(self):
        return len(self.elements)

def inverser_pile(pile):
    pile_temporaire = Pile()

    while not pile.est_vide():
        element = pile.depiler()
        pile_temporaire.empiler(element)

    while not pile_temporaire.est_vide():
        element = pile_temporaire.depiler()
        pile.empiler(element)

# Exemple d'utilisation
ma_pile = Pile()
ma_pile.empiler(1)
ma_pile.empiler(2)
ma_pile.empiler(3)

print("Pile avant inversion:", ma_pile.elements)

inverser_pile(ma_pile)

print("Pile après inversion:", ma_pile.elements)



# Fonction 3
def est_symbole_ouvrant(caractere):
    symboles_ouvrants = "({["
    return caractere in symboles_ouvrants

def symbole_fermant_correspondant(symbole_ouvrant):
    correspondances = {"(": ")", "{": "}", "[": "]"}
    return correspondances.get(symbole_ouvrant, None)

def est_expression_bien_parenthesee(expression):
    pile = []

    for caractere in expression:
        if est_symbole_ouvrant(caractere):
            pile.append(caractere)
        else:
            if not pile or caractere != symbole_fermant_correspondant(pile.pop()):
                return False

    return len(pile) == 0

# Exemple d'utilisation
expression_valide = "{[()]}"
expression_invalide = "{[(])}"

resultat_valide = est_expression_bien_parenthesee(expression_valide)
resultat_invalide = est_expression_bien_parenthesee(expression_invalide)

print("Expression valide:", resultat_valide)
print("Expression invalide:", resultat_invalide)


#Fonction 4
def est_operation(caractere):
    operations = "+-*/"
    return caractere in operations

def evaluer_operation(operateur, operand1, operand2):
    if operateur == '+':
        return operand1 + operand2
    elif operateur == '-':
        return operand1 - operand2
    elif operateur == '*':
        return operand1 * operand2
    elif operateur == '/':
        # Vérifier la division par zéro
        if operand2 == 0:
            raise ValueError("Division par zéro")
        return operand1 / operand2

def evaluer_expression_polonaise_inverse(expression):
    pile = []

    for caractere in expression:
        if caractere.isdigit():
            pile.append(int(caractere))
        elif est_operation(caractere):
            operand2 = pile.pop()
            operand1 = pile.pop()
            resultat = evaluer_operation(caractere, operand1, operand2)
            pile.append(resultat)
        else:
            raise ValueError("Caractère invalide dans l'expression")

    if len(pile) == 1:
        return pile[0]
    else:
        raise ValueError("Expression invalide")

# Exemple d'utilisation
expression_polonaise_inverse = "32*5+"

resultat_evaluation = evaluer_expression_polonaise_inverse(expression_polonaise_inverse)

print("Résultat de l'évaluation:", resultat_evaluation)
