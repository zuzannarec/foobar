MOVES = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (1, -2), (-1, 2), (1, 2)]
BOARD_SIZE = 8


def solution(src, dest):
    paths = dict()  # square id, number of moves to get to x, y from the src
    _solution(src, dest, paths, 0)
    return paths[dest]


def getX(squareId):
    return squareId // BOARD_SIZE


def getY(squareId):
    return squareId % BOARD_SIZE


def getSquareId(x, y):
    return x * BOARD_SIZE + y


def _solution(currentLocation, dest, paths, count):
    if currentLocation in paths.keys() and count > paths[currentLocation]:
        return
    paths[currentLocation] = count
    if currentLocation == dest:
        return
    for move in MOVES:
        x = getX(currentLocation) + move[0]
        y = getY(currentLocation) + move[1]
        newSquareId = getSquareId(x, y)
        if x < BOARD_SIZE and x >= 0 and y < BOARD_SIZE and y >= 0:
            _solution(newSquareId, dest, paths, paths[currentLocation] + 1)
    return


print(solution(0, 1))

print(solution(19, 36))
