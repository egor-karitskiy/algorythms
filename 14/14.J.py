# J. Относительная сортировка

# Кондратий ввел новый метод сортировки - Относительная сортировка.
# Идея метода следующая. С помощью образца - массива уникальных чисел, задается порядок.
# В соответствии с этим порядком и должны сортироваться числа.
# Но метод еще требует доработки. Пока не известно, как сортировать числа, которые не входят в образец.
# Так что такие числа нужно выводить в конце в соответствии со стандартной сортировкой.

# Формат ввода
# В первой строке задано количество чисел, которые нужно отсортировать, n. Оно не превосходит 1500.
# В следующей строке через пробел заданы n чисел, каждое из которых не превосходит 1000.
# В третей строке задана длина образца m. Это число не превосходит 1500.
# В следующей строке записан образец. Он состоит из чисел, не превосходящих 1000.
# Гарантируется, что среди чисел, которые нужно отсортировать, присутствуют все числа из образца.

# Формат вывода
# Выведите в строку через пробел числа, отсортированные Относительной сортировкой.

def relative_sort(array, sample):
    count_array = {x: y for x in sample for y in range(1)}
    num_sample_out = []
    for number in array:
        if number in sample:
            count_array[number] += 1
        else:
            num_sample_out.append(number)
    num_sample_out = sorted(num_sample_out)        
    pre_result = []
    for key, value in count_array.items():
        cnt = value
        while cnt != 0:
            pre_result.append(key)
            cnt -= 1
    result = pre_result + num_sample_out
    for n in result:
        print(n, end=' ')  
        

with open('input.txt', 'r', encoding='utf8') as f: 
    n = int(f.readline())
    array = [int(x) for x in f.readline().split()]
    m = int(f.readline())
    sample = [int(x) for x in f.readline().split()]
    relative_sort(array, sample)
    