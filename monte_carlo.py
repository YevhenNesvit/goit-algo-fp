import random


def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}  # Ініціалізуємо словник для зберігання результатів
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  # Кидаємо перший кубик
        dice2 = random.randint(1, 6)  # Кидаємо другий кубик
        total = dice1 + dice2  # Обчислюємо суму чисел
        results[total] += 1  # Збільшуємо лічильник для відповідної суми
    probabilities = {key: value / num_rolls for key, value in results.items()}  # Обчислюємо ймовірності
    return probabilities

def print_probabilities_table(probabilities):
    print("Сума чисел Ймовірність")
    for key, value in probabilities.items():
        print(f"{key:^10} {value*100:>7.2f}%")

# Симулюємо кидки кубиків та обчислюємо ймовірності для 10000 кидків
probabilities = simulate_dice_rolls(1000000)

# Графічне відображення ймовірностей
print_probabilities_table(probabilities)
