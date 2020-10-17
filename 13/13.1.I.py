# Гоше стало интересно, можно ли разбить все заработанные им во время игры в
# Лампу очки на две части так, чтобы сумма в них была одинаковой. Формат ввода
#
# В первой строке записано число элементов массива n. Оно не превосходит
# 10000 Далее в строку записаны n целых неотрицательных чисел, каждое из
# которых не превосходит 10000 Формат вывода
#
# Нужно вывести True, если произвести такое разбиение возможно, иначе — False
#
#

#
# def is_equal_sums_possible_greedy_classical_algorithm(numbers):
#     first_partitioned_array = []
#     second_partitioned_array = []
#     sum_first = 0
#     sum_second = 0
#     for n in sorted(numbers, reverse=True):
#         if sum_first < sum_second:
#             first_partitioned_array.append(n)
#             sum_first = sum_first + n
#         else:
#             second_partitioned_array.append(n)
#             sum_second = sum_second + n
#     if sum_first == sum_second:
#         return True
#     return sum_first, sum_second

import heapq


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)


def is_equal_sums_possible_using_heap(num_arr):
    if len(num_arr) <= 1:
        return False
    heap = MaxHeap(num_arr)
    elem1 = heap.pop()
    elem2 = heap.pop()
    while elem2 != 0:
        heap.push(abs(elem1 - elem2))
        heap.push(0)
        elem1 = heap.pop()
        elem2 = heap.pop()
    if elem1 == 0:
        return True
    return False


def is_equal_sums_possible(array):
    if len(array) <= 1:
        return False
    array = sorted(array)
    el1 = array.pop()
    el2 = array.pop()
    while el2 != 0:
        array.append(abs(el1 - el2))
        array.append(0)
        array = sorted(array)
        el1 = array.pop()
        el2 = array.pop()
    if el1 == 0:
        return True
    return False


if __name__ == '__main__':
    input()
    input_array = list(map(int, input().split()))
    print(is_equal_sums_possible(input_array))
    # print(is_equal_sums_possible_using_heap(input_array))
