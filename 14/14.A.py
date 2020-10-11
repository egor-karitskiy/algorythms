def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    n = input()
    input_array = list(map(int, input().split()))
    bubble_sort(input_array)
    print(*input_array)
