def main():

    with open("dataday4.txt", "r") as fichier:
        assignationsvalides = 0
        for ligne in fichier:
            assignation1, assignation2 = ligne.split(",")

            (
                prnbrassignation1,
                scnbrassignation1,
            ) = assignation1.split("-")
            (
                prnbrassignation2,
                scnbrassignation2,
            ) = assignation2.split("-")



            if int(scnbrassignation1) >= int(
                prnbrassignation2
            ) and int(prnbrassignation1) <= int(
                scnbrassignation2
            ):
                assignationsvalides += 1
            elif int(scnbrassignation2) >= int(
                prnbrassignation1
            ) and int(prnbrassignation2) <= int(
                scnbrassignation1
            ):
                assignationsvalides += 1

        print(assignationsvalides)


if __name__ == "__main__":
    main()
