
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def is_axis_symmetric(tree_root1, tree_root2):
    if tree_root2 is None and tree_root1 is None:
        return True
    elif tree_root2 is not None and tree_root1 is not None:
        if tree_root2.value == tree_root1.value:
            return (is_axis_symmetric(tree_root1.left, tree_root2.right) and
                    is_axis_symmetric(tree_root1.right, tree_root2.left)
                    )
    return False


def solution(tree_root):
    return is_axis_symmetric(tree_root, tree_root)


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