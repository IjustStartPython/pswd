import os #sert à connaitre le dossier courant
password = ""
os.path.exists("mdp_valides.txt") #verifie si le fichier existe
open("mdp_valides.txt", "a").close() #cree le fichier s'il n'existe pas
with open ("mdp_valides.txt", "r") as fichier:
     contenu = fichier.readlines()
                    #verificiation du mot de passe dans le fichier
if password + "\n" in contenu:
    print("Ce mot de passe a déjà été utilisé, choisis en un autre")
else:
    print("Mot de passe inédit")

#caracteres speciaux
caractere_specials = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
#liste de mots de passe interits
mots = ["password", "12345678", "qwerty", "letmein", "admin", "welcome", "monkey", "abc123", "football", "iloveyou", "starwars"]

mot_valide = False

while not mot_valide:

    password = input("Choisi un mot de passe de plus de 8 caractères :")
    if len(password) >= 8:
        print("Longueur correcte")
    else:
        print("Longueur insuffisante, il faut au moins 8 caractères")

    if password in mots:
        print("Je te conseil de changer de mot de passe il est trop commun")
    else:
        print("C'est beaucoup mieux !")

    
        

        #Initialisation des variables
    Majuscule_trouvee = False
    Chiffre_trouvee = False
    Special_trouvee = False

        # permert de verifier si MAJ et Chiffre en une seule boucle 
    for lettre in password:
        if lettre.isupper():
            Majuscule_trouvee = True
        if lettre.isdigit():
            Chiffre_trouvee= True
        if lettre in caractere_specials:
            Special_trouvee = True

        #trouver une majuscule
    if Majuscule_trouvee:
        print("Majuscule trouvé")
    else:
        continue

        #trouver un chiffre
    if Chiffre_trouvee:
        print("Chiffre trouvee")
    else: 
        continue

        #trouver un caractere special
    if Special_trouvee:
        print("Caractère special trouvée")
    else: 
        continue

        # score du mot de passe
    score = 0
    if len(password) >= 8:
            score +=40
    if Majuscule_trouvee :
            score +=30
    if Chiffre_trouvee : 
            score +=10
    if Special_trouvee : 
            score +=20
    print("Score du mot de passe:", score)

    if score >=70 and Majuscule_trouvee and Chiffre_trouvee and Special_trouvee:
        print("Tu peut utiliser ce mot de passe, il est enregistrer dans :", os.getcwd() + "/mdp_valides.txt") 
        with open ("mdp_valides.txt", "a") as fichier:
             fichier.write(password + "\n")
        mot_valide = True
    else:
        print("Mot de passe refusé, réessaye !")