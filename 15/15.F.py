class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def left_view(root):
    queue_for_nodes = []
    res = []
    if root is None:
        return []
    queue_for_nodes = [root, None]

    # заполняем результирующий массив слоями с помощью очереди
    # если есть левый элемент, то его, если нет, то правый элемент
    # между слоями - разделитель None

    while queue_for_nodes:
        current_node = queue_for_nodes[0]
        if current_node:
            res.append(current_node.value)
            while queue_for_nodes[0] is not None:
                current_node = queue_for_nodes[0]
                if current_node.left:
                    queue_for_nodes.append(current_node.left)
                if current_node.right:
                    queue_for_nodes.append(current_node.right)
                queue_for_nodes.pop(0)
            queue_for_nodes.append(None)
        queue_for_nodes.pop(0)
    return res


def solution(tree_root):
    return left_view(tree_root)


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
