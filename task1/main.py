import time
import random
from AVLTree import *
from VizualizeTree import visualize_tree


def generate_data(size, order='random'):
    if order == 'ascending':
        return list(range(size))
    elif order == 'descending':
        return list(range(size, 0, -1))
    elif order == 'random':
        return random.sample(range(size), size)



if __name__ == "__main__":
    sizes = [100]
    for size in sizes:
        data_random = generate_data(size, 'random')

        root = None
        for val in data_random:
            root = insert(root, val)

        print(get_max_node(root).val, get_min_node(root).val)
        print(search(root, 65))
        print(in_order_traversal(root))

        pz = in_order_traversal(root)
        sp = 50
        a, b = split(root, sp)
        z = merge(a, b)
        px = in_order_traversal(z)
        print(pz == px)
        print(check_avl(root), check_avl(a), check_avl(b), check_avl(z))

        tree_viz = visualize_tree(root)
        tree_viz.render('avl_tree', format='svg')
        tree_viz = visualize_tree(a)
        tree_viz.render('avl_tree_a', format='svg')
        tree_viz = visualize_tree(b)
        tree_viz.render('avl_tree_b', format='svg')
        tree_viz = visualize_tree(z)
        tree_viz.render('avl_tree_z', format='svg')