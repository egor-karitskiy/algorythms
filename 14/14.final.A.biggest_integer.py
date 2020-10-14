# Посылка 36295621

class LexicographicalStr(str):
    def __ge__(self, other):
        return self + other >= other + self

    def __le__(self, other):
        return self + other <= other + self

    def __lt__(self, other):
        return self + other < other + self

    def __gt__(self, other):
        return self + other > other + self


def biggest_integer(array):
    array = sorted(array, reverse=True)
    return ''.join(array)


if __name__ == '__main__':
    input()
    input_array = list(map(LexicographicalStr, input().split()))
    print(biggest_integer(input_array))
