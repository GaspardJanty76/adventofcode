# Ouvrir le fichier en mode lecture
with open("dataday1.txt", "r") as file:
    # Lire toutes les lignes du fichier dans une liste
    lines = file.readlines()

# Initialiser les variables pour suivre la somme actuelle et la somme maximale
current_sum = 0
max_sum = 0

# Parcourir chaque ligne des données
for line in lines:
    # Vérifier si la ligne est une ligne vide (indiquant une nouvelle section)
    if line == "\n":
        # Mettre à jour la somme maximale si la somme actuelle est plus grande
        max_sum = max(current_sum, max_sum)
        # Réinitialiser la somme actuelle pour la nouvelle section
        current_sum = 0
    else:
        # Ajouter la valeur entière de la ligne à la somme actuelle
        current_sum += int(line)

# Après la boucle, mettre à jour la somme maximale une dernière fois
max_sum = max(current_sum, max_sum)

# Afficher la somme maximale
print(max_sum)

