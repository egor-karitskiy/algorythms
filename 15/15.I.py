class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def is_BST_recursive(tree_root, left_margin, right_margin):
    if tree_root is None:
        return True
    if tree_root.value < left_margin or tree_root.value > right_margin:
        return False
    return (
            is_BST_recursive(tree_root.left, left_margin, tree_root.value - 1)
            and
            is_BST_recursive(tree_root.right, tree_root.value + 1,
                             right_margin)
    )


def is_BST(tree_root):
    infinite_min = float('-inf')
    infinite_max = float('inf')
    return is_BST_recursive(tree_root, infinite_min, infinite_max)


def solution(tree_root):
    return is_BST(tree_root)


if __name__ == '__main__':
    input_root = Node(2)
    input_root.left = Node(13)
    input_root.right = Node(13)
    input_root.left.left = Node(6)
    input_root.right.right = Node(6)
    # input_root.left.right.left = Node(1)
    # input_root.left.right.right = Node(11)
    # input_root.right.right = Node(9)
    # input_root.right.right.left = Node(16)
    # input_root.right.right.left.left = Node(56)
    # input_root.right.right.left.left.left = Node(10)

    # print(breadth_first_search(input_root))
    print(solution(input_root))
