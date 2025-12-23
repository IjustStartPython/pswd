# Vérificateur de mot de passe sécurisé V1.1.0
## Projet pour portfolio cybersécurité débutant python

Ce projet est un vérificateur et générateur de mots de passe sécurisés.
Il permet à un utilisateur de :
- Créer des mots de passe robustes
- Vérifier leur sécurité selon plusieurs critères
- Eviter la réutilisation de mots de passe
- Enregistrer les mots de passe validés dans un fichier local
- Le programme fonctionne en ligne de commande et peut être transformé en exécutable (.exe) pour Windows.
### Fonctionnalités
1. Vérification du mot de passe :
- Longueur minimale : 8 caractères.
- Doit contenir au moins une majuscule, un chiffre et un caractère spécial.
- Score de sécurité basé sur ces critères (max 100 points).
- Vérifie si le mot de passe est trop commun ou déjà utilisé.
- Possibilité d'ajouter plusieurs comptes
- Delais de 6 secondes avant la fermeture du programme

2. Génération automatique de mots de passe :
- Peut générer un mot de passe aléatoire de 12 caractères (modifiable).
- Garantit au moins une majuscule, un chiffre et un caractère spécial.

3. Enregistrement sécurisé :
- Les mots de passe valides sont stockés dans un fichier texte avec le site et l’utilisateur :
site | utilisateur | mot_de_passe
- Affiche le chemin complet du fichier

 ### Comment l'utiliser 
 1. Clonner le dépôt GitHub ou télécharger le fichier.
 2. Ouvrir le fichier 'psdw.py' dans VS Code.
 3. Exécuter le programme.
 4. Saisir un mot de passe pour tester sa sécurité. 

 ### Technologies 
 - Python 3
 - VS code
 - Fichier communmdp.txt (liste de mots de passe communs, un par ligne).
 - Permissions d’écriture pour créer/ouvrir mot_de_passe_valides.txt.

 ### Lien avec la cybersécurité
 Ce programme simule un contrôle de sécurité des mots de passe, ce qui est une compétence clé pour un futur étudiant dans ce domaine comme moi.

 ### Amélioration possibles :
 - Chiffrement des mots de passe
 - Enregistrement automatique dans un le dosssier documents
 - Interface graphique (Tkinter)
 - Gestion des comptes existants
 - Mot de passe maître 

 ## Auteur
 Projet réalisé par IjustStartPython 
 Dans le cadre d'un apprentissage en python / CyberSécurité