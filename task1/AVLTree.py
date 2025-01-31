from typing import Union


class AVLNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Union[AVLNode, None] = left
        self.right: Union[AVLNode, None] = right
        self.height: int = 1


def get_height(node: AVLNode) -> int:
    return 0 if not node else node.height


def update_height(node: AVLNode) -> None:
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def get_balance(node: AVLNode) -> int:
    """
       Возвращает баланс-фактор узла (разницу высот левого и правого поддеревьев).
       Используется для проверки сбалансированности АВЛ-дерева.
    """
    return 0 if not node else get_height(node.left) - get_height(node.right)


def get_min_node(node: AVLNode) -> Union[AVLNode, None]:
    return node if (not node.left) or (not node) else get_min_node(node.left)


def get_max_node(node: AVLNode) -> Union[AVLNode, None]:
    return node if (not node.right) or (not node) else get_max_node(node.right)


def right_rotate(b: AVLNode) -> AVLNode:
    """
        Выполняет правый поворот вокруг узла `b`.
        Используется для балансировки АВЛ-дерева.
    """
    a = b.left
    temp = a.right

    a.right = b
    b.left = temp

    update_height(b)
    update_height(a)

    return a


def left_rotate(a: AVLNode) -> AVLNode:
    """
    Выполняет левый поворот вокруг узла `a`.
    Используется для балансировки АВЛ-дерева.
    """
    b = a.right
    temp = b.left

    b.left = a
    a.right = temp

    update_height(a)
    update_height(b)

    return b


def left_right_rotate(node: AVLNode) -> AVLNode:
    node.left = left_rotate(node.left)
    return right_rotate(node)


def right_left_rotate(node: AVLNode) -> AVLNode:
    node.right = right_rotate(node.right)
    return left_rotate(node)


def balance(node: AVLNode) -> AVLNode:
    """
       Балансирует узел, если его баланс-фактор выходит за пределы [-1, 1].
       В зависимости от типа дисбаланса выполняется определенный поворот.
    """
    balance = get_balance(node)

    if balance == -2:
        if get_balance(node.right) == 1:
            return right_left_rotate(node)
        return left_rotate(node)

    if balance == 2:
        if get_balance(node.left) == -1:
            return left_right_rotate(node)
        return right_rotate(node)

    return node


def insert(node, val: int) -> AVLNode:
    if not node:
        return AVLNode(val)

    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    update_height(node)
    return balance(node)


def delete(node: AVLNode, val) -> Union[AVLNode, None]:
    if not node:
        return None

    if node.right and val == 'max':
        node.right = delete(node.right, val)
    elif node.left and val == 'min':
        node.left = delete(node.left, val)
    elif isinstance(val, int) and val < node.val:
        node.left = delete(node.left, val)
    elif isinstance(val, int) and val > node.val:
        node.right = delete(node.right, val)
    else:
        if (not node.left) or (not node.right):
            return node.right if not node.left else node.left

        temp = get_min_node(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)

    update_height(node)
    return balance(node)


def search(node: AVLNode, val: int) -> bool:
    if not node:
        return False
    if node.val == val:
        return True
    return search(node.left, val) if val < node.val else search(node.right, val)


def split(root: AVLNode, val: int):
    """
        Делит АВЛ-дерево на два разных АВЛ-дерева по значению `val`
    """
    left_elements = []
    right_elements = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        if node.val <= val:
            left_elements.append(node.val)
        else:
            right_elements.append(node.val)
        traverse(node.right)

    traverse(root)
    return build_avl(left_elements), build_avl(right_elements)


def merge(left_tree: AVLNode, right_tree: AVLNode) -> AVLNode:
    """
        Объединяет два АВЛ-дерева в одно сбалансированное.
        Использует максимальный элемент левого дерева или минимальный элемент правого.
    """
    if not left_tree:
        return right_tree
    if not right_tree:
        return left_tree

    if get_height(left_tree) > get_height(right_tree):
        max_left = get_max_node(left_tree)
        left_tree = delete(left_tree, max_left.val)

        max_left.left = left_tree
        max_left.right = right_tree

        update_height(max_left)
        return balance(max_left)

    else:
        min_right = get_min_node(right_tree)
        right_tree = delete(right_tree, min_right.val)

        min_right.left = left_tree
        min_right.right = right_tree

        update_height(min_right)
        return balance(min_right)


def build_avl(sorted_list):
    """
        Строит АВЛ-дерево из отсортированного массива.
    """
    if not sorted_list:
        return None
    mid = len(sorted_list) // 2
    node = AVLNode(sorted_list[mid])
    node.left = build_avl(sorted_list[:mid])
    node.right = build_avl(sorted_list[mid+1:])
    update_height(node)
    return node


def count_nodes(root):
    return 0 if not root else 1 + count_nodes(root.left) + count_nodes(root.right)


def in_order_traversal(root: AVLNode):
    elements = []

    def traverse(node):
        if node:
            traverse(node.left)
            elements.append(node.val)
            traverse(node.right)

    traverse(root)
    return elements


def check_avl(root: AVLNode) -> bool:
    """
        Проверяет, является ли дерево АВЛ-деревом.
        Проверка выполняется рекурсивно для всех узлов.
    """
    if not root:
        return True
    balance = abs(get_balance(root))
    return balance <= 1 and check_avl(root.left) and check_avl(root.right)







