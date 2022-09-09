def solution(A, B, C, D):
    perms = [[A, B], [A, C], [A, D], [B, C], [B, D], [C, D]]
    maxSqDist = 0
    for idx0 in range(len(perms) - 1):
        for idx1 in range(idx0 + 1, len(perms)):
            maxSqDist = max(maxSqDist, sqDist(perms[idx0], perms[idx1]))
    return maxSqDist


def sqDist(point1, point2):
    return abs(point1[0] - point2[0])**2 + abs(point1[1] - point2[1])**2


print(solution(1, 1, 2, 3))