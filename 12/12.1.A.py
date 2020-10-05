# A. Значения функции

# Младший брат Аллы Вася делает тест по математике: вычисляет значение функций в различных точках. 
# Стоит отличная погода, и друзья зовут Васю гулять. Но мама разрешила мальчику пойти на улицу только после того, как он закончит тест. 
# К сожалению, Вася пока не умеет программировать. Зато Алла умеет. Она решила помочь брату и написала код функции y = ax2 + bx + c. И вы напишите.

# Формат ввода
# На вход через пробел подаются числа a, x, b, c.

# Формат вывода
# Выведите одно число - значение функции в точке x.

# Пример 1
# Ввод	Вывод
# -8 -5 -2 7
# -183
# Пример 2
# Ввод	Вывод
# 8 2 9 -10
# 40
# Примечания
# Решение должно работать за O(1) и использовать O(1) дополнительной памяти.


a, x, b, c = input().split()
a = int(a)
x = int(x)
b = int(b)
c = int(c)
y = a * x ** 2 + b * x + c
print(y)