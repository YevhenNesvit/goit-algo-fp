import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови бінарної купи зі списку
def build_heap(arr):
    heap = []
    for val in arr:
        heapq.heappush(heap, val)
    return heap_to_tree(heap, 0)

# Функція для перетворення масиву купи у бінарне дерево
def heap_to_tree(heap, idx):
    if idx < len(heap):
        node = HeapNode(heap[idx])
        node.left = heap_to_tree(heap, 2 * idx + 1)
        node.right = heap_to_tree(heap, 2 * idx + 2)
        return node

# Створення бінарної купи зі списку
heap_root = build_heap([4, 10, 5, 1, 3, 8, 7])
# Відображення бінарної купи
draw_heap(heap_root)
