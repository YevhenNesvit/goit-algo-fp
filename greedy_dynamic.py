def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            total_cost += info['cost']
            total_calories += info['calories']
            chosen_items.append(item)

    return total_calories, chosen_items


def dynamic_max_calories(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if items[i - 1]['cost'] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]['cost']] + items[i - 1]['calories'])

    max_calories = dp[n][budget]
    chosen_items = []
    j = budget

    for i in range(n, 0, -1):
        if max_calories <= 0:
            break
        if max_calories == dp[i - 1][j]:
            continue
        else:
            chosen_items.append(list(items.keys())[i - 1])
            max_calories -= items[list(items.keys())[i - 1]]['calories']
            j -= items[list(items.keys())[i - 1]]['cost']

    return dp[n][budget], chosen_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 50
max_calories, chosen_items = greedy_algorithm(items, budget)

print("Greedy Max Calories:", max_calories)
print("Greedy Chosen Items:", chosen_items)

print("Dynamic Max Calories:", max_calories)
print("Dynamic Chosen Items:", chosen_items)
