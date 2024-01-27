# Ouvrir le fichier en mode lecture
with open("dataday1.txt", "r") as file:
    # Lire toutes les lignes du fichier dans une liste
    lines = file.readlines()

# Initialiser une liste pour stocker les sommes intermédiaires
sums = []
# Initialiser une variable pour suivre la somme actuelle
current_sum = 0

# Parcourir chaque ligne des données
for line in lines:
    # Vérifier si la ligne est une ligne vide (indiquant une nouvelle section)
    if line == "\n":
        # Ajouter la somme actuelle à la liste
        sums.append(current_sum)
        # Réinitialiser la somme actuelle pour la nouvelle section
        current_sum = 0
    else:
        # Ajouter la valeur entière de la ligne à la somme actuelle
        current_sum += int(line)

# Après la boucle, ajouter la dernière somme actuelle à la liste
sums.append(current_sum)

# Trier la liste des sommes et afficher la somme des trois plus grandes
print(sum(sorted(sums)[-3:]))
