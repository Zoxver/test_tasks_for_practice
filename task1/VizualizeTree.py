from graphviz import Digraph
from AVLTree import AVLNode

def add_edges(graph, node):
    if node is None:
        return
    if node.left:
        graph.edge(str(node.val), str(node.left.val))
        add_edges(graph, node.left)
    if node.right:
        graph.edge(str(node.val), str(node.right.val))
        add_edges(graph, node.right)


def visualize_tree(root: AVLNode) -> Digraph:
    dot = Digraph()
    dot.node(str(root.val))
    add_edges(dot, root)
    return dot