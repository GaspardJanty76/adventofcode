def priorite(caractere: str) -> int:
    char = ord(caractere)

    if char >= 97: 
        return char - 96
    return char - 65 + 27


def main():

    with open("dataday3.txt", "r") as fichier:

        charsac = list()
        for ligne in fichier:
            ligne = ligne.strip()
            moitie = len(ligne) // 2
            compartiment1 = ligne[:moitie]
            compartiment2 = ligne[moitie:]

            charcompartiment1 = set(compartiment1)

            charrecherche = set()
            for char in compartiment2:
                if char not in charrecherche:
                    prioritee = priorite(char)
                    if char in charcompartiment1:
                        charsac.append(prioritee)
                    charrecherche.add(char)

        print(sum(charsac))


if __name__ == "__main__":
    main()
