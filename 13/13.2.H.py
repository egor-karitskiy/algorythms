# H. Генератор скобок

# В Удотинске объявлен конкурс. Нужно написать самую быструю реализацию функции,
# которая генерирует все правильные скобочные последовательности длины n.
# Вид скобок только один: ( )

# Формат ввода
# На вход функция принимает n - целое число от 0 до 10.

# Формат вывода
# Функция должна напечатать все возможные скобочные последовательности заданной длины в лексикографическом порядке.

# Примечания
# Строка A лексикографически меньше другой строки B, если она является точным собственным префиксом B
# или если существует такой индекс i, i < |A|, i < |B|, что A[i] < B[i].

def get_bracket_sequence(n, bracket_sequence, cnt, indx):
    if (cnt <= n-indx-2):
        bracket_sequence[indx] = '('
        get_bracket_sequence(n, bracket_sequence, cnt+1, indx+1)
    if cnt > 0:
        bracket_sequence[indx] = ')'
        get_bracket_sequence(n, bracket_sequence, cnt-1, indx+1)
    if indx == n:
        if cnt == 0:
            print(''.join(bracket_sequence))
            
            
if __name__ == '__main__':
    n = int(input())
    bracket_sequence = [0]*2*n
    cnt = 0
    indx = 0
    get_bracket_sequence(n*2, bracket_sequence, cnt, indx)
    