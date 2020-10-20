# Нужно реализовать класс StackMax, который поддерживает операцию
# определения максимума среди всех элементов в стеке. Класс также должен
# поддерживать все операции, реализованные в классе Stack, из урока. При
# этом в классе StackMax может быть реализовано не более трёх методов. Стек
# может содержать только данные типов, поддерживающих операцию сравнения.
# Иначе операция поиска максимума будет некорректной.


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = None

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.is_empty():
            self.max = item
            self.items.append(item)
        elif item > self.max:

            # если item > self.max, то
            # item - self.max > 0, тогда прибавив item к обеим частям
            # неравенства получим
            # item - self.max + item > item, тогда получаем
            # 2 * item - self.max > item
            # то есть, вместо item мы можем смело сохранить в стеке вот эту
            # конструкцию 2 * item - self.max, которая точно больше item и
            # связывает текущий максимум и значение.

            tmp = 2 * item - self.max
            self.items.append(tmp)
            self.max = item
        else:
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        if self.peek() < self.max:
            self.items.pop()
            return None

        # если self.max < self.peek(), тогда
        # self.max - self.peek() < 0 и, прибавив self.max к обеим частям
        # неравенства, получим
        # self.max - self.peek() + self.max < self.max, то есть,
        # 2 * self.max - self.peek() < self.max
        # вот так и восстановим предыдущее значение self.max, когда будем
        # удалять текущий максимум

        self.max = 2 * self.max - self.peek()
        self.items.pop()
        return None

    def peek(self):
        if self.is_empty():
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.is_empty():
            return None
        return self.max


if __name__ == '__main__':
    stack = StackMaxEffective()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'get_max':
            print(stack.get_max())
        elif command[0] == 'pop':
            if stack.pop() is not None:
                print(stack.pop())
