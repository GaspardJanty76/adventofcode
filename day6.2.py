import sys


def main():


    with open("dataday6.txt", "r") as fichier:
        chars = []
        for ligne in fichier:
            for i in range(0, len(ligne)):

                chars.append(ligne[i])
                if len(chars) >= 15:
                    del chars[0]

                chars_uniques = list(set(chars))

                if len(chars_uniques) == 14:
                    print("index: ", i + 1)
                    break


if __name__ == "__main__":
    main()
