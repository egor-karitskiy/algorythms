# Посылка 36139019

def counting_sort(array, digit_pos):
    array_length = len(array)
    output_array = [0] * array_length
    digits_counter_array = [0] * 10
    exp = 1
    while digit_pos > 1:
        exp *= 10
        digit_pos -= 1
    for i in range(0, array_length):
        base_division = array[i] / exp
        digit = int(base_division % 10)
        digits_counter_array[digit] += 1

    for i in range(1, 10):
        digits_counter_array[i] += digits_counter_array[i - 1]

    i = array_length - 1
    while i >= 0:
        base_division = array[i] / exp
        digit = int(base_division % 10)
        output_array_index = digits_counter_array[digit] - 1
        output_array[output_array_index] = array[i]
        digits_counter_array[digit] -= 1
        i -= 1

    for i in range(0, len(array)):
        array[i] = output_array[i]


def radix_sort(array):
    max_number = max(array)
    max_number_of_digits = len(str(max_number))
    for digit_position in range(1, max_number_of_digits + 1):
        counting_sort(array, digit_position)


if __name__ == '__main__':
    n = input()
    try:
        input_array = list(map(int, input().split()))
    except EOFError:
        input_array = []
    radix_sort(input_array)
    print(*input_array)
