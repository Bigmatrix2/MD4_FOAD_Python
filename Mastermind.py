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



