# Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть
# про сбалансированные деревья. Он решил написать функцию, которая
# определяет, сбалансировано ли дерево. Дерево считается сбалансированным,
# если левое и правое поддеревья каждого узла отличаются по высоте не
# больше, чем на один. Функция должна вернуть True, если дерево
# сбалансировано в соответствии с критерием из условия, иначе - False.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def tree_height(tree_root):
    if tree_root is None:
        return 0
    return max(tree_height(tree_root.left), tree_height(tree_root.right)) + 1


def solution(tree_root):
    if tree_root is None:
        return True
    height_left = tree_height(tree_root.left)
    height_right = tree_height(tree_root.right)
    if (
        abs(height_left - height_right) <= 1 and
        solution(tree_root.left) and
        solution(tree_root.right)
    ):
        return True
    return False


if __name__ == '__main__':
    input_root = Node(2)
    input_root.left = Node(13)
    input_root.right = Node(5)
    # input_root.left.right = Node(6)
    # input_root.left.right.left = Node(1)
    # input_root.left.right.right = Node(11)
    # input_root.right.right = Node(9)
    # input_root.right.right.left = Node(16)
    # input_root.right.right.left.left = Node(56)
    # input_root.right.right.left.left.left = Node(10)

    print(solution(input_root), tree_height(input_root))
