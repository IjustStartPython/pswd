from cryptography.fernet import Fernet
import base64
import hashlib

def generer_cle(master_password):
    hash = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hash)

def chiffrer(mdp, master_password):
    f = Fernet(generer_cle(master_password))
    return f.encrypt(mdp.encode()).decode()

def dechiffrer(mdp_chiffre, master_password):
    f = Fernet(generer_cle(master_password))
    return f.decrypt(mdp_chiffre.encode()).decode()
