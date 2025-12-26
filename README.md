# Gestionnaire de mots de passe sécurisé V2.0.0

## Projet pour portfolio cybersécurité débutant python

Cette mise à jour marque la fin de la première version en ligne de commande et introduit une version complètement graphique et sécurisée. 

Le programme permet désormais à un utilisateur de : 

- Créer un compte avec mot de passe maître
- Ajouter, gérer et supprimer des mots de passes pour différents sites.
- Générer automatiquement des mots de passe sécurisés.
- Tout est stocké de manière sécurisée dans une base de données SQLite.

### Fonctionnalités
1. Gestion des comptes utilisateurs
    - Création de compte avec mot de passe maître
    - Connexion sécurisée avec vérification du mot de passe maître.
    - Les mots de passe des utilisateurs sont stockés sous forme hachée.

2. Gestion de mots de passe :
    - Ajouter des mots de passe pour différents sites avec identifiant associé.
    - Suppression de mots de passe existants.
    - Affichage et copie sécurisée dans le presse papier.
    - Génération de mots de passe aléatoires robustes.
    - Recherche de sites pour filtrer facilement la liste des mots de passe.

3. Sécurité :
    - Les mots de passe sont chiffrés avec le mot de passe maître avant stockage dans la base SQLite
    - Vérification automatique des critères de sécurité:
        - Longueur minimal de 8 caractères
        - Contient au moins une majuscule, un chiffre et un caractère spécial
        - Score de sécurité minimal
    - Protection contre réutilisation de mots de passe.

4. Interface graphique : 
    - Développé avec Tkinter pour une utilisation intuitive.
    - Affichage clair des mots de passe et informations associées.
    - Icône personnalisée pour l'application une fois transformé en .exe.

 ### Comment l'utiliser 
 1. Clonner le dépôt GitHub ou télécharger le fichier.
 2. Installer les dépendances Python nécessaires :
    - pip install pycryptodome
 3. Lancer le programme avec Python : 
    - python gui.py
 4. Créer un utilisateur ou se connecter avec un mot de passe maître existant.
 5. Ajouter, générer, copier et gérer vos mots de passe via l’interface graphique.

 #### Instalation .EXE
  - Téléchargez le .exe directement depuis [GitHub Releases](https://github.com/IjustStartPython/pswd/releases/tag/FinProjet), ou généré via PyInstaller.
  - Double-cliquer sur l'icône pour lancer le programme.
  - Créer un utilisateur ou se connecter avec le mot de passe maître.
  - L'interface permet de gérer vos mots de passe sans aucune ligne de commande. 

 ### Technologies 
 - Python 3
 - VS code
 - Fichier communmdp.txt (liste de mots de passe communs, un par ligne).
 - Tkinter (interface graphique)
 - SQLite pour la base de données sécurisée
 - PyCryptodome pour le chiffrement des mots de passe

 ### Lien avec la cybersécurité
    Ce projet simule un gestionnaire de mots de passe sécurisé, ce qui est une compétence clé dans la protection des données et la cybersécurité

 ### Amélioration possibles :
 - CSynchronisation avec le cloud pour accès multi-appareils.
 - Notifications pour mot de passe faible ou expiré.
 - Thème sombre pour l’interface graphique.
 - Export/import sécurisé des mots de passe. 

 ## Auteur
 Projet réalisé par IjustStartPython 
 Dans le cadre d'un apprentissage en python / CyberSécurité