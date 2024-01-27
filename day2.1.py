# Valeurs pour les résultats des rounds
PERDU = 0
EGALITE = 3
GAGNE = 6

# Fonction pour obtenir le score d'une main
def score(main: str) -> int:
    # Utiliser un dictionnaire pour mapper les mains à leurs scores
    scores = {"X": 1, "Y": 2, "Z": 3}
    return scores.get(main, 0)

# Fonction pour obtenir le vainqueur d'un round
def vainqueur(choix_adversaire: str, mon_choix: str) -> int:
    # Utiliser un dictionnaire pour déterminer le vainqueur de chaque round
    resultats = {
        ("A", "X"): EGALITE,
        ("A", "Y"): GAGNE,
        ("A", "Z"): PERDU,
        ("B", "X"): PERDU,
        ("B", "Y"): EGALITE,
        ("B", "Z"): GAGNE,
        ("C", "X"): GAGNE,
        ("C", "Y"): PERDU,
        ("C", "Z"): EGALITE,
    }
    return resultats.get((choix_adversaire, mon_choix), 0)

# Programme principal
scores = []

# Utiliser le gestionnaire de contexte pour ouvrir le fichier
with open("dataday2.txt", "r") as fichier:
    for ligne in fichier:
        choix_adversaire, mon_choix = ligne.split()
        score1 = vainqueur(choix_adversaire.strip(), mon_choix.strip())
        score2 = score(mon_choix.strip())
        scores.append(score1 + score2)

# Utiliser la fonction sum() pour calculer la somme des scores
score_total = sum(scores)
print(score_total)
