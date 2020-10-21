# У Евлампии есть брошь с бриллиантами в виде дерева. В каждом узле дерева
# есть какое-то количество бриллиантов. Помогите выяснить, какое
# максимальное количество бриллиантов есть в одном узле. В Трешландии может
# быть и отрицательное число драгоценных камней в украшении.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(tree_root):
    if tree_root is None:
        return float('-inf')
    search_left = solution(tree_root.left)
    search_right = solution(tree_root.right)
    return max(tree_root.value, search_left, search_right)


if __name__ == '__main__':
    input_root = Node(2)
    input_root.left = Node(13)
    input_root.right = Node(5)
    input_root.left.right = Node(6)
    input_root.left.right.left = Node(1)
    input_root.left.right.right = Node(11)
    input_root.right.right = Node(9)
    input_root.right.right.left = Node(16)

    print(solution(input_root))
