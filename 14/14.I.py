def colored_clothes(array):
    pinks = []
    yellows = []
    raspberries = []
    for el in array:
        if el == 0:
            pinks.append(el)
        elif el == 1:
            yellows.append(el)
        else:
            raspberries.append(el)
    return pinks + yellows + raspberries


if __name__ == '__main__':
    n = input()
    try:
        input_array = list(map(int, input().split()))
    except EOFError:
        input_array = []
    print(*colored_clothes(input_array))