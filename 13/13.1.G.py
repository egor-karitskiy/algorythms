def spiral_order(matrix):
    res = []
    lo_x = lo_y = 0
    hi_x = len(matrix[0]) - 1
    hi_y = len(matrix) - 1

    while lo_x <= hi_x and lo_y <= hi_y:
        for x in range(lo_x, hi_x + 1):
            res.append(matrix[lo_y][x])
        lo_y += 1
        for y in range(lo_y, hi_y + 1):
            res.append(matrix[y][hi_x])
        hi_x -= 1
        if not (lo_x <= hi_x and lo_y <= hi_y):
            break
        for x in reversed(range(lo_x, hi_x + 1)):
            res.append(matrix[hi_y][x])
        hi_y -= 1
        for y in reversed(range(lo_y, hi_y + 1)):
            res.append(matrix[y][lo_x])
        lo_x += 1
    return res


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    input_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        input_matrix.append(row)
    for el in spiral_order(input_matrix):
        print(el)
