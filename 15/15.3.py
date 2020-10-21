class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def breadth_first_search(root):
    level = 1
    current_node_and_level = (root, level)
    checking_set = set()
    result = []
    nodes_queue = [current_node_and_level]
    while nodes_queue:
        current_node_and_level = nodes_queue.pop()
        level = current_node_and_level[1]
        if current_node_and_level[0] not in checking_set:
            result.append([current_node_and_level[0].value, level])
            checking_set.add(current_node_and_level[0])
        if current_node_and_level[0].left:
            nodes_queue.insert(0, (current_node_and_level[0].left, level + 1))
        if current_node_and_level[0].right:
            nodes_queue.insert(0, (current_node_and_level[0].right, level + 1))
    output_array = []
    level_array = []
    level = 1
    for value_level_pair in result:
        if value_level_pair[1] == level:
            level_array.append(value_level_pair[0])
        elif value_level_pair[1] > level:
            output_array.append(level_array)
            level_array = [value_level_pair[0]]
            level += 1
    output_array.append(level_array)
    return output_array


def solution(tree_root):
    return breadth_first_search(tree_root)


if __name__ == '__main__':
    input_root = Node(2)
    input_root.left = Node(13)
    input_root.right = Node(5)
    input_root.left.right = Node(6)
    input_root.left.right.left = Node(1)
    input_root.left.right.right = Node(11)
    input_root.right.right = Node(9)
    input_root.right.right.left = Node(16)
    input_root.right.right.left.left = Node(56)
    input_root.right.right.left.left.left = Node(10)

    # print(breadth_first_search(input_root))
    print(solution(input_root))
