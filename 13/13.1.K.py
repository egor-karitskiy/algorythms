# Дочь Кондратия Евлампия решила купить в ипотеку несколько домов на территории Трешландии.
# Она нашла n объявлений о продаже. Известна стоимость каждого дома в трешландских франках. Евлампия может позволить себе взять ипотеку на общую сумму k франков. Нужно помочь ей определить, какое наибольшее количество домов можно купить на эти деньги.
# Формат ввода
#
# В первой строке через пробел записаны целые числа n и k
# n - количество домов, которые рассматривает Евлампия, оно не превосходит 1000
# k - общий бюджет, не превосходит 10000
# В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не превосходит 10000. Все стоимости - целые числа.
# Формат вывода
#
# Выведите число, равное максимально возможному числу домов, которые может купить Евлампия

def max_estate_affordable(available_funds, prices_array):
    prices_array = sorted(prices_array)
    total_price = 0

    if len(prices_array) == 1 and prices_array[0] <= available_funds:
        return 1

    for i in range(len(prices_array)):
        total_price += prices_array[i]
        if total_price > available_funds:
            return i
    return i + 1


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    house_prices = list(map(int, input().split()))
    print(max_estate_affordable(k, house_prices))
