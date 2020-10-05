# E. Кондратиева система шифрования

# Ещё один важный математический объект — факториал. 
# Факториал - это произведение чисел от 1 до n. 
# В Трешландии существует своя система кодирования - Кондратиева.
# Число в этой системе кодируется через значение факториала.
# Дочь Кондратия, Евлампия, использует эту систему для шифрования пароля от айфона.
# Помогите Евлампии зашифровать пароль. Нужно написать рекурсивную реализацию функции, вычисляющей факториал заданного числа.

# Формат ввода
# На вход подаётся целое положительное число в диапазоне от 0 до 20.

# Формат вывода
# Нужно вывести факториал заданного числа.

# Примечания
# Решение должно быть реализовано с помощью рекурсивной функции.

def get_factorial(n):
    if n == 0:
        return 1
    return n * get_factorial((n-1))

if __name__ == '__main__':
    n = int(input())
    print(get_factorial(n))
    