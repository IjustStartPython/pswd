import sqlite3
from pathlib import Path

DB_PATH = Path("password_manager.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

# =====================
# Initialisation de la DB
# =====================
def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                master_hash TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                site TEXT NOT NULL,
                identifiant TEXT NOT NULL,
                password_chiffre TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.commit()

# =====================
# Utilisateurs
# =====================
def lister_utilisateurs():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users ORDER BY username")
        return [row[0] for row in cursor.fetchall()]

def get_utilisateur(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, master_hash FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row  # None si l'utilisateur n'existe pas

def creer_utilisateur(username, master_hash):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, master_hash) VALUES (?, ?)", (username, master_hash))
        conn.commit()

# =====================
# Mots de passe
# =====================
def lister_mots_de_passe(user_id, filtre=""):
    filtre = f"%{filtre}%"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, site, identifiant, password_chiffre
            FROM passwords
            WHERE user_id = ? AND site LIKE ?
            ORDER BY site
        """, (user_id, filtre))
        return cursor.fetchall()

def ajouter_mot_de_passe(user_id, site, identifiant, password_chiffre):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO passwords (user_id, site, identifiant, password_chiffre)
            VALUES (?, ?, ?, ?)
        """, (user_id, site, identifiant, password_chiffre))
        conn.commit()

def supprimer_mot_de_passe(password_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
        conn.commit()

def mot_de_passe_existe(user_id, password_chiffre):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 1 FROM passwords WHERE user_id = ? AND password_chiffre = ?
        """, (user_id, password_chiffre))
        return cursor.fetchone() is not None
