def riverSizes(matrix):
    output = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1 or matrix[i][j] == 0:
                continue
            output.append(_riverSizes(matrix, i, j))
            return output


def _riverSizes(matrix, x, y):
    if matrix[x][y] == 0:
        return 0
    matrix[x][y] = -1
    output = 1
    if x + 1 < len(matrix) and matrix[x + 1][y] != -1:
        output += _riverSizes(matrix, x + 1, y)
    if x - 1 >= 0 and matrix[x - 1][y] != -1:
        output += _riverSizes(matrix, x - 1, y)
    if y + 1 < len(matrix[0]) and matrix[x][y + 1] != -1:
        output += _riverSizes(matrix, x, y + 1)
    if y - 1 >= 0 and matrix[x][y - 1] != -1:
        output += _riverSizes(matrix, x, y - 1)
    return output



matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
print(riverSizes(matrix))
# print(_riverSizes(matrix, 0, 0))