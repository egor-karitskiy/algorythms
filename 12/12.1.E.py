# E. Работа из дома
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Алла осталась работать из дома. Во время её рабочего видеозвонка с Тимофеем и Гошей подошёл Вася. Он решил показать им написанный им недавно код функции, переводящей целое число из десятичной системы в двоичную. Ему было интересно, смогут ли ребята написать более короткую, или более эффективную программу. Тимофей, Алла и Гоша с радостью отвлеклись от работы, чтобы попробовать. А у вас получится обойти Васю?

# Формат ввода
# На вход подается целое число в диапазоне от 0 до 10000.

# Формат вывода
# Выведите двоичное представление этого числа.

# Пример 1
# Ввод	Вывод
# 5
# 101
# Пример 2
# Ввод	Вывод
# 14
# 1110


n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)