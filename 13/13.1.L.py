# Для каждой ступеньки известно, на какое максимальное количество ступенек
# вверх с неё можно допрыгнуть. Нужно помочь Евлампии определить, сможет ли
# она добраться с нижней ступеньки на верхнюю. Формат ввода
#
# В первой строке записано число n - количество ступенек. Оно не превосходит
# 10000 В следующей строке через пробел записано n неотрицательных чисел,
# каждое из которых не больше 1000. Формат вывода
#
# Нужно вывести True, если получится добраться с 1 ступеньки до верхней,
# иначе — False
#

def is_upstairs_possible(max_stairs_to_jump_array):
    if len(max_stairs_to_jump_array) <= 1:
        return True

    if max_stairs_to_jump_array[0] == 0:
        return False

    max_stairs_to_jump = max_stairs_to_jump_array[0]
    step = max_stairs_to_jump_array[0]
    jump = 1

    for i in range(1, len(max_stairs_to_jump_array)):
        if i == len(max_stairs_to_jump_array) - 1:
            return True
        max_stairs_to_jump = max(max_stairs_to_jump,
                                 i + max_stairs_to_jump_array[i]
                                 )
        step -= 1
        if step == 0:
            jump += 1
            if i >= max_stairs_to_jump:
                return False
            step = max_stairs_to_jump - i
    return False


if __name__ == '__main__':
    input()
    stairs_array = list(map(int, input().split()))
    print(is_upstairs_possible(stairs_array))
