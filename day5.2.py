import sys
import re


def main():

    with open("dataday5.txt", "r") as fichier:
        compteur = 0
        tableau = []

        for ligne in fichier:
            compteur += 1

            if "move" in ligne:
                motif = re.compile(r"\d+")
                [premier, deuxieme, troisieme] = motif.finditer(ligne)

                qttdeplacer = int(premier.group())
                ideplacerde = int(deuxieme.group()) - 1
                ideplacervers = int(troisieme.group()) - 1

                tableau[ideplacervers] = (
                    tableau[ideplacerde][0:qttdeplacer]
                    + tableau[ideplacervers]
                )
                tableau[ideplacerde] = tableau[ideplacerde][qttdeplacer:]
            elif any(char.isdigit() for char in ligne):
                # ne rien faire
                pass
            else:
                compteur_espaces = 0

                # créer un tableau pour contenir les lettres s'il est vide
                if len(tableau) == 0:
                    longueur_ligne = round(len(ligne) / 4)
                    for _ in range(0, longueur_ligne):
                        tableau.append([])

                for i in range(0, len(ligne), 4):
                    item = ligne[i + 1 : i + 2]
                    if item.isalpha():
                        tableau[compteur_espaces].append(ligne[i + 1 : i + 2])
                    compteur_espaces += 1

        mot = ""
        for sous_tableau in tableau:
            mot += sous_tableau[0]
        print(mot)


if __name__ == "__main__":
    main()
