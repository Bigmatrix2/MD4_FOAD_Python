import random  # Pour la sélection de nombres aléatoires

#Etape 1: Définition des variables
combination_len = 4
maximum_try = 10
combination_value = [1, 2, 3, 4, 5, 6]

#Etape 2: Génération de la combinaison secrète
def secret_combination():
    return [random.choice(combination_value) for _ in range(combination_len)]
# Test de la fonction secret_combination
secret_test = secret_combination()
print(f"Combinaison secrète générée (test) : {secret_test}")

#Etape 3: Récupération de la proposition du joueur
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

#Etape 4: Vérification de la proposition du joueur
def verify_proposition(secret_test, choice):
    well_placed = sum(s == c for s, c in zip(secret_test, choice))
    # Comptage des chiffres correctement placés et mal placés
    secret_test_counts = {number: secret_test.count(number) for number in combination_value}
    choice_counts = {number: choice.count(number) for number in combination_value}
    correct_numbers = sum(min(secret_test_counts[number], choice_counts[number]) for number in combination_value)
    misplaced = correct_numbers - well_placed
    return well_placed, misplaced
# Test de la fonction verify_proposition
well_placed, misplaced = verify_proposition(secret_test, player_choice)
print(f"Nombre de Chiffres bien placés : {well_placed}, Nombre de Chiffres mal placés : {misplaced}")




#Etape 5 et 6: Boucle de jeu principale
def game_mastermind():
    print("Bienvenue au jeu des cerveaux!")
    secret = secret_combination()  # Génération de la combinaison secrète
    attempts_left = maximum_try

    while attempts_left > 0:
        print(f"\nTentatives restantes: {attempts_left}")
        # Récupérer la proposition du joueur
        player_guess = get_proposition()  # Appel correct de la fonction
        # Vérification de la proposition
        well_placed, misplaced = verify_proposition(secret, player_guess)
        # Affichage des résultats
        print(f"Chiffres bien placés : {well_placed}")
        print(f"Chiffres mal placés : {misplaced}")
        
        if well_placed == combination_len:
            print("Félicitations, vous avez trouvé la combinaison secrète!")
            return

        attempts_left -= 1

    print(f"\nGame Over! La combinaison secrète était : {''.join(map(str, secret))}")

# Lancer le jeu
if __name__ == "__main__":
    game_mastermind()







