# Посылка 35484976

def binary_search(array, value):
    lower_index = 0
    higher_index = len(array) - 1
    while lower_index <= higher_index:
        middle = int((lower_index + higher_index) / 2)
        if array[middle] < value:
            lower_index = middle + 1
        elif array[middle] > value:
            higher_index = middle - 1
        else:
            return middle
    return -1


def find_pivot_point(array):
    lower_index = 0
    higher_index = len(array) - 1
    while lower_index <= higher_index:
        if lower_index == higher_index:
            return higher_index
        middle = (higher_index + lower_index) // 2
        if array[middle + 1] < array[middle]:
            return middle
        if array[lower_index] > array[middle]:
            higher_index = middle - 1
        else:
            lower_index = middle + 1
    return -1


def rotated_search(array, value):
    pivot_point = find_pivot_point(array)
    if pivot_point == -1:
        return binary_search(array, value)
    elif array[pivot_point] == value:
        return pivot_point
    elif array[0] <= value:
        return binary_search(array[0:pivot_point - 1], value)
    elif binary_search(array[pivot_point + 1:], value) == -1:
        return -1
    res = binary_search(array[pivot_point + 1:], value)
    return pivot_point + 1 + res


if __name__ == '__main__':
    list_length = int(input())
    search_value = int(input())
    broken_circle_array = list(map(int, input().split()))
    print(rotated_search(broken_circle_array, search_value))
