"""
Ce fichier contient le jeu du pendu.
Il s'appuie sur les fichiers :
- donnees.py
- fonctions.py
"""

from donnees import *
from fonctions import *

# On récupère les scores de la partie
scores = recupscores()

# On récupère un nom d'utilisateur
utilisateur = recupnomutilisateur()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0  # 0 point pour commencer

# Notre variable pour savoir quand arrêter la partie
continuerpartie = 'o'

while continuerpartie != 'n':
    print("Joueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    motatrouver = choisirmot()
    lettrestrouvees = []
    mottrouve = recupmotmasque(motatrouver, lettrestrouvees)
    nbchances = nbcoups

    while motatrouver != mottrouve and nbchances > 0:
        print("Mot à trouver {0} (encore {1} chances)".format(mottrouve, nbchances))
        lettre = recuplettre()
        if lettre in lettrestrouvees:
            # La lettre a déjà été choisie
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in motatrouver:
            # La lettre est dans le mot à trouver
            lettrestrouvees.append(lettre)
            print("Bien joué.")
        else:
            nbchances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")

        mottrouve = recupmotmasque(motatrouver, lettrestrouvees)

    # A-t-on trouvé le mot ou nos chances sont-elles épuisées ?
    if motatrouver == mottrouve:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(motatrouver))
    else:
        print("PENDU !!! Vous avez perdu.")

    # On met à jour le score de l'utilisateur
    scores[utilisateur] += nbchances

    # Demande de continuer la partie
    continuerpartie = input("Souhaitez-vous continuer la partie (O/N) ? ").lower()

# La partie est finie, on enregistre les scores
enregistrerscores(scores)

# On affiche les scores de l'utilisateur
print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))
