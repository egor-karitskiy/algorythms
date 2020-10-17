# Посылка 36404498

def counting_sort(array, digit_pos):
    output_array = [0] * len(array)
    digits_counter_array = [0] * 10
    elements_result_positions_array = [0] * 10
    exp = 10 ** digit_pos
    order_index = 0

    for element in array:
        digit = element // exp % 10
        digits_counter_array[digit] += 1

    for i in range(9):
        order_index += digits_counter_array[i]
        if digits_counter_array[i] > 0:
            elements_result_positions_array[i] = order_index

    for element in reversed(array):
        digit = element // exp % 10
        position_of_element_in_output_array = (
                elements_result_positions_array[digit] - 1)
        output_array[position_of_element_in_output_array] = element
        elements_result_positions_array[digit] -= 1

    for i in range(len(array)):
        array[i] = output_array[i]


def radix_sort(array):
    max_number = max(array)
    max_number_of_digits = len(str(max_number))
    for digit_position in range(max_number_of_digits):
        counting_sort(array, digit_position)


if __name__ == '__main__':
    input()
    input_array = list(map(int, input().split()))
    radix_sort(input_array)
    print(*input_array)
