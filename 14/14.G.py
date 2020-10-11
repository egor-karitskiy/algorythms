def max_perimeter(array):
    n = len(array)
    array.sort(reverse=True)
    for i in range(0, n - 2):
        if array[i] < (array[i + 1] + array[i + 2]):
            return array[i] + array[i + 1] + array[i + 2]
    return 0


if __name__ == '__main__':
    n = input()
    try:
        input_array = list(map(int, input().split()))
    except EOFError:
        input_array = []
    print(max_perimeter(input_array))
