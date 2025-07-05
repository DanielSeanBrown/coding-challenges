# spiral-matrix-printing

def spiral_matrix(n):
    spiral = [[0 for _ in range(1, n + 1)] for _ in range(n)]
    directions = ['r', 'd', 'l', 'u']
    distance = [m//2 for m in range(n * 2, 1, -1)]
    pos = [0,-1]
    counter = 0
    direction_count = 0
    for step in distance:
        direction = directions[direction_count % 4]
        direction_count += 1
        for mark in range(step):
            spiral[pos[0]][pos[1]] = counter
            counter += 1
            if direction == 'r':
                pos[1] += 1
            if direction == 'd':
                pos[0] += 1
            if direction == 'l':
                pos[1] -= 1
            if direction == 'u':
                pos[0] -= 1
    spiral[pos[0]][pos[1]] = counter

    return spiral

assert spiral_matrix(3) == [[1, 2, 3],
                            [8, 9, 4],
                            [7, 6, 5]]
assert spiral_matrix(2) == [[1, 2],
                            [4, 3]]
assert spiral_matrix(4) == [[1, 2, 3, 4],
                            [12, 13, 14, 5],
                            [11, 16, 15, 6],
                            [10, 9, 8, 7]]
assert spiral_matrix(7) == [[1, 2, 3, 4, 5, 6, 7],
                            [24, 25, 26, 27, 28, 29, 8],
                            [23, 40, 41, 42, 43, 30, 9],
                            [22, 39, 48, 49, 44, 31, 10],
                            [21, 38, 47, 46, 45, 32, 11],
                            [20, 37, 36, 35, 34, 33, 12],
                            [19, 18, 17, 16, 15, 14, 13]]
