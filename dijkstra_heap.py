import networkx as nx
import matplotlib.pyplot as plt
import heapq


# Створення графу
metro_network = nx.Graph(name="Харківський метрополітен")

# Додавання ребер (дружба між людьми)
metro_network.add_edge("Холодна гора", "Південний вокзал", weight=2.52)
metro_network.add_edge("Південний вокзал", "Центральний ринок", weight=1.3)
metro_network.add_edge("Центральний ринок", "Майдан конституції", weight=0.93)
metro_network.add_edge("Майдан конституції", "Проспект Гагаріна", weight=1.96)
metro_network.add_edge("Проспект Гагаріна", "Спортивна", weight=1.8)
metro_network.add_edge("Спортивна", "Завод Малишева", weight=1.85)
metro_network.add_edge("Завод Малишева", "Турбоатом", weight=1.65)
metro_network.add_edge("Турбоатом", "Палац спорту", weight=1.65)
metro_network.add_edge("Палац спорту", "Армійська", weight=1.86)
metro_network.add_edge("Армійська", "Масельського", weight=1.47)
metro_network.add_edge("Масельського", "Тракторний завод", weight=1.68)
metro_network.add_edge("Тракторний завод", "Індустріальна", weight=2.21)
metro_network.add_edge("Майдан конституції", "Історичний музей", weight=0.16)
metro_network.add_edge("Історичний музей", "Університет", weight=1.79)
metro_network.add_edge("Університет", "Пушкінська", weight=1.26)
metro_network.add_edge("Пушкінська", "Київська", weight=1.96)
metro_network.add_edge("Київська", "Академіка Барабашова", weight=2.76)
metro_network.add_edge("Академіка Барабашова", "Академіка павлова",
                       weight=1.74)
metro_network.add_edge("Академіка павлова", "Студентська", weight=1.28)
metro_network.add_edge("Студентська", "Героїв праці", weight=0.92)
metro_network.add_edge("Спортивна", "Метробудівників", weight=0.15)
metro_network.add_edge("Метробудівників", "Захисників України",
                       weight=1.57)
metro_network.add_edge("Захисників України", "Архітектора Бекетова",
                       weight=2.93),
metro_network.add_edge("Архітектора Бекетова", "Держпром", weight=1.16)
metro_network.add_edge("Держпром", "Наукова", weight=2.17)
metro_network.add_edge("Наукова", "Ботанічний сад", weight=2.03)
metro_network.add_edge("Ботанічний сад", "23 серпня", weight=0.83)
metro_network.add_edge("23 серпня", "Олексіївська", weight=2.27)
metro_network.add_edge("Олексіївська", "Перемога", weight=1.19)
metro_network.add_edge("Університет", "Держпром",
                       weight=0.5)

pos = {"Холодна гора": (-0.8, 0.4), "Південний вокзал": (-0.7, 0.4,),
       "Центральний ринок": (-0.6, 0.4), "Майдан конституції": (-0.5, 0.2),
       "Проспект Гагаріна": (-0.45, 0.0), "Спортивна": (-0.3, -0.2),
       "Завод Малишева": (-0.2, -0.4), "Турбоатом": (-0.1, -0.6),
       "Палац спорту": (0.0, -0.8), "Армійська": (0.1, -1.0),
       "Масельського": (0.2, -1.2), "Тракторний завод": (0.3, -1.2),
       "Індустріальна": (0.4, -1.2), "Історичний музей": (-0.45, 0.3),
       "Університет": (-0.3, 0.4), "Пушкінська": (-0.2, 0.5),
       "Київська": (-0.15, 0.65), "Академіка Барабашова": (-0.1, 0.8),
       "Академіка павлова": (-0.05, 0.95), "Студентська": (0.0, 1.1),
       "Героїв праці": (0.05, 1.25), "Метробудівників": (-0.3, -0.4),
       "Захисників України": (-0.2, 0.0), "Архітектора Бекетова": (-0.2, 0.2),
       "Держпром": (-0.27, 0.55), "Наукова": (-0.3, 0.65),
       "Ботанічний сад": (-0.35, 0.8), "23 серпня": (-0.4, 0.95),
       "Олексіївська": (-0.45, 1.1), "Перемога": (-0.5, 1.25)}


# Візуалізація графу
nx.draw(metro_network, pos=pos, with_labels=True, font_weight='bold',
        node_color='lightblue', edge_color='gray', node_size=800,
        font_size=8, font_color='black')

plt.show()


def dijkstra_heap(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes}
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Reconstruct the path
    end_station = max(distances, key=distances.get)
    path = []
    current = end_station
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    # Calculate the total cost
    total_cost = distances[end_station]

    return path, total_cost


# Assuming you have a NetworkX graph named metro_network
start_station = "Холодна гора"
shortest_path, cost = dijkstra_heap(metro_network, start_station)

print(f"Найкоротший шлях від {start_station}: {shortest_path}, Дальність: {cost} км")
