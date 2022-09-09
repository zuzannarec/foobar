def uniqueDialsByKnight(start, n):
    if n == 0:
        return 1
    result = 0
    for neighbour in neighbours(start):
        result += uniqueDialsByKnight(neighbour, n - 1)
    return result

# O(2^n)

def uniqueDialsByKnight(start, n, memo={}):
    if n == 0:
        return 1
    if (start, n) in memo:
        return memo[(start, n)]
    result = 0
    for neighbour in neighbours(start):
        result += uniqueDialsByKnight(neighbour, n - 1, memo)
    memo[(start, n)] = result

    return result
# O(n)

def uniqueDialsByKnight(start, n):
    previous = [1] * 10
    count = 1
    while count < n:
        current = [0] * 10
        for position in range(len(current)):
            for neighbour in neighbours(position):
                current[position] += previous[neighbour]
        previous = current
        count += 1
    return previous[start]
# O(n)

def neighbours(start):
    NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)}
    return NEIGHBORS_MAP[start]