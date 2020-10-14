# Посылка 36404134

class LexicographicalStr(str):
    def __lt__(self, other):
        return self + other < other + self

    def __gt__(self, other):
        return self + other > other + self


def biggest_integer(array):
    array = sorted(array, key=LexicographicalStr, reverse=True)
    return ''.join(array)


if __name__ == '__main__':
    input()
    input_array = input().split()
    print(biggest_integer(input_array))
