import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.gca().set_title('Click to close')
    plt.gcf().canvas.mpl_connect('button_press_event', lambda event: plt.close() if event.button == 1 else None)
    plt.show()

def depth_first_traversal(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    node.color = get_color(len(visited))
    draw_tree(root)
    node.color = "skyblue"
    if node.left and node.left not in visited:
        depth_first_traversal(node.left, visited)
    if node.right and node.right not in visited:
        depth_first_traversal(node.right, visited)


def breadth_first_traversal(root):
    visited = set()
    queue = [root]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        node.color = get_color(len(visited))
        draw_tree(root)
        node.color = "skyblue"
        if node.left and node.left not in visited:
            queue.append(node.left)
        if node.right and node.right not in visited:
            queue.append(node.right)


def get_color(step):
    # Convert step to RGB color
    r = (step * 25) % 256
    g = (step * 25) % 256
    b = (step * 25) % 256
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

depth_first_traversal(root)

breadth_first_traversal(root)
