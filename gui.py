import tkinter as tk
from tkinter import messagebox
import webbrowser
import hashlib

import pswd
from crypto_utils import chiffrer, dechiffrer
from database import init_db, lister_utilisateurs, get_utilisateur, creer_utilisateur, \
    lister_mots_de_passe, ajouter_mot_de_passe, supprimer_mot_de_passe, mot_de_passe_existe

init_db()

# =====================
# Fonctions utilitaires
# =====================

def hash_mdp(master_password):
    return hashlib.sha256(master_password.encode()).hexdigest()

def raccourcir_site(site, max_len=15):
    return site if len(site) <= max_len else site[:max_len] + "..."

def ouvrir_site(event, listbox):
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    site = listbox.urls[index]
    webbrowser.open(site if site.startswith("http") else "https://" + site)

# =====================
# Gestionnaire de mots de passe
# =====================

def ouvrir_gestionnnaire(user_id, username, master_password):
    app = tk.Toplevel()
    app.title(f"Gestionnaire - {username}")

    listbox = tk.Listbox(app, width=80)
    listbox.pack()
    listbox.password_ids = []
    listbox.urls = []

    # ----- Fonctions internes -----

    def charger_liste(filtre=""):
        listbox.delete(0, tk.END)
        listbox.password_ids.clear()
        listbox.urls.clear()
        rows = lister_mots_de_passe(user_id, filtre)
        for pwd_id, site, ident, mdp_chiffre in rows:
            try:
                mdp = dechiffrer(mdp_chiffre, master_password)
            except Exception:
                mdp = "[ERREUR]"
            affichage = f"{raccourcir_site(site):<22} | {ident:<15} | {mdp}"
            listbox.insert(tk.END, affichage)
            listbox.password_ids.append(pwd_id)
            listbox.urls.append(site)

    def ajouter_entry():
        site = entry_site.get().strip()
        ident = entry_ident.get().strip()
        mdp = entry_mdp.get().strip()

        valide, erreurs, _ = pswd.verifier_mot_de_passe(mdp, "")
        if not valide:
            messagebox.showerror("Mot de passe refusé", "\n".join(erreurs))
            return

        mdp_chiffre = chiffrer(mdp, master_password)
        ajouter_mot_de_passe(user_id, site, ident, mdp_chiffre)

        entry_site.delete(0, tk.END)
        entry_ident.delete(0, tk.END)
        entry_mdp.delete(0, tk.END)
        charger_liste(entry_recherche.get())

    def supprimer_entry():
        sel = listbox.curselection()
        if not sel:
            messagebox.showerror("Erreur", "Sélectionne une entrée")
            return
        pwd_id = listbox.password_ids[sel[0]]
        supprimer_mot_de_passe(pwd_id)
        charger_liste(entry_recherche.get())

    def copier_mdp():
        sel = listbox.curselection()
        if not sel:
            return
        index = sel[0]
        rows = lister_mots_de_passe(user_id, filtre="")
        mdp_chiffre = rows[index][3]
        mdp = dechiffrer(mdp_chiffre, master_password)
        app.clipboard_clear()
        app.clipboard_append(mdp)
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier")

    def generer_mdp():
        while True:
            mdp = pswd.generer_mot_de_passe()
            valide, _, _ = pswd.verifier_mot_de_passe(mdp, "")
            if valide and not mot_de_passe_existe(user_id, chiffrer(mdp, master_password)):
                entry_mdp.delete(0, tk.END)
                entry_mdp.insert(0, mdp)
                break

    def toggle_mdp():
        nonlocal mdp_visible
        mdp_visible = not mdp_visible
        entry_mdp.config(show="" if mdp_visible else "*")

    # ----- Widgets -----
    tk.Button(app, text="🗑️ Supprimer l’entrée sélectionnée", command=supprimer_entry).pack()
    tk.Label(app, text="🔍 Rechercher un site :").pack()
    entry_recherche = tk.Entry(app)
    entry_recherche.pack()
    entry_recherche.bind("<KeyRelease>", lambda e: charger_liste(entry_recherche.get()))

    tk.Label(app, text="Site:").pack()
    entry_site = tk.Entry(app)
    entry_site.pack()

    tk.Label(app, text="Identifiant:").pack()
    entry_ident = tk.Entry(app)
    entry_ident.pack()

    tk.Label(app, text="Mot de passe:").pack()
    entry_mdp = tk.Entry(app, show="*")
    entry_mdp.pack()
    mdp_visible = False

    tk.Button(app, text="👁 Afficher / Masquer", command=toggle_mdp).pack()
    tk.Button(app, text="📋 Copier le mot de passe", command=copier_mdp).pack()
    tk.Button(app, text="Générer mot de passe sécurisé", command=generer_mdp).pack()
    tk.Button(app, text="Ajouter", command=ajouter_entry).pack()
    listbox.bind("<Double-Button-1>", lambda e: ouvrir_site(e, listbox))

    charger_liste()

# =====================
# Création d'utilisateur
# =====================

def creer_nouvel_utilisateur():
    def valider_creation():
        username = entry_user.get().strip()
        master_pass = entry_master.get().strip()
        if not username or not master_pass:
            messagebox.showerror("Erreur", "Utilisateur ou mot de passe vide")
            return
        try:
            creer_utilisateur(username, hash_mdp(master_pass))
        except Exception as e:
            messagebox.showerror("Erreur", f"L'utilisateur existe déjà ({e})")
            return
        listbox_users.insert(tk.END, username)
        fenetre.destroy()
        messagebox.showinfo("Succès", f"Utilisateur '{username}' créé avec succès !")

    fenetre = tk.Toplevel(root)
    fenetre.title("Créer un nouvel utilisateur")
    tk.Label(fenetre, text="Nom de l'utilisateur:").pack()
    entry_user = tk.Entry(fenetre)
    entry_user.pack()
    tk.Label(fenetre, text="Mot de passe maître:").pack()
    entry_master = tk.Entry(fenetre, show="*")
    entry_master.pack()
    tk.Button(fenetre, text="Créer", command=valider_creation).pack()

# =====================
# Connexion
# =====================

def connexion():
    sel = listbox_users.curselection()
    if not sel:
        messagebox.showerror("Erreur", "Sélectionne un utilisateur")
        return
    username = listbox_users.get(sel[0])
    master_pass = entry_master_password.get()
    user = get_utilisateur(username)
    if not user:
        messagebox.showerror("Erreur", "Utilisateur inconnu")
        return
    user_id, master_hash = user
    if master_hash != hash_mdp(master_pass):
        messagebox.showerror("Erreur", "Mot de passe incorrect")
        return
    root.withdraw()
    ouvrir_gestionnnaire(user_id, username, master_pass)

# =====================
# Interface principale
# =====================

root = tk.Tk()
root.title("Gestionnaire de mots de passe")
root.iconbitmap(r"C:\Users\Utilisateur\Desktop\vs\icone.ico")
tk.Label(root, text="Utilisateur:").pack()
listbox_users = tk.Listbox(root)
listbox_users.pack()
for u in lister_utilisateurs():
    listbox_users.insert(tk.END, u)

tk.Label(root, text="Mot de passe maître:").pack()
entry_master_password = tk.Entry(root, show="*")
entry_master_password.pack()

tk.Button(root, text="Se connecter", command=connexion).pack()
root.bind("<Return>", lambda e: connexion())
tk.Button(root, text="Nouvel utilisateur", command=creer_nouvel_utilisateur).pack(pady=5)

root.mainloop()
