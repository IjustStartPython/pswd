import os #sert à connaitre le dossier courant
import random
import string
import getpass
import time


UTILISATEUR_WINDOWS = getpass.getuser()

#Vérification du fichier de mot de passe________________________________
mot_de_passe = ""
FICHIER_MDP = "mot_de_passe_valides.txt"
os.path.exists(FICHIER_MDP) #verifie si le fichier existe
open(FICHIER_MDP, "a").close() #cree le fichier s'il n'existe pas

#caractères spéciaux autorisés___________________________________________
caractere_specials = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

#lecture de la liste des passes communs_________________________________
try:
    with open("communmdp.txt", "r") as f:
        LISTE_MOTS_COMMUNS = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    LISTE_MOTS_COMMUNS = []

#Definition des fonctions_______________________________________________
def verifier_longueur(mot):
     return len(mot) >= 8

def mot_trop_commun(mot, liste_mots_communs):
    return mot in liste_mots_communs

def verifier_caracteres(mot, caracteres_speciaux):
     maj = any(c.isupper() for c in mot)
     chiffre= any(c.isdigit() for c in mot)
     special = any(c in caracteres_speciaux for c in mot)
     return maj, chiffre, special

def mot_deja_utilise(mot, fichier_path):
    with open(fichier_path, "r") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if not ligne:
                continue
            # On prend seulement la dernière partie après le dernier " | "
            parts = ligne.rsplit(" | ", 1)
            if len(parts) != 2:
                continue
            mot_enregistre = parts[1]
            if mot == mot_enregistre:
                return True
    return False

    
def calculer_score(mot, maj, chiffre, special):
     score = 0
     if len(mot) >=8:
          score +=40
     if maj:
          score +=30
     if chiffre:
          score +=10
     if special:
          score +=20
     return score 

def generer_mot_de_passe(longueur=12):
     while True: 
          mot = [
               random.choice(string.ascii_uppercase),
               random.choice(string.ascii_lowercase),
               random.choice(string.digits),
               random.choice(caractere_specials)
          ]
          tous_les_caracteres = string.ascii_letters + string.digits + caractere_specials
          mot += [random.choice(tous_les_caracteres) for _ in range(longueur -4)]
          random.shuffle(mot)
          mot_final = ''.join(mot)
          maj, chiffre, special = verifier_caracteres(mot_final, caractere_specials)
          if len(mot_final) >=8 and maj and chiffre and special:
               return mot_final

def verifier_mot_de_passe_complet(mot, fichier_path, liste_mots_communs, caractere_specials):
    erreurs = []

    if not verifier_longueur(mot):
        erreurs.append("Mot de passe trop court")
    
    if mot_deja_utilise(mot, fichier_path):
        erreurs.append("Ce mot de passe a déjà été utilisé")

    if mot_trop_commun(mot, liste_mots_communs):
        erreurs.append("Mot de passe trop commun")
    
    maj, chiffre, special = verifier_caracteres(mot, caractere_specials)
    if not maj:
        erreurs.append("Il doit contenir au moins une lettre majuscule")
    if not chiffre:
        erreurs.append("Il doit contenir au moins un chiffre")
    if not special:
        erreurs.append("Il doit contenir au moins un caractère spécial")

    score = calculer_score(mot, maj, chiffre, special)
    if score < 70:
        erreurs.append("Score insuffisant")

    print(f"Score actuel : {score}/100")

    valide = len(erreurs) == 0
    return valide, erreurs


def enregistrer_mot_de_passe(site, utilisateur, mot):
    chemin_absolu = os.path.abspath(FICHIER_MDP)

    with open(FICHIER_MDP, "a") as f:
        f.write(f"{site} | {utilisateur} | {mot}\n")

    print(f"Mot de passe enregistré avec succès pour {utilisateur} sur {site} !")
    print(f"Chemin du fichier : {chemin_absolu}")

def saisir_mot_de_passe(site, utilisateur):
    while True:
        choix = input("Veux-tu générer un mot de passe sécurisé automatiquement ? (o/n) : ").upper()
        if choix == 'O':
            mot_de_passe = generer_mot_de_passe()
            print("Voici un mot de passe sécurisé généré pour toi :", mot_de_passe)
        else:
            mot_de_passe = input("Choisi un mot de passe de plus de 8 caractères :")
        
        valide, erreurs = verifier_mot_de_passe_complet(
            mot_de_passe, FICHIER_MDP, LISTE_MOTS_COMMUNS, caractere_specials
        )
        if valide:
            enregistrer_mot_de_passe(site, utilisateur, mot_de_passe)
            return mot_de_passe
        else:
            print("Mot de passe refusé, réessaye !")
            # Afficher le score même si le mot de passe est refusé
            maj, chiffre, special = verifier_caracteres(mot_de_passe, caractere_specials)
            score = calculer_score(mot_de_passe, maj, chiffre, special)
            print(f"Score du mot de passe : {score}/100\n")

#Boucle principale______________________________________________________

print(f"Bonjour {UTILISATEUR_WINDOWS} !")
print("Bienvenue dans le V1.1.0 du vérificateur de mot de passe")

while True: #Permet d'ajouter plusieurs udentifiants/mots de passe
    site = input("Entrez l'URl du site : ")
    utilisateur = input("Entrer votre nom d'utilisateur : ")

    mot_de_passe = saisir_mot_de_passe(site, utilisateur)

#continuer ou arrêter le programme______________________________________
    continuer = input("Veux-tu ajouter un autre mot de passe ? (o/n) : ").upper()
    if continuer != 'O':
        print("N'hésitez pas a me donner des conseils sur pour m'améliorer !")
        print("Merci d'avoir utilisé le vérificateur de mot de passe ! À bientôt !")
        print("https://github.com/IjustStartPython")
        time.sleep(6)
        break
#_______________________________________________________________________