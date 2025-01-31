import pytest
from AVLTree import *

def create_sample_tree():
    root = None
    for value in [30, 20, 40, 10, 25, 35, 50]:
        root = insert(root, value)
    return root


def test_insert_root():
    root = insert(None, 30)
    assert root.val == 30


def test_insert_left_child():
    root = insert(None, 30)
    root = insert(root, 20)
    assert root.left.val == 20


def test_insert_right_child():
    root = insert(None, 30)
    root = insert(root, 40)
    assert root.right.val == 40


def test_insert_height():
    root = None
    for value in [30, 20, 40, 10, 25]:
        root = insert(root, value)
    assert get_height(root) == 3


def test_delete_leaf_node():
    root = create_sample_tree()
    root = delete(root, 10)
    assert get_min_node(root).val == 20


def test_delete_root():
    root = create_sample_tree()
    root = delete(root, 30)
    assert root.val == 35


def test_delete_max_node():
    root = create_sample_tree()
    root = delete(root, 'max')
    assert root.right.right == None


def test_delete_min_node():
    root = create_sample_tree()
    root = delete(root, 'min')
    assert get_min_node(root).val == 20


def test_get_min_node():
    root = create_sample_tree()
    min_node = get_min_node(root)
    assert min_node.val == 10


def test_balance_after_insertions():
    root = create_sample_tree()
    root = insert(root, 5)
    assert get_balance(root) == 1


def test_balance_after_right_rotation():
    root = create_sample_tree()
    root = insert(root, 5)
    root = insert(root, 4)
    assert root.left.left.val == 5


def test_balance_after_left_rotation():
    root = create_sample_tree()
    root = insert(root, 55)
    root = insert(root, 65)
    assert root.right.right.val == 55


def test_merge():
    left_tree = None
    right_tree = None

    for value in [10, 20, 30]:
        left_tree = insert(left_tree, value)
    for value in [40, 50, 60]:
        right_tree = insert(right_tree, value)

    merged_tree = merge(left_tree, right_tree)
    assert in_order_traversal(merged_tree) == [10, 20, 30, 40, 50, 60] and check_avl(merged_tree) and count_nodes(merged_tree) == 6


def test_split():
    root = None
    for value in [10, 20, 30, 40, 50, 60]:
        root = insert(root, value)

    left_tree, right_tree = split(root, 30)
    assert in_order_traversal(right_tree) == [40, 50, 60] and in_order_traversal(left_tree) == [10, 20, 30]


def test_search():
    root = create_sample_tree()
    assert search(root, 5) is False


def test_check_avl():
    root = create_sample_tree()
    assert check_avl(root) is True