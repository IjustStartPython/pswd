password = input("Choisi un mot de passe de plus de 8 caractères :")
if len(password) >= 8:
   print("Mot de passe accepté")
else :
   print("Mot de passe trop petit")
   
#Initialisation des variables

Majuscule_trouvee = False
Chiffre_trouvee = False

# permert de verifier si MAJ et Chiffre en une seule boucle 
for lettre in password:
        if lettre.isupper():
            Majuscule_trouvee = True
        if lettre.isdigit():
            Chiffre_trouvee= True

if Majuscule_trouvee:
    print("Majuscule trouvé")
else:
 print("pas de majuscule")

#trouver un chiffre

if Chiffre_trouvee:
    print("Chiffre trouvee")
else: 
 print("Pas de chiffre")

 # score du mot de passe
score = 0
if len(password) >= 8:
    score +=40
if Majuscule_trouvee :
    score +=30
if Chiffre_trouvee : 
    score +=30
print("Score du mot de passe:", score)

#Refus ou non du mot de passe
 
if score >= 70:
    print("Mot de passe accepté")
else:
    print("Mot de passe refusé")