import random  # Pour la sélection de nombres aléatoires

# Définition des variables
combination_len = 4
maximum_try = 10
combination_value = [1, 2, 3, 4, 5, 6]

#Etape 1: Génération de la combinaison secrète
def secret_combination():
    return [random.choice(combination_value) for _ in range(combination_len)]

# Test de la fonction secret_combination
secret_test = secret_combination()
print(f"Combinaison secrète générée (test) : {secret_test}")

#Etape 2 : Récupération de la proposition du joueur
def get_proposition():
    while True:
        choice = input(f"Saisissez votre choix ({combination_len} chiffres parmi {', '.join(map(str, combination_value))}): ")
        # Vérification de la longueur et des valeurs
        if len(choice) == combination_len and all(char.isdigit() and int(char) in combination_value for char in choice):
            return [int(char) for char in choice]  # Conversion en liste d'entiers
        else:
            print(f"Saisie invalide. Vérifiez que votre choix est composé de {combination_len} chiffres et utilise seulement ces valeurs : {', '.join(map(str, combination_value))}.")

# Test de la fonction get_proposition
player_choice = get_proposition()
print(f"Choix du joueur : {player_choice}")

