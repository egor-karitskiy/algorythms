def is_even(number):
    return number % 2 == 0


def odd_even_sort(array):
    odds = []
    evens = []
    res = []
    for el in array:
        if is_even(el):
            evens.append(el)
        else:
            odds.append(el)
    for i in range(len(evens)):
        res.append(evens.pop(0))
        res.append(odds.pop(0))
    return res


if __name__ == '__main__':
    n = input()
    try:
        input_array = list(map(int, input().split()))
    except EOFError:
        input_array = []
    print(*odd_even_sort(input_array))
