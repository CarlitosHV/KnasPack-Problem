import random
import time
import matplotlib.pyplot as plt

random.seed(0)
items = []
for i in range(40):
    name = f"Producto {i+1}"
    weight = random.randint(1, 10)
    value = random.randint(10, 50)
    items.append((name, weight, value))

capacity = 60

def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    evaluation_times = []

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        start_time = time.time()
        for w in range(1, capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        end_time = time.time()
        evaluation_time = end_time - start_time
        evaluation_times.append(evaluation_time)

    selected_items = []
    w, v = capacity, dp[n][capacity]
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, weight, value = items[i - 1]
            selected_items.append((name, weight, value))
            w -= weight

    return v, selected_items, evaluation_times

max_value, selected_items, evaluation_times = knapsack(items, capacity)

weights = [item[1] for item in items]
plt.plot(weights, evaluation_times)
plt.xlabel('Peso (kilogramos)')
plt.ylabel('Tiempo de evaluación (segundos)')
plt.title('Tiempo de evaluación por peso')
plt.xticks(range(1, max(weights) + 1))
plt.show()

print(f"Valor máximo de la mochila: {max_value}")
print("Elementos seleccionados:")
for item in selected_items:
    print(f"{item[0]}, Peso: {item[1]} kg, Valor: {item[2]}")



