# C. Списочная форма

# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Вася просил Аллу помочь решить задачу. На этот раз по информатике.

# Для неотрицательного целого числа X списочная форма — это массив его цифр слева направо. 
# К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход подается количество цифр числа Х, 
# списочная форма неотрицательного числа Х и число K. Числа К и Х не превосходят 10000.

# Нужно вернуть списочную форму числа X + K.

# Формат ввода
# В первой строке - длина списочной формы числа X. На следующей строке - сама списочная форма с цифрами записанными через пробел. 
# В последней строке записано число K.

# Формат вывода
# Выведите списочную форму числа X+K.

# Пример 1
# Ввод	Вывод
# 4
# 1 2 0 0
# 34
# 1 2 3 4
# Пример 2
# Ввод	Вывод
# 2
# 9 5
# 17
# 1 1 2
# Примечания
# Решение должно работать за O(N), где N - максимум из длин двух чисел на входе. 
# Разрешается использовать O(N) дополнительной памяти.


x_len = int(input())
x_map = map(int, input().split(maxsplit = 10000))
x_list = list(x_map)

if len(x_list) != x_len:
    print('error, please enter correct lenght/list')
x = sum([value * 10 ** index for index, value in enumerate(x_list[::-1])])

k = int(input())
while k <= 10000 and 0 < x <= 10000:
    sum = x + k
    sum_list = [int(i) for i in str(sum)]
    print(" ".join(map(str, sum_list)))
    break