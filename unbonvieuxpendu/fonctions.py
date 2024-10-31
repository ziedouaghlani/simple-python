"""
Ce fichier définit des fonctions utiles pour le programme pendu.
On utilise les données du programme contenues dans donnees.py
"""

import os
import pickle
from random import choice
from donnees import *

# Gestion des scores
def recupscores():
    """
    Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire,
    soit l'objet dépicklé, soit un dictionnaire vide.
    On s'appuie sur nomfichierscores défini dans donnees.py
    """
    if os.path.exists(nomfichierscores):
        # Le fichier existe
        with open(nomfichierscores, 'rb') as fichierscores:
            mondepickler = pickle.Unpickler(fichierscores)
            scores = mondepickler.load()
    else:
        # Le fichier n'existe pas
        scores = {}
    return scores

def enregistrerscores(scores):
    """
    Cette fonction se charge d'enregistrer les scores dans le fichier nomfichierscores.
    Elle reçoit en paramètre le dictionnaire des scores à enregistrer
    """
    with open(nomfichierscores, 'wb') as fichierscores:
        monpickler = pickle.Pickler(fichierscores)
        monpickler.dump(scores)

# Fonctions gérant les éléments saisis par l'utilisateur
def recupnomutilisateur():
    """
    Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.
    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau
    """
    nomutilisateur = input("Tapez votre nom: ").capitalize()
    if not nomutilisateur.isalnum() or len(nomutilisateur) < 4:
        print("Ce nom est invalide.")
        return recupnomutilisateur()
    return nomutilisateur

def recuplettre():
    """
    Cette fonction récupère une lettre saisie par l'utilisateur.
    Si la chaîne récupérée n'est pas une lettre,
    on appelle récursivement la fonction jusqu'à obtenir une lettre
    """
    lettre = input("Tapez une lettre: ").lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recuplettre()
    return lettre

# Fonctions du jeu de pendu
def choisirmot():
    """
    Cette fonction renvoie le mot choisi dans la liste des mots listemots.
    On utilise la fonction choice du module random (voir l'aide).
    """
    return choice(listemots)

def recupmotmasque(motcomplet, lettrestrouvees):
    """
    Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)
    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées.
    """
    motmasque = ""
    for lettre in motcomplet:
        if lettre in lettrestrouvees:
            motmasque += lettre
        else:
            motmasque += "*"
    return motmasque
