def qs_partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        partition_index = qs_partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


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
    return None


def find_cheating_cockroaches(first_array, second_array):
    res = []
    quick_sort(second_array, 0, len(second_array) - 1)
    for el in first_array:
        if binary_search(second_array, el) is not None and el not in res:
            res.append(el)
    return res


if __name__ == '__main__':
    n = input()
    m = input()
    first_input_array = list(map(int, input().split()))
    try:
        second_input_array = list(map(int, input().split()))
    except EOFError:
        second_input_array = []
    print(*find_cheating_cockroaches(first_input_array, second_input_array))
