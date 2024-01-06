def chiffrement_lettre(lettre, correspondances):
    # Vérifier si la lettre existe dans le dictionnaire
    if lettre in correspondances:
        return correspondances[lettre]
    else:
        # Si la correspondance n'existe pas, renvoyer la lettre elle-même
        return lettre

# Exemple d'utilisation
correspondances = {'a': 'x', 'b': 'y', 'c': 'z'}

lettre_chiffree = chiffrement_lettre('a', correspondances)
print("Lettre chiffrée :", lettre_chiffree)  # Renvoie 'x'

lettre_chiffree_inexistante = chiffrement_lettre('d', correspondances)
print("Lettre chiffrée :", lettre_chiffree_inexistante)  # Renvoie 'd' (lettre elle-même)




def chiffrement_phrase(phrase, correspondances):
    phrase_chiffree = ""
    for caractere in phrase:
        lettre_chiffree = chiffrement_lettre(caractere, correspondances)
        phrase_chiffree += lettre_chiffree
    return phrase_chiffree

# Fonction chiffrement_lettre définie précédemment
def chiffrement_lettre(lettre, correspondances):
    if lettre in correspondances:
        return correspondances[lettre]
    else:
        return lettre

# Exemple de dictionnaire de correspondances
dictionnaire_correspondances = {'a': 'x', 'b': 'y', 'c': 'z', ' ': ' '}

# Phrase à chiffrer
phrase_a_chiffrer = "bonjour le monde"

# Chiffrer la phrase en utilisant le dictionnaire de correspondances
phrase_chiffree = chiffrement_phrase(phrase_a_chiffrer, dictionnaire_correspondances)

# Afficher les résultats
print("Phrase à chiffrer :", phrase_a_chiffrer)
print("Phrase chiffrée  :", phrase_chiffree)



def inverse_dico(dictionnaire):
    return {v: k for k, v in dictionnaire.items()}

# Exemple de dictionnaire de correspondances
dictionnaire_correspondances = {'a': 'x', 'b': 'y', 'c': 'z', ' ': ' '}

# Inverser le dictionnaire de correspondances
dictionnaire_inverse = inverse_dico(dictionnaire_correspondances)

# Phrase à déchiffrer
phrase_a_dechiffrer = "xypmtr xli tstlmr"

# Déchiffrer la phrase en utilisant le dictionnaire inversé
phrase_dechiffree = chiffrement_phrase(phrase_a_dechiffrer, dictionnaire_inverse)

# Afficher les résultats
print("Phrase à déchiffrer :", phrase_a_dechiffrer)
print("Phrase déchiffrée   :", phrase_dechiffree)




def dico_rot_13():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    correspondances = {}
    
    for char in alphabet:
        index = (alphabet.index(char) + 13) % 26
        correspondances[char] = alphabet[index]
        correspondances[char.upper()] = alphabet[index].upper()
    
    return correspondances

# Exemple de dictionnaire ROT13
dictionnaire_rot_13 = dico_rot_13()

# Phrase à chiffrer en utilisant ROT13
phrase_a_chiffrer_rot13 = chiffrement_phrase("Hello, World!", dictionnaire_rot_13)

# Afficher les résultats
print("Phrase à chiffrer (ROT13) :", phrase_a_chiffrer_rot13)

phrase_dechiffree_rot13 = chiffrement_phrase(phrase_a_chiffrer_rot13, dictionnaire_rot_13)
print("Phrase déchiffrée (ROT13) :", phrase_dechiffree_rot13)




def compte_lettres(phrase):
    occurrences = {}
    
    for caractere in phrase:
        if caractere.isalpha():  # Ignorer les caractères non alphabétiques
            caractere = caractere.lower()  # Convertir en minuscule pour considérer la casse
            occurrences[caractere] = occurrences.get(caractere, 0) + 1
    
    return occurrences

# Exemple d'utilisation sur un texte mystère
texte_mystere = "Bienvenue dans le monde mystérieux des codes et des chiffres secrets."

# Compter les occurrences de chaque lettre
occurrences_lettres = compte_lettres(texte_mystere)

# Afficher les résultats
print("Occurrences des lettres dans le texte mystère:")
for lettre, occurrence in occurrences_lettres.items():
    print(f"{lettre}: {occurrence}")


def tri_bulles_dico(dictionnaire):
    cles = list(dictionnaire.keys())
    n = len(cles)

    for i in range(n):
        for j in range(0, n - i - 1):
            if dictionnaire[cles[j]] < dictionnaire[cles[j + 1]]:
                cles[j], cles[j + 1] = cles[j + 1], cles[j]

    return cles

# Utilisation sur le dictionnaire précédemment calculé par compte_lettres
texte_mystere = "Bienvenue dans le monde mystérieux des codes et des chiffres secrets."
occurrences_lettres = compte_lettres(texte_mystere)

# Trier les lettres par occurrences décroissantes
cles_triees = tri_bulles_dico(occurrences_lettres)

# Afficher les résultats
print("Lettres triées par occurrences décroissantes:")
for lettre in cles_triees:
    print(f"{lettre}: {occurrences_lettres[lettre]}")




def arrays2dict(ks, vs):
    return dict(zip(ks, vs))

# Tableau fourni par tri_bulles_dico
cles_triees_occurrences = tri_bulles_dico(occurrences_lettres)

# Tableau des lettres de l'alphabet classées par fréquences décroissantes dans la langue française
lettres_alphabet_freq_desc = ['e', 'a', 's', 'i', 'n', 'r', 'u', 'l', 'o', 't', 'd', 'c', 'p', 'm', 'v', 'q', 'g', 'f', 'b', 'h', 'x', 'j', 'y', 'z', 'k', 'w']

# Utilisation de la fonction pour combiner les deux tableaux en un dictionnaire
dictionnaire_combine = arrays2dict(cles_triees_occurrences, lettres_alphabet_freq_desc)

# Afficher les résultats
print("Dictionnaire combiné:")
for cle, valeur in dictionnaire_combine.items():
    print(f"{cle}: {valeur}")


def decrypte(phrase_chiffree, lettres_alphabet_freq_desc):
    correspondances_chiffre_lettre = arrays2dict(range(26), lettres_alphabet_freq_desc)

    phrase_decryptee = ""
    for caractere in phrase_chiffree:
        if caractere.isalpha():
            caractere = caractere.lower()
            if caractere in correspondances_chiffre_lettre.values():
                lettre_decryptee = [lettre for lettre, chiffre in correspondances_chiffre_lettre.items() if chiffre == caractere][0]
                phrase_decryptee = str(phrase_decryptee + lettre_decryptee)
            else:
                phrase_decryptee =  str(phrase_decryptee + caractere)
        else:
            phrase_decryptee = str(phrase_decryptee + caractere)

    return phrase_decryptee

# Texte mystère
texte_mystere = "Wrairhavir qnfv yr zraqre zryivrerhkrf qr fnffnvpur q'rfpre."
texte_mystere_decrypte = decrypte(str(texte_mystere), str(lettres_alphabet_freq_desc))

# Afficher les résultats
print("Texte mystère chiffré :")
print(texte_mystere)
print("\nTexte mystère déchiffré :")
print(texte_mystere_decrypte)


