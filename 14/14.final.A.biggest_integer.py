# Посылка 36124975

def lexicographically_bigger(str_x: str, str_y: str):
    str_xy = str_x + str_y
    str_yx = str_y + str_x
    if str_xy > str_yx:
        return True
    return False


def biggest_integer(array):
    array = list(map(str, array))
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and lexicographically_bigger(key, array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return ''.join(array)


if __name__ == '__main__':
    n = input()
    try:
        input_array = list(map(int, input().split()))
    except EOFError:
        input_array = []
    print(biggest_integer(input_array))
