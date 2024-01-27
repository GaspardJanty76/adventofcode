import os

def priorite(caractere: str) -> int:
    char = ord(caractere)

    if char >= 97:
        return char - 96
    return char - 65 + 27

def main():
    cwd = os.getcwd()
    with open(os.path.join(cwd, "dataday3.txt"), "r") as fichier:

        charsac = list()
        lignes = fichier.readlines()
        for i in range(0, len(lignes), 3):
            chaine = [s.strip() for s in lignes[i : i + 3]]
            compartiment1 = set(chaine[0])
            compartiment2 = set(chaine[1])

            charrecherche = set()
            for char in chaine[2]:
                if char not in charrecherche:
                    prioritee = priorite(char)
                    if char in compartiment1 and char in compartiment2:
                        charsac.append(prioritee)
                    charrecherche.add(char)

        print(sum(charsac))

if __name__ == "__main__":
    main()
