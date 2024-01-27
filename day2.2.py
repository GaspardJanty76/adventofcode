from typing import Tuple

# Dictionnaire associant les mains (pierre, papier, ciseaux) à leurs lettres correspondantes (A, B, C)
mains_adversaire = dict(pierre="A", papier="B", ciseaux="C")

# Valeurs pour les résultats des rounds
PERDU = 0
EGALITE = 3
GAGNE = 6

# Lettres correspondant aux résultats des rounds
LETTRE_PERDU = "X"
LETTRE_GAGNE = "Z"
LETTRE_EGALITE = "Y"

# Valeurs associées à chaque type de main
VALEUR_CISEAUX = 3
VALEUR_PIERRE = 1
VALEUR_PAPIER = 2

def obtenir_score_main(resultat: str, main_adversaire: str) -> Tuple[int, int]:
    # Si le résultat est LETTRE_EGALITE, retourner la valeur de la même main
    if resultat == LETTRE_EGALITE:
        if main_adversaire == mains_adversaire["pierre"]:
            return (VALEUR_PIERRE, EGALITE)
        elif main_adversaire == mains_adversaire["papier"]:
            return (VALEUR_PAPIER, EGALITE)
        else:
            return (VALEUR_CISEAUX, EGALITE)

    # Si le résultat est LETTRE_PERDU, retourner la valeur de la main perdante
    if resultat == LETTRE_PERDU:
        if main_adversaire == mains_adversaire["pierre"]:
            return (VALEUR_CISEAUX, PERDU)
        elif main_adversaire == mains_adversaire["papier"]:
            return (VALEUR_PIERRE, PERDU)
        else:
            return (VALEUR_PAPIER, PERDU)

    # Si le résultat n'est ni LETTRE_EGALITE ni LETTRE_PERDU, retourner la valeur de la main gagnante
    if main_adversaire == mains_adversaire["pierre"]:
        return (VALEUR_PAPIER, GAGNE)
    elif main_adversaire == mains_adversaire["papier"]:
        return (VALEUR_CISEAUX, GAGNE)
    else:
        return (VALEUR_PIERRE, GAGNE)

def main():
    # Ouvrir le fichier et récupérer toutes les lignes
    with open("dataday2.txt", "r") as fichier:
        scores = []
        for ligne in fichier:
            choix_adversaire, mon_choix = ligne.split(" ")
            choix_adversaire = choix_adversaire.strip()
            mon_choix = mon_choix.strip()

            # Obtenir les résultats du round et les ajouter à la liste des scores
            resultat = obtenir_score_main(choix_adversaire, mon_choix)
            scores.append(sum(resultat))
        # Afficher la somme totale des scores
        print(sum(scores))

if __name__ == "__main__":
    main()
