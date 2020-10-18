# Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции:
# Взять наиболее ценный предмет, который поместится в рюкзак. Выбрать
# следующий по стоимости товар с учётом того, что для него осталось место в
# рюкзаке. Формат ввода
#
# В первой строке записано целое число с в диапазоне от 0 до 1000 —
# вместимость рюкзака. Во второй — число n — количество предметов. Оно не
# больше 10000. В следующих n строках записано по 2 числа, разделенные
# пробелом: стоимость предмета и его вес. Оба числа не превосходят 1000
# Формат вывода
#
# Нужно в строке вывести в отсортированном порядке номера предметов, которые
# будут выбраны. Номер предмета - это порядковый номер его появления во
# входных данных. (Индексация начинается с нуля)

def primitive_knapsack(items, knapsack_capacity):
    items = sorted(items, key=lambda x: (-x[0], x[1]))
    res = []
    j = 0
    while knapsack_capacity > 0 and j <= len(items) - 1:
        if items[j][1] <= knapsack_capacity:
            res.append(items[j][2])
            knapsack_capacity -= items[j][1]
        j += 1
    res = sorted(res)
    return res


if __name__ == '__main__':
    capacity_input = int(input())
    number_of_items = int(input())
    items_list = []
    for i in range(number_of_items):
        item = list(map(int, input().split()))
        item.append(i)
        items_list.append(item)

    print(*primitive_knapsack(items_list, capacity_input))
