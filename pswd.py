import os
import random
import string
import hashlib

CARACTERES_SPECIAUX = string.punctuation


def hash_mot_de_passe(mot: str) -> str:
    return hashlib.sha256(mot.encode()).hexdigest()


def charger_mots_communs(fichier="communmdp.txt") -> list[str]:
    if not os.path.exists(fichier):
        return []
    with open(fichier, "r") as f:
        return [ligne.strip() for ligne in f if ligne.strip()]


LISTE_MOTS_COMMUNS = charger_mots_communs()


# =========================
# Validation mot de passe
# =========================

def verifier_caracteres(mot: str):
    return {
        "maj": any(c.isupper() for c in mot),
        "chiffre": any(c.isdigit() for c in mot),
        "special": any(c in CARACTERES_SPECIAUX for c in mot),
    }


def calculer_score(mot: str, flags: dict) -> int:
    score = 0
    if len(mot) >= 8:
        score += 40
    if flags["maj"]:
        score += 30
    if flags["chiffre"]:
        score += 10
    if flags["special"]:
        score += 20
    return score


def verifier_mot_de_passe(mot: str, fichier_mdp: str):
    erreurs = []

    if len(mot) < 8:
        erreurs.append("Au moins 8 caractères requis")

    if mot.lower() in (m.lower() for m in LISTE_MOTS_COMMUNS):
        erreurs.append("Mot de passe trop commun")

    flags = verifier_caracteres(mot)

    if not flags["maj"]:
        erreurs.append("Une majuscule requise")
    if not flags["chiffre"]:
        erreurs.append("Un chiffre requis")
    if not flags["special"]:
        erreurs.append("Un caractère spécial requis")

    score = calculer_score(mot, flags)
    if score < 70:
        erreurs.append("Score de sécurité insuffisant")

    return len(erreurs) == 0, erreurs, score


# =========================
# Génération
# =========================

def generer_mot_de_passe(longueur: int = 12) -> str:
    caracteres = string.ascii_letters + string.digits + CARACTERES_SPECIAUX

    while True:
        mot = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(CARACTERES_SPECIAUX),
        ]
        mot += random.choices(caracteres, k=longueur - 4)
        random.shuffle(mot)
        mot = "".join(mot)

        valide, _, _ = verifier_mot_de_passe(mot, "")
        if valide:
            return mot
